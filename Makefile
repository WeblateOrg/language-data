# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

all: weblate_language_data/languages.py weblate_language_data/plural_tags.py PLURALS_DIFF.md $(wildcard weblate_language_data/locale/*/LC_MESSAGES/django.po) $(filter-out $(patsubst modules/cldr-json/cldr-json/cldr-localenames-full/main/%/languages.json,languages-po/%.po,$(wildcard modules/cldr-json/cldr-json/cldr-localenames-full/main/*/languages.json)),languages-po/en.po)

weblate_language_data/languages.py: languages.csv aliases.csv cldr.csv extraplurals.csv default_countries.csv population.csv qt.csv rtl.csv case-insensitive.csv $(wildcard modules/iso-codes/data/iso_*.json) scripts/generate-language-data.py
	./scripts/generate-language-data.py

PLURALS_DIFF.md: languages.csv cldr.csv gettext.csv translate.csv scripts/list-diff.py
	./scripts/list-diff.py
	prek run --files PLURALS_DIFF.md || true

cldr.csv: modules/cldr-json/cldr-json/cldr-core/supplemental/plurals.json modules/cldr-json/cldr-json/cldr-localenames-full/main/en/languages.json scripts/export-cldr.py languages.csv
	./scripts/export-cldr.py

rtl.csv: modules/cldr-json/cldr-json/cldr-misc-full/main/*/layout.json scripts/export-cldr-orientation.py languages.csv
	./scripts/export-cldr-orientation.py

case-insensitive.csv: modules/cldr-json/cldr-json/cldr-core/scriptMetadata.json modules/cldr-json/cldr-json/cldr-core/supplemental/languageData.json scripts/export-cldr-case.py languages.csv
	./scripts/export-cldr-case.py

qt.csv: modules/qttools/src/linguist/shared/numerus.cpp scripts/export-qt.py languages.csv
	./scripts/export-qt.py

gettext.csv: modules/gettext/gettext-tools/src/plural-table.c scripts/export-gettext.py
	./scripts/export-gettext.py

.PRECIOUS: languages-po/%.po
languages-po/%.po: modules/cldr-json/cldr-json/cldr-localenames-full/main/en/languages.json modules/cldr-json/cldr-json/cldr-localenames-full/main/%/languages.json scripts/export-languages-po.py
	./scripts/export-languages-po.py $*

LANG_DATA = $(shell python ./scripts/get-lang-data-path.py)

translate.csv: $(LANG_DATA) scripts/export-translate.py
	./scripts/export-translate.py

weblate_language_data/plural_tags.py: modules/cldr-json/cldr-json/cldr-core/supplemental/plurals.json scripts/export-plural-tags.py modules/cldr-json/cldr-json/cldr-core/supplemental/aliases.json aliases.csv
	./scripts/export-plural-tags.py

aliases.csv: scripts/export-iso-aliases.py modules/iso-codes/data/iso_639-2.json modules/iso-codes/data/iso_639-3.json modules/cldr-json/cldr-json/cldr-core/supplemental/aliases.json
	./scripts/export-iso-aliases.py
	@touch $@

population.csv: modules/cldr-json/cldr-json/cldr-core/supplemental/territoryInfo.json scripts/export-cldr-population.py
	./scripts/export-cldr-population.py

languages.csv: modules/iso-codes/data/iso_639-2.json scripts/export-iso-languages.py scripts/add-iso-population.py aliases.csv population.csv
	./scripts/export-iso-languages.py
	./scripts/add-iso-population.py
	@touch $@

weblate_language_data/locale/django.pot: weblate_language_data/languages.py weblate_language_data/plurals.py
	xgettext --add-comments=Translators: --msgid-bugs-address=https://github.com/WeblateOrg/language-data/issues/ --from-code=utf-8 --language=python --no-location --package-name="Weblate Language Data" --output=$@.1 weblate_language_data/*.py
	cp $@.1 $@.2
	./scripts/copy-pot-date.sh $@ $@.2
	if cmp $@ $@.2 ; then touch $@ ; else cp $@.1 $@; fi
	rm $@.1 $@.2


.SECONDEXPANSION:
weblate_language_data/locale/%/LC_MESSAGES/django.po: weblate_language_data/locale/django.pot $$(wildcard modules/iso-codes/iso_639-3/%.po modules/iso-codes/iso_639-2/%.po languages-po/%.po)
	@echo "Update $@"
	@ARGS=""; \
	for file in modules/iso-codes/iso_639-3/$*.po modules/iso-codes/iso_639-2/$*.po languages-po/$*.po ; do \
		if [ -f $$file ] ; then \
			ARGS="$$ARGS -C $$file" ; \
		fi ; \
	done; \
	msgmerge $$ARGS --previous -U $@ $<
	@touch $@

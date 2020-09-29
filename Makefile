all: weblate_language_data/languages.py

weblate_language_data/languages.py: languages.csv aliases.csv extraplurals.csv default_countries.csv $(wildcard modules/iso-codes/data/iso_*.json)
	./scripts/generate-language-data

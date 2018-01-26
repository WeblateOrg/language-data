# language-data

Language definitions used by [Weblate][w] and free to use by others.

## Generic file format

* Semicolon delimited files
* Contains language code, name, number of plurals and plural equation

## languages.csv

* Combined from several sources, plurals should match CLDR when available
* Used by [Weblate][w] for language definitions
* Manually edited

## extraplurals.csv

* Additional plural variants for some languages
* Usually used in Gettext
* Manually edited

## cldr.csv

* Based purely on the CLDR data
* Generated using export-cldr from https://github.com/mlocati/cldr-to-gettext-plural-rules

## gettext.csv

* Based on Gettext defaults
* Generated using export-gettext

## translate.csv

* Extracted from [translate-toolkit][t]
* Generated using export-translate

## l10n-guide.csv

* Extracted from the [l10n guide][g]
* Generated using export-l10n-guide

## languages-po

* Directory containing PO files with langauge names translations
* Extracted from CLDR data

[w]: https://weblate.org/
[t]: http://toolkit.translatehouse.org/
[g]: http://docs.translatehouse.org/projects/localization-guide/en/latest/

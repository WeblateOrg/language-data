# language-data

Language definitions used by [Weblate][w] and free to use by others.

## Generic file format

* Semicolon delimited file
* Contains language code, name, number of plurals and plural equation

## languages.csv

* Based on Gettext definitions
* Imported from translate-toolkit and Weblate
* Used by [Weblate][w] for language definitions

## extraplurals.csv

* Additional plural variants for some Languages

## cldr.csv

* Based purely on the CLDR data
* Generated using https://github.com/mlocati/cldr-to-gettext-plural-rules

## gettext.csv

* Based on Gettext defaults

## translate.csv

* Extracted from translate-toolkit

## l10n-guide.csv

* Extracted from the l10n guide

## languages-po

* Directory containing PO files with langauge names translations
* Extracted from CLDR data

[w]: https://weblate.org/

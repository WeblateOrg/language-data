# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Language data definitions.

This is an automatically generated file, see scripts/generate-language-data

Do not edit, please adjust language definitions in following repository:
https://github.com/WeblateOrg/language-data
"""
# pylint: disable=line-too-long,too-many-lines


from .utils import gettext_noop as _

# Additional plural rules definitions
EXTRAPLURALS = (
    (
        "br",
        # Translators: Language name for ISO code "br". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Breton"),
        2,
        "n > 1",
    ),
    (
        "cgg",
        # Translators: Language name for ISO code "cgg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chiga"),
        1,
        "0",
    ),
    (
        "cy",
        # Translators: Language name for ISO code "cy". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Welsh"),
        2,
        "(n==2) ? 1 : 0",
    ),
    (
        "cy",
        # Translators: Language name for ISO code "cy". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Welsh"),
        4,
        "(n==1) ? 0 : (n==2) ? 1 : (n != 8 && n != 11) ? 2 : 3",
    ),
    (
        "dsb",
        # Translators: Language name for ISO code "dsb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lower Sorbian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "fil",
        # Translators: Language name for ISO code "fil". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Filipino"),
        2,
        "(n > 1)",
    ),
    (
        "ga",
        # Translators: Language name for ISO code "ga". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Irish"),
        3,
        "n==1 ? 0 : n==2 ? 1 : 2",
    ),
    (
        "he",
        # Translators: Language name for ISO code "he". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hebrew"),
        2,
        "(n != 1)",
    ),
    (
        "he",
        # Translators: Language name for ISO code "he". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hebrew"),
        3,
        "n==1 ? 0 : n==2 ? 2 : 1",
    ),
    (
        "hsb",
        # Translators: Language name for ISO code "hsb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Upper Sorbian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "jv",
        # Translators: Language name for ISO code "jv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Javanese"),
        2,
        "(n != 1)",
    ),
    (
        "ka",
        # Translators: Language name for ISO code "ka". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Georgian"),
        1,
        "0",
    ),
    (
        "kw",
        # Translators: Language name for ISO code "kw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Cornish"),
        3,
        "(n == 1) ? 0 : ((n == 2) ? 1 : 2)",
    ),
    (
        "kw",
        # Translators: Language name for ISO code "kw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Cornish"),
        4,
        "(n==1) ? 0 : (n==2) ? 1 : (n == 3) ? 2 : 3",
    ),
    (
        "lt",
        # Translators: Language name for ISO code "lt". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lithuanian"),
        4,
        "n==1 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : n%10==0 || (n%100>10 && n%100<20) ? 2 : 3",
    ),
    (
        "lt",
        # Translators: Language name for ISO code "lt". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lithuanian"),
        3,
        "(n%10==1 && n%100!=11 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : 2)",
    ),
    (
        "lv",
        # Translators: Language name for ISO code "lv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Latvian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n != 0 ? 1 : 2",
    ),
    (
        "lv",
        # Translators: Language name for ISO code "lv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Latvian"),
        3,
        "(n%10==1 && n%100!=11 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : 2)",
    ),
    (
        "se",
        # Translators: Language name for ISO code "se". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sami (Northern)"),
        2,
        "(n != 1)",
    ),
    (
        "sl",
        # Translators: Language name for ISO code "sl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Slovenian"),
        4,
        "(n%100==1 ? 1 : n%100==2 ? 2 : n%100==3 || n%100==4 ? 3 : 0)",
    ),
    (
        "ro_MD",
        # Translators: Language name for ISO code "ro_MD". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Moldavian"),
        3,
        "(n == 1) ? 0 : ((n == 0 || n != 1 && n % 100 >= 1 && n % 100 <= 19) ? 1 : 2)",
    ),
)

CLDRPLURALS = (
    (
        "ca",
        # Translators: Language name for ISO code "ca". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Catalan"),
        3,
        "(n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
    ),
    (
        "es",
        # Translators: Language name for ISO code "es". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish"),
        3,
        "(n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
    ),
    (
        "es_419",
        # Translators: Language name for ISO code "es_419". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Latin America)"),
        3,
        "(n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
    ),
    (
        "es_MX",
        # Translators: Language name for ISO code "es_MX". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Mexico)"),
        3,
        "(n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
    ),
    (
        "fr",
        # Translators: Language name for ISO code "fr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("French"),
        3,
        "(n == 0 || n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
    ),
    (
        "fr_CA",
        # Translators: Language name for ISO code "fr_CA". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("French (Canada)"),
        3,
        "(n == 0 || n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
    ),
    (
        "fr_CH",
        # Translators: Language name for ISO code "fr_CH". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("French (Switzerland)"),
        3,
        "(n == 0 || n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
    ),
    (
        "he",
        # Translators: Language name for ISO code "he". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hebrew"),
        3,
        "(n == 1) ? 0 : ((n == 2) ? 1 : 2)",
    ),
    (
        "it",
        # Translators: Language name for ISO code "it". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Italian"),
        3,
        "(n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
    ),
    (
        "mt",
        # Translators: Language name for ISO code "mt". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Maltese"),
        5,
        "(n == 1) ? 0 : ((n == 2) ? 1 : ((n == 0 || n % 100 >= 3 && n % 100 <= 10) ? 2 : ((n % 100 >= 11 && n % 100 <= 19) ? 3 : 4)))",
    ),
    (
        "pt",
        # Translators: Language name for ISO code "pt". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Portuguese"),
        3,
        "(n == 0 || n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
    ),
    (
        "pt_BR",
        # Translators: Language name for ISO code "pt_BR". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Portuguese (Brazil)"),
        3,
        "(n == 0 || n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
    ),
    (
        "pt_PT",
        # Translators: Language name for ISO code "pt_PT". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Portuguese (Portugal)"),
        3,
        "(n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
    ),
    (
        "vec",
        # Translators: Language name for ISO code "vec". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Venetian"),
        3,
        "(n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
    ),
)

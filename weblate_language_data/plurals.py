# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""
Language data definitions.

This is an automatically generated file, see scripts/generate-language-data

Do not edit, please adjust language definitions in following repository:
https://github.com/WeblateOrg/language-data
"""
# pylint: disable=line-too-long,too-many-lines

from .utils import gettext_noop as _

# Additional plural rules definitions
EXTRAPLURALS: tuple[tuple[str, str, int, str], ...] = (
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
    (
        "scn",
        # Translators: Language name for ISO code "scn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sicilian"),
        2,
        "n != 1",
    ),
)

CLDRPLURALS: tuple[tuple[str, str, int, str], ...] = (
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
        "(n == 1) ? 0 : ((n != 0 && n % 1000000 == 0) ? 1 : 2)",
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
)

QTPLURALS: tuple[tuple[str, str, int, str], ...] = (
    (
        "aa",
        # Translators: Language name for ISO code "aa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Afar"),
        2,
        "(n != 1)",
    ),
    (
        "ab",
        # Translators: Language name for ISO code "ab". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Abkhazian"),
        2,
        "(n != 1)",
    ),
    (
        "af",
        # Translators: Language name for ISO code "af". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Afrikaans"),
        2,
        "(n != 1)",
    ),
    (
        "am",
        # Translators: Language name for ISO code "am". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Amharic"),
        2,
        "(n != 1)",
    ),
    (
        "ar",
        # Translators: Language name for ISO code "ar". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arabic"),
        6,
        "(n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : (n%100>=3 && n%100<=10) ? 3 : n%100>=11 ? 4 : 5)",
    ),
    (
        "as",
        # Translators: Language name for ISO code "as". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Assamese"),
        2,
        "(n != 1)",
    ),
    (
        "ay",
        # Translators: Language name for ISO code "ay". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Aymara"),
        2,
        "(n != 1)",
    ),
    (
        "az",
        # Translators: Language name for ISO code "az". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Azerbaijani"),
        2,
        "(n != 1)",
    ),
    (
        "ba",
        # Translators: Language name for ISO code "ba". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bashkir"),
        2,
        "(n != 1)",
    ),
    (
        "be",
        # Translators: Language name for ISO code "be". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Belarusian"),
        3,
        "(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)",
    ),
    (
        "bg",
        # Translators: Language name for ISO code "bg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bulgarian"),
        2,
        "(n != 1)",
    ),
    (
        "bi",
        # Translators: Language name for ISO code "bi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bislama"),
        1,
        "0",
    ),
    (
        "bn",
        # Translators: Language name for ISO code "bn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bengali"),
        2,
        "(n != 1)",
    ),
    (
        "bo",
        # Translators: Language name for ISO code "bo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tibetan"),
        1,
        "0",
    ),
    (
        "br",
        # Translators: Language name for ISO code "br". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Breton"),
        2,
        "(n > 1)",
    ),
    (
        "bs",
        # Translators: Language name for ISO code "bs". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bosnian"),
        3,
        "(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)",
    ),
    (
        "ca",
        # Translators: Language name for ISO code "ca". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Catalan"),
        2,
        "(n != 1)",
    ),
    (
        "co",
        # Translators: Language name for ISO code "co". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Corsican"),
        2,
        "(n != 1)",
    ),
    (
        "cs",
        # Translators: Language name for ISO code "cs". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Czech"),
        3,
        "((n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2)",
    ),
    (
        "cy",
        # Translators: Language name for ISO code "cy". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Welsh"),
        5,
        "(n==0 ? 0 : n==1 ? 1 : (n>=2 && n<=5) ? 2 : n==6 ? 3 : 4)",
    ),
    (
        "da",
        # Translators: Language name for ISO code "da". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Danish"),
        2,
        "(n != 1)",
    ),
    (
        "de",
        # Translators: Language name for ISO code "de". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("German"),
        2,
        "(n != 1)",
    ),
    (
        "dv",
        # Translators: Language name for ISO code "dv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dhivehi"),
        3,
        "(n==1 ? 0 : n==2 ? 1 : 2)",
    ),
    (
        "dz",
        # Translators: Language name for ISO code "dz". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dzongkha"),
        1,
        "0",
    ),
    (
        "el",
        # Translators: Language name for ISO code "el". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Greek"),
        2,
        "(n != 1)",
    ),
    (
        "en",
        # Translators: Language name for ISO code "en". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English"),
        2,
        "(n != 1)",
    ),
    (
        "eo",
        # Translators: Language name for ISO code "eo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Esperanto"),
        2,
        "(n != 1)",
    ),
    (
        "es",
        # Translators: Language name for ISO code "es". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish"),
        2,
        "(n != 1)",
    ),
    (
        "et",
        # Translators: Language name for ISO code "et". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Estonian"),
        2,
        "(n != 1)",
    ),
    (
        "eu",
        # Translators: Language name for ISO code "eu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Basque"),
        2,
        "(n != 1)",
    ),
    (
        "fa",
        # Translators: Language name for ISO code "fa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Persian"),
        1,
        "0",
    ),
    (
        "fi",
        # Translators: Language name for ISO code "fi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Finnish"),
        2,
        "(n != 1)",
    ),
    (
        "fil",
        # Translators: Language name for ISO code "fil". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Filipino"),
        3,
        "(n==1 ? 0 : (n%10==4 || n%10==6 || n%10== 9) ? 1 : 2)",
    ),
    (
        "fj",
        # Translators: Language name for ISO code "fj". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Fijian"),
        1,
        "0",
    ),
    (
        "fo",
        # Translators: Language name for ISO code "fo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Faroese"),
        2,
        "(n != 1)",
    ),
    (
        "fr",
        # Translators: Language name for ISO code "fr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("French"),
        2,
        "(n > 1)",
    ),
    (
        "fur",
        # Translators: Language name for ISO code "fur". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Friulian"),
        2,
        "(n != 1)",
    ),
    (
        "fy",
        # Translators: Language name for ISO code "fy". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Frisian"),
        2,
        "(n != 1)",
    ),
    (
        "ga",
        # Translators: Language name for ISO code "ga". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Irish"),
        3,
        "(n==1 ? 0 : n==2 ? 1 : 2)",
    ),
    (
        "gd",
        # Translators: Language name for ISO code "gd". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gaelic"),
        4,
        "(n==1 || n==11) ? 0 : (n==2 || n==12) ? 1 : (n > 2 && n < 20) ? 2 : 3",
    ),
    (
        "gl",
        # Translators: Language name for ISO code "gl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Galician"),
        2,
        "(n != 1)",
    ),
    (
        "gn",
        # Translators: Language name for ISO code "gn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Guarani"),
        1,
        "0",
    ),
    (
        "gu",
        # Translators: Language name for ISO code "gu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gujarati"),
        2,
        "(n != 1)",
    ),
    (
        "gv",
        # Translators: Language name for ISO code "gv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Manx"),
        3,
        "(n==1 ? 0 : n==2 ? 1 : 2)",
    ),
    (
        "ha",
        # Translators: Language name for ISO code "ha". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hausa"),
        2,
        "(n != 1)",
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
        "hi",
        # Translators: Language name for ISO code "hi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hindi"),
        2,
        "(n != 1)",
    ),
    (
        "hr",
        # Translators: Language name for ISO code "hr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Croatian"),
        3,
        "(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)",
    ),
    (
        "hu",
        # Translators: Language name for ISO code "hu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hungarian"),
        1,
        "0",
    ),
    (
        "hy",
        # Translators: Language name for ISO code "hy". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Armenian"),
        2,
        "(n > 1)",
    ),
    (
        "ia",
        # Translators: Language name for ISO code "ia". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Interlingua"),
        2,
        "(n != 1)",
    ),
    (
        "id",
        # Translators: Language name for ISO code "id". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Indonesian"),
        1,
        "0",
    ),
    (
        "ik",
        # Translators: Language name for ISO code "ik". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Inupiaq"),
        3,
        "(n==1 ? 0 : n==2 ? 1 : 2)",
    ),
    (
        "is",
        # Translators: Language name for ISO code "is". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Icelandic"),
        2,
        "(n%10==1 && n%100!=11 ? 0 : 1)",
    ),
    (
        "it",
        # Translators: Language name for ISO code "it". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Italian"),
        2,
        "(n != 1)",
    ),
    (
        "iu",
        # Translators: Language name for ISO code "iu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Inuktitut"),
        3,
        "(n==1 ? 0 : n==2 ? 1 : 2)",
    ),
    (
        "ja",
        # Translators: Language name for ISO code "ja". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Japanese"),
        1,
        "0",
    ),
    (
        "jv",
        # Translators: Language name for ISO code "jv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Javanese"),
        1,
        "0",
    ),
    (
        "ka",
        # Translators: Language name for ISO code "ka". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Georgian"),
        2,
        "(n != 1)",
    ),
    (
        "kk",
        # Translators: Language name for ISO code "kk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kazakh"),
        2,
        "(n != 1)",
    ),
    (
        "kl",
        # Translators: Language name for ISO code "kl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Greenlandic"),
        2,
        "(n != 1)",
    ),
    (
        "km",
        # Translators: Language name for ISO code "km". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Khmer (Central)"),
        2,
        "(n != 1)",
    ),
    (
        "kn",
        # Translators: Language name for ISO code "kn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kannada"),
        2,
        "(n != 1)",
    ),
    (
        "ko",
        # Translators: Language name for ISO code "ko". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Korean"),
        1,
        "0",
    ),
    (
        "ks",
        # Translators: Language name for ISO code "ks". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kashmiri"),
        2,
        "(n != 1)",
    ),
    (
        "ku",
        # Translators: Language name for ISO code "ku". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kurdish"),
        2,
        "(n != 1)",
    ),
    (
        "kw",
        # Translators: Language name for ISO code "kw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Cornish"),
        2,
        "(n != 1)",
    ),
    (
        "ky",
        # Translators: Language name for ISO code "ky". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kyrgyz"),
        2,
        "(n != 1)",
    ),
    (
        "la",
        # Translators: Language name for ISO code "la". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Latin"),
        2,
        "(n != 1)",
    ),
    (
        "lb",
        # Translators: Language name for ISO code "lb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Luxembourgish"),
        2,
        "(n != 1)",
    ),
    (
        "lg",
        # Translators: Language name for ISO code "lg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Luganda"),
        2,
        "(n != 1)",
    ),
    (
        "ln",
        # Translators: Language name for ISO code "ln". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lingala"),
        2,
        "(n != 1)",
    ),
    (
        "lo",
        # Translators: Language name for ISO code "lo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lao"),
        2,
        "(n != 1)",
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
        "(n%10==1 && n%100!=11 ? 0 : n != 0 ? 1 : 2)",
    ),
    (
        "mg",
        # Translators: Language name for ISO code "mg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Malagasy"),
        2,
        "(n != 1)",
    ),
    (
        "mi",
        # Translators: Language name for ISO code "mi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Maori"),
        3,
        "(n==1 ? 0 : n==2 ? 1 : 2)",
    ),
    (
        "mk",
        # Translators: Language name for ISO code "mk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Macedonian"),
        3,
        "(n%100==1 ? 0 : n%100==2 ? 1 : 2)",
    ),
    (
        "ml",
        # Translators: Language name for ISO code "ml". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Malayalam"),
        2,
        "(n != 1)",
    ),
    (
        "mn",
        # Translators: Language name for ISO code "mn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mongolian"),
        2,
        "(n != 1)",
    ),
    (
        "mr",
        # Translators: Language name for ISO code "mr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Marathi"),
        2,
        "(n != 1)",
    ),
    (
        "ms",
        # Translators: Language name for ISO code "ms". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Malay"),
        1,
        "0",
    ),
    (
        "mt",
        # Translators: Language name for ISO code "mt". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Maltese"),
        4,
        "(n==1 ? 0 : (n==0 || (n%100>=1 && n%100<=10)) ? 1 : (n%100>=11 && n%100<=19) ? 2 : 3)",
    ),
    (
        "my",
        # Translators: Language name for ISO code "my". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Burmese"),
        1,
        "0",
    ),
    (
        "na",
        # Translators: Language name for ISO code "na". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nauru"),
        1,
        "0",
    ),
    (
        "nb_NO",
        # Translators: Language name for ISO code "nb_NO". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Norwegian Bokmål"),
        2,
        "(n != 1)",
    ),
    (
        "ne",
        # Translators: Language name for ISO code "ne". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nepali"),
        2,
        "(n != 1)",
    ),
    (
        "nl",
        # Translators: Language name for ISO code "nl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dutch"),
        2,
        "(n != 1)",
    ),
    (
        "nn",
        # Translators: Language name for ISO code "nn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Norwegian Nynorsk"),
        2,
        "(n != 1)",
    ),
    (
        "nso",
        # Translators: Language name for ISO code "nso". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Pedi"),
        2,
        "(n != 1)",
    ),
    (
        "oc",
        # Translators: Language name for ISO code "oc". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Occitan"),
        2,
        "(n != 1)",
    ),
    (
        "om",
        # Translators: Language name for ISO code "om". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Oromo"),
        1,
        "0",
    ),
    (
        "or",
        # Translators: Language name for ISO code "or". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Odia"),
        2,
        "(n != 1)",
    ),
    (
        "pa",
        # Translators: Language name for ISO code "pa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Punjabi"),
        2,
        "(n != 1)",
    ),
    (
        "pl",
        # Translators: Language name for ISO code "pl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Polish"),
        3,
        "(n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)",
    ),
    (
        "ps",
        # Translators: Language name for ISO code "ps". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Pashto"),
        2,
        "(n != 1)",
    ),
    (
        "pt",
        # Translators: Language name for ISO code "pt". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Portuguese"),
        2,
        "(n != 1)",
    ),
    (
        "pt_BR",
        # Translators: Language name for ISO code "pt_BR". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Portuguese (Brazil)"),
        2,
        "(n > 1)",
    ),
    (
        "qu",
        # Translators: Language name for ISO code "qu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Quechua"),
        2,
        "(n != 1)",
    ),
    (
        "rm",
        # Translators: Language name for ISO code "rm". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Romansh"),
        2,
        "(n != 1)",
    ),
    (
        "rn",
        # Translators: Language name for ISO code "rn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Rundi"),
        2,
        "(n != 1)",
    ),
    (
        "ro",
        # Translators: Language name for ISO code "ro". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Romanian"),
        3,
        "(n==1 ? 0 : (n==0 || (n%100 > 0 && n%100 < 20)) ? 1 : 2)",
    ),
    (
        "ru",
        # Translators: Language name for ISO code "ru". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Russian"),
        3,
        "(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)",
    ),
    (
        "rw",
        # Translators: Language name for ISO code "rw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kinyarwanda"),
        2,
        "(n != 1)",
    ),
    (
        "sa",
        # Translators: Language name for ISO code "sa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sanskrit"),
        3,
        "(n==1 ? 0 : n==2 ? 1 : 2)",
    ),
    (
        "sd",
        # Translators: Language name for ISO code "sd". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sindhi"),
        2,
        "(n != 1)",
    ),
    (
        "se",
        # Translators: Language name for ISO code "se". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sami (Northern)"),
        3,
        "(n==1 ? 0 : n==2 ? 1 : 2)",
    ),
    (
        "si",
        # Translators: Language name for ISO code "si". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sinhala"),
        2,
        "(n != 1)",
    ),
    (
        "sk",
        # Translators: Language name for ISO code "sk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Slovak"),
        3,
        "((n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2)",
    ),
    (
        "sl",
        # Translators: Language name for ISO code "sl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Slovenian"),
        4,
        "(n%100==1 ? 0 : n%100==2 ? 1 : n%100==3 || n%100==4 ? 2 : 3)",
    ),
    (
        "sm",
        # Translators: Language name for ISO code "sm". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Samoan"),
        3,
        "(n==1 ? 0 : n==2 ? 1 : 2)",
    ),
    (
        "sn",
        # Translators: Language name for ISO code "sn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Shona"),
        2,
        "(n != 1)",
    ),
    (
        "so",
        # Translators: Language name for ISO code "so". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Somali"),
        2,
        "(n != 1)",
    ),
    (
        "sq",
        # Translators: Language name for ISO code "sq". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Albanian"),
        2,
        "(n != 1)",
    ),
    (
        "sr",
        # Translators: Language name for ISO code "sr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Serbian"),
        3,
        "(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)",
    ),
    (
        "ss",
        # Translators: Language name for ISO code "ss". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Swati"),
        2,
        "(n != 1)",
    ),
    (
        "st",
        # Translators: Language name for ISO code "st". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sotho (Southern)"),
        2,
        "(n != 1)",
    ),
    (
        "su",
        # Translators: Language name for ISO code "su". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sundanese"),
        1,
        "0",
    ),
    (
        "sv",
        # Translators: Language name for ISO code "sv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Swedish"),
        2,
        "(n != 1)",
    ),
    (
        "sw",
        # Translators: Language name for ISO code "sw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Swahili"),
        2,
        "(n != 1)",
    ),
    (
        "ta",
        # Translators: Language name for ISO code "ta". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tamil"),
        2,
        "(n != 1)",
    ),
    (
        "te",
        # Translators: Language name for ISO code "te". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Telugu"),
        2,
        "(n != 1)",
    ),
    (
        "tg",
        # Translators: Language name for ISO code "tg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tajik"),
        2,
        "(n != 1)",
    ),
    (
        "th",
        # Translators: Language name for ISO code "th". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Thai"),
        1,
        "0",
    ),
    (
        "ti",
        # Translators: Language name for ISO code "ti". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tigrinya"),
        2,
        "(n > 1)",
    ),
    (
        "tk",
        # Translators: Language name for ISO code "tk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Turkmen"),
        2,
        "(n != 1)",
    ),
    (
        "tn",
        # Translators: Language name for ISO code "tn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tswana"),
        2,
        "(n != 1)",
    ),
    (
        "to",
        # Translators: Language name for ISO code "to". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tongan"),
        2,
        "(n != 1)",
    ),
    (
        "tr",
        # Translators: Language name for ISO code "tr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Turkish"),
        1,
        "0",
    ),
    (
        "ts",
        # Translators: Language name for ISO code "ts". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tsonga"),
        2,
        "(n != 1)",
    ),
    (
        "tt",
        # Translators: Language name for ISO code "tt". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tatar"),
        1,
        "0",
    ),
    (
        "ug",
        # Translators: Language name for ISO code "ug". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Uyghur"),
        2,
        "(n != 1)",
    ),
    (
        "uk",
        # Translators: Language name for ISO code "uk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ukrainian"),
        3,
        "(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)",
    ),
    (
        "ur",
        # Translators: Language name for ISO code "ur". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Urdu"),
        2,
        "(n != 1)",
    ),
    (
        "uz",
        # Translators: Language name for ISO code "uz". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Uzbek"),
        2,
        "(n != 1)",
    ),
    (
        "vi",
        # Translators: Language name for ISO code "vi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Vietnamese"),
        1,
        "0",
    ),
    (
        "vo",
        # Translators: Language name for ISO code "vo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Volapük"),
        2,
        "(n != 1)",
    ),
    (
        "wa",
        # Translators: Language name for ISO code "wa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Walloon"),
        2,
        "(n > 1)",
    ),
    (
        "wo",
        # Translators: Language name for ISO code "wo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Wolof"),
        2,
        "(n != 1)",
    ),
    (
        "xh",
        # Translators: Language name for ISO code "xh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Xhosa"),
        2,
        "(n != 1)",
    ),
    (
        "yi",
        # Translators: Language name for ISO code "yi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Yiddish"),
        2,
        "(n != 1)",
    ),
    (
        "yo",
        # Translators: Language name for ISO code "yo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Yoruba"),
        1,
        "0",
    ),
    (
        "za",
        # Translators: Language name for ISO code "za". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Zhuang"),
        1,
        "0",
    ),
    (
        "zh_Hans",
        # Translators: Language name for ISO code "zh_Hans". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chinese (Simplified Han script)"),
        1,
        "0",
    ),
    (
        "zh_Hant",
        # Translators: Language name for ISO code "zh_Hant". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chinese (Traditional Han script)"),
        1,
        "0",
    ),
    (
        "zu",
        # Translators: Language name for ISO code "zu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Zulu"),
        2,
        "(n != 1)",
    ),
)

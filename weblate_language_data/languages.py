#
# Copyright © 2012 - 2021 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

"""Language data definitions.

This is an automatically generated file, see scripts/generate-language-data

Do not edit, please adjust language definitions in following repository:
https://github.com/WeblateOrg/language-data
"""
# pylint: disable=line-too-long,too-many-lines


from .utils import gettext_noop as _

# Language definitions
LANGUAGES = (
    (
        "aa",
        # Translators: Language name for ISO code "aa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Afar"),
        2,
        "n != 1",
    ),
    (
        "ab",
        # Translators: Language name for ISO code "ab". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Abkhazian"),
        2,
        "n != 1",
    ),
    (
        "ace",
        # Translators: Language name for ISO code "ace". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Acehnese"),
        1,
        "0",
    ),
    (
        "ach",
        # Translators: Language name for ISO code "ach". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Acholi"),
        2,
        "n > 1",
    ),
    (
        "ada",
        # Translators: Language name for ISO code "ada". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Adangme"),
        2,
        "n != 1",
    ),
    (
        "ady",
        # Translators: Language name for ISO code "ady". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Adyghe"),
        2,
        "n > 1",
    ),
    (
        "ae",
        # Translators: Language name for ISO code "ae". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Avestan"),
        2,
        "n != 1",
    ),
    (
        "af",
        # Translators: Language name for ISO code "af". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Afrikaans"),
        2,
        "n != 1",
    ),
    (
        "afh",
        # Translators: Language name for ISO code "afh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Afrihili"),
        2,
        "n != 1",
    ),
    (
        "aii",
        # Translators: Language name for ISO code "aii". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Assyrian Neo-Aramaic"),
        2,
        "n != 1",
    ),
    (
        "ain",
        # Translators: Language name for ISO code "ain". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ainu (Japan)"),
        2,
        "n != 1",
    ),
    (
        "ak",
        # Translators: Language name for ISO code "ak". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Akan"),
        2,
        "n > 1",
    ),
    (
        "akk",
        # Translators: Language name for ISO code "akk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Akkadian"),
        2,
        "n != 1",
    ),
    (
        "ale",
        # Translators: Language name for ISO code "ale". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Aleut"),
        2,
        "n != 1",
    ),
    (
        "alt",
        # Translators: Language name for ISO code "alt". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Altai (Southern)"),
        2,
        "n != 1",
    ),
    (
        "am",
        # Translators: Language name for ISO code "am". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Amharic"),
        2,
        "n > 1",
    ),
    (
        "an",
        # Translators: Language name for ISO code "an". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Aragonese"),
        2,
        "n != 1",
    ),
    (
        "ang",
        # Translators: Language name for ISO code "ang". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (Old)"),
        2,
        "n != 1",
    ),
    (
        "anp",
        # Translators: Language name for ISO code "anp". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Angika"),
        2,
        "n != 1",
    ),
    (
        "ar",
        # Translators: Language name for ISO code "ar". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arabic"),
        6,
        "n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5",
    ),
    (
        "ar_BH",
        # Translators: Language name for ISO code "ar_BH". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arabic (Bahrain)"),
        6,
        "n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5",
    ),
    (
        "ar_DZ",
        # Translators: Language name for ISO code "ar_DZ". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arabic (Algeria)"),
        6,
        "n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5",
    ),
    (
        "ar_EG",
        # Translators: Language name for ISO code "ar_EG". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arabic (Egypt)"),
        6,
        "n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5",
    ),
    (
        "ar_KW",
        # Translators: Language name for ISO code "ar_KW". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arabic (Kuwait)"),
        6,
        "n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5",
    ),
    (
        "ar_LY",
        # Translators: Language name for ISO code "ar_LY". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arabic (Libya)"),
        6,
        "n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5",
    ),
    (
        "ar_MA",
        # Translators: Language name for ISO code "ar_MA". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arabic (Morocco)"),
        6,
        "n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5",
    ),
    (
        "ar_SA",
        # Translators: Language name for ISO code "ar_SA". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arabic (Saudi Arabia)"),
        6,
        "n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5",
    ),
    (
        "ar_XB",
        # Translators: Language name for ISO code "ar_XB". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arabic (XB pseudolocale)"),
        6,
        "n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5",
    ),
    (
        "ar_YE",
        # Translators: Language name for ISO code "ar_YE". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arabic (Yemen)"),
        6,
        "n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5",
    ),
    (
        "arc",
        # Translators: Language name for ISO code "arc". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Aramaic"),
        2,
        "n != 1",
    ),
    (
        "arn",
        # Translators: Language name for ISO code "arn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mapudungun"),
        2,
        "n > 1",
    ),
    (
        "arp",
        # Translators: Language name for ISO code "arp". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arapaho"),
        2,
        "n != 1",
    ),
    (
        "ars",
        # Translators: Language name for ISO code "ars". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arabic (Najdi)"),
        6,
        "(n == 0) ? 0 : ((n == 1) ? 1 : ((n == 2) ? 2 : ((n % 100 >= 3 && n % 100 <= 10) ? 3 : ((n % 100 >= 11 && n % 100 <= 99) ? 4 : 5))))",
    ),
    (
        "arw",
        # Translators: Language name for ISO code "arw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Arawak"),
        2,
        "n != 1",
    ),
    (
        "as",
        # Translators: Language name for ISO code "as". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Assamese"),
        2,
        "n > 1",
    ),
    (
        "asa",
        # Translators: Language name for ISO code "asa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Asu"),
        2,
        "n != 1",
    ),
    (
        "ast",
        # Translators: Language name for ISO code "ast". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Asturian"),
        2,
        "n != 1",
    ),
    (
        "av",
        # Translators: Language name for ISO code "av". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Avaric"),
        2,
        "n != 1",
    ),
    (
        "awa",
        # Translators: Language name for ISO code "awa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Awadhi"),
        2,
        "n != 1",
    ),
    (
        "ay",
        # Translators: Language name for ISO code "ay". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Aymará"),
        1,
        "0",
    ),
    (
        "ayc",
        # Translators: Language name for ISO code "ayc". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Aymara (Southern)"),
        2,
        "n != 1",
    ),
    (
        "az",
        # Translators: Language name for ISO code "az". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Azerbaijani"),
        2,
        "n != 1",
    ),
    (
        "ba",
        # Translators: Language name for ISO code "ba". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bashkir"),
        2,
        "n != 1",
    ),
    (
        "bal",
        # Translators: Language name for ISO code "bal". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Baluchi"),
        2,
        "n != 1",
    ),
    (
        "ban",
        # Translators: Language name for ISO code "ban". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Balinese"),
        2,
        "n != 1",
    ),
    (
        "bar",
        # Translators: Language name for ISO code "bar". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bavarian"),
        2,
        "n != 1",
    ),
    (
        "bas",
        # Translators: Language name for ISO code "bas". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Basa (Cameroon)"),
        2,
        "n != 1",
    ),
    (
        "be",
        # Translators: Language name for ISO code "be". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Belarusian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "be_Latn",
        # Translators: Language name for ISO code "be_Latn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Belarusian (latin)"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "bej",
        # Translators: Language name for ISO code "bej". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Beja"),
        2,
        "n != 1",
    ),
    (
        "bem",
        # Translators: Language name for ISO code "bem". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bemba"),
        2,
        "n != 1",
    ),
    (
        "ber",
        # Translators: Language name for ISO code "ber". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Berber"),
        2,
        "n != 1",
    ),
    (
        "bez",
        # Translators: Language name for ISO code "bez". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bena"),
        2,
        "n != 1",
    ),
    (
        "bg",
        # Translators: Language name for ISO code "bg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bulgarian"),
        2,
        "n != 1",
    ),
    (
        "bh",
        # Translators: Language name for ISO code "bh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bihari"),
        2,
        "n > 1",
    ),
    (
        "bho",
        # Translators: Language name for ISO code "bho". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bhojpuri"),
        2,
        "n > 1",
    ),
    (
        "bi",
        # Translators: Language name for ISO code "bi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bislama"),
        2,
        "n != 1",
    ),
    (
        "bik",
        # Translators: Language name for ISO code "bik". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bikol"),
        2,
        "n != 1",
    ),
    (
        "bin",
        # Translators: Language name for ISO code "bin". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bini"),
        2,
        "n != 1",
    ),
    (
        "bla",
        # Translators: Language name for ISO code "bla". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Siksika"),
        2,
        "n != 1",
    ),
    (
        "bm",
        # Translators: Language name for ISO code "bm". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bambara"),
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
        "n > 1",
    ),
    (
        "bn_BD",
        # Translators: Language name for ISO code "bn_BD". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bengali (Bangladesh)"),
        2,
        "n != 1",
    ),
    (
        "bn_IN",
        # Translators: Language name for ISO code "bn_IN". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bengali (India)"),
        2,
        "n != 1",
    ),
    (
        "bnt",
        # Translators: Language name for ISO code "bnt". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bantu (Other)"),
        2,
        "n != 1",
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
        5,
        "(n % 10 == 1 && n % 100 != 11 && n % 100 != 71 && n % 100 != 91) ? 0 : ((n % 10 == 2 && n % 100 != 12 && n % 100 != 72 && n % 100 != 92) ? 1 : ((((n % 10 == 3 || n % 10 == 4) || n % 10 == 9) && (n % 100 < 10 || n % 100 > 19) && (n % 100 < 70 || n % 100 > 79) && (n % 100 < 90 || n % 100 > 99)) ? 2 : ((n != 0 && n % 1000000 == 0) ? 3 : 4)))",
    ),
    (
        "bra",
        # Translators: Language name for ISO code "bra". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Braj"),
        2,
        "n != 1",
    ),
    (
        "brx",
        # Translators: Language name for ISO code "brx". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bodo"),
        2,
        "n != 1",
    ),
    (
        "bs",
        # Translators: Language name for ISO code "bs". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bosnian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "bs_Cyrl",
        # Translators: Language name for ISO code "bs_Cyrl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bosnian (cyrillic)"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "bs_Latn",
        # Translators: Language name for ISO code "bs_Latn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bosnian (latin)"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "bua",
        # Translators: Language name for ISO code "bua". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Buriat"),
        2,
        "n != 1",
    ),
    (
        "bug",
        # Translators: Language name for ISO code "bug". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Buginese"),
        2,
        "n != 1",
    ),
    (
        "byn",
        # Translators: Language name for ISO code "byn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Bilen"),
        2,
        "n != 1",
    ),
    (
        "ca",
        # Translators: Language name for ISO code "ca". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Catalan"),
        2,
        "n != 1",
    ),
    (
        "ca@valencia",
        # Translators: Language name for ISO code "ca@valencia". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Valencian"),
        2,
        "n != 1",
    ),
    (
        "cad",
        # Translators: Language name for ISO code "cad". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Caddo"),
        2,
        "n != 1",
    ),
    (
        "cak",
        # Translators: Language name for ISO code "cak". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kaqchikel"),
        2,
        "n != 1",
    ),
    (
        "car",
        # Translators: Language name for ISO code "car". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Galibi Carib"),
        2,
        "n != 1",
    ),
    (
        "ce",
        # Translators: Language name for ISO code "ce". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chechen"),
        2,
        "n != 1",
    ),
    (
        "ceb",
        # Translators: Language name for ISO code "ceb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Cebuano"),
        2,
        "n != 1 && n != 2 && n != 3 && (n % 10 == 4 || n % 10 == 6 || n % 10 == 9)",
    ),
    (
        "cgg",
        # Translators: Language name for ISO code "cgg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chiga"),
        2,
        "n != 1",
    ),
    (
        "ch",
        # Translators: Language name for ISO code "ch". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chamorro"),
        2,
        "n != 1",
    ),
    (
        "chb",
        # Translators: Language name for ISO code "chb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chibcha"),
        2,
        "n != 1",
    ),
    (
        "chg",
        # Translators: Language name for ISO code "chg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chagatai"),
        2,
        "n != 1",
    ),
    (
        "chk",
        # Translators: Language name for ISO code "chk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chuukese"),
        2,
        "n != 1",
    ),
    (
        "chm",
        # Translators: Language name for ISO code "chm". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mari"),
        2,
        "n != 1",
    ),
    (
        "chn",
        # Translators: Language name for ISO code "chn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chinook jargon"),
        2,
        "n != 1",
    ),
    (
        "cho",
        # Translators: Language name for ISO code "cho". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Choctaw"),
        2,
        "n != 1",
    ),
    (
        "chp",
        # Translators: Language name for ISO code "chp". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chipewyan"),
        2,
        "n != 1",
    ),
    (
        "chr",
        # Translators: Language name for ISO code "chr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Cherokee"),
        2,
        "n != 1",
    ),
    (
        "chy",
        # Translators: Language name for ISO code "chy". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Cheyenne"),
        2,
        "n != 1",
    ),
    (
        "ckb",
        # Translators: Language name for ISO code "ckb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kurdish (Central)"),
        2,
        "n != 1",
    ),
    (
        "ckb_IQ",
        # Translators: Language name for ISO code "ckb_IQ". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kurdish (Central, Iraq)"),
        2,
        "n != 1",
    ),
    (
        "ckb_IR",
        # Translators: Language name for ISO code "ckb_IR". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kurdish (Central, Iran)"),
        2,
        "n != 1",
    ),
    (
        "co",
        # Translators: Language name for ISO code "co". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Corsican"),
        2,
        "n != 1",
    ),
    (
        "cop",
        # Translators: Language name for ISO code "cop". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Coptic"),
        2,
        "n != 1",
    ),
    (
        "cpe",
        # Translators: Language name for ISO code "cpe". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Creoles and pidgins (English based)"),
        2,
        "n != 1",
    ),
    (
        "cpf",
        # Translators: Language name for ISO code "cpf". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Creoles and pidgins (French-based)"),
        2,
        "n != 1",
    ),
    (
        "cpp",
        # Translators: Language name for ISO code "cpp". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Creoles and pidgins (Portuguese-based)"),
        3,
        "(n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2",
    ),
    (
        "cr",
        # Translators: Language name for ISO code "cr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Cree"),
        2,
        "n != 1",
    ),
    (
        "crh",
        # Translators: Language name for ISO code "crh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Crimean Tatar"),
        1,
        "0",
    ),
    (
        "crp",
        # Translators: Language name for ISO code "crp". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Creoles and pidgins"),
        2,
        "n != 1",
    ),
    (
        "cs",
        # Translators: Language name for ISO code "cs". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Czech"),
        3,
        "(n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2",
    ),
    (
        "csb",
        # Translators: Language name for ISO code "csb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kashubian"),
        3,
        "n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "cu",
        # Translators: Language name for ISO code "cu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Slavonic (Old Church)"),
        2,
        "n != 1",
    ),
    (
        "cv",
        # Translators: Language name for ISO code "cv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chuvash"),
        2,
        "n != 1",
    ),
    (
        "cy",
        # Translators: Language name for ISO code "cy". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Welsh"),
        6,
        "(n==0) ? 0 : (n==1) ? 1 : (n==2) ? 2 : (n==3) ? 3 :(n==6) ? 4 : 5",
    ),
    (
        "da",
        # Translators: Language name for ISO code "da". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Danish"),
        2,
        "n != 1",
    ),
    (
        "dak",
        # Translators: Language name for ISO code "dak". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dakota"),
        2,
        "n != 1",
    ),
    (
        "dar",
        # Translators: Language name for ISO code "dar". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dargwa"),
        2,
        "n != 1",
    ),
    (
        "de",
        # Translators: Language name for ISO code "de". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("German"),
        2,
        "n != 1",
    ),
    (
        "de@formal",
        # Translators: Language name for ISO code "de@formal". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("German (formal)"),
        2,
        "n != 1",
    ),
    (
        "de@informal",
        # Translators: Language name for ISO code "de@informal". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("German (informal)"),
        2,
        "n != 1",
    ),
    (
        "de_1901",
        # Translators: Language name for ISO code "de_1901". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("German (old spelling)"),
        2,
        "n != 1",
    ),
    (
        "de_AT",
        # Translators: Language name for ISO code "de_AT". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("German (Austria)"),
        2,
        "n != 1",
    ),
    (
        "de_CH",
        # Translators: Language name for ISO code "de_CH". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("German (Switzerland)"),
        2,
        "n != 1",
    ),
    (
        "de_LU",
        # Translators: Language name for ISO code "de_LU". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("German (Luxembourg)"),
        2,
        "n != 1",
    ),
    (
        "del",
        # Translators: Language name for ISO code "del". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Delaware"),
        2,
        "n != 1",
    ),
    (
        "den",
        # Translators: Language name for ISO code "den". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Slave (Athapascan)"),
        2,
        "n != 1",
    ),
    (
        "dgo",
        # Translators: Language name for ISO code "dgo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dogri"),
        2,
        "n != 1",
    ),
    (
        "dgr",
        # Translators: Language name for ISO code "dgr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dogrib"),
        2,
        "n != 1",
    ),
    (
        "din",
        # Translators: Language name for ISO code "din". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dinka"),
        2,
        "n != 1",
    ),
    (
        "doi",
        # Translators: Language name for ISO code "doi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dogri"),
        2,
        "n != 1",
    ),
    (
        "dsb",
        # Translators: Language name for ISO code "dsb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lower Sorbian"),
        4,
        "(n % 100 == 1) ? 0 : ((n % 100 == 2) ? 1 : ((n % 100 == 3 || n % 100 == 4) ? 2 : 3))",
    ),
    (
        "dua",
        # Translators: Language name for ISO code "dua". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Duala"),
        2,
        "n != 1",
    ),
    (
        "dum",
        # Translators: Language name for ISO code "dum". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dutch (Middle)"),
        2,
        "n != 1",
    ),
    (
        "dv",
        # Translators: Language name for ISO code "dv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dhivehi"),
        2,
        "n != 1",
    ),
    (
        "dyu",
        # Translators: Language name for ISO code "dyu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dyula"),
        2,
        "n != 1",
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
        "ee",
        # Translators: Language name for ISO code "ee". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ewe"),
        2,
        "n != 1",
    ),
    (
        "efi",
        # Translators: Language name for ISO code "efi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Efik"),
        2,
        "n != 1",
    ),
    (
        "egy",
        # Translators: Language name for ISO code "egy". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Egyptian (Ancient)"),
        2,
        "n != 1",
    ),
    (
        "eka",
        # Translators: Language name for ISO code "eka". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ekajuk"),
        2,
        "n != 1",
    ),
    (
        "el",
        # Translators: Language name for ISO code "el". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Greek"),
        2,
        "n != 1",
    ),
    (
        "elx",
        # Translators: Language name for ISO code "elx". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Elamite"),
        2,
        "n != 1",
    ),
    (
        "en",
        # Translators: Language name for ISO code "en". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English"),
        2,
        "n != 1",
    ),
    (
        "en_AU",
        # Translators: Language name for ISO code "en_AU". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (Australia)"),
        2,
        "n != 1",
    ),
    (
        "en_CA",
        # Translators: Language name for ISO code "en_CA". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (Canada)"),
        2,
        "n != 1",
    ),
    (
        "en_GB",
        # Translators: Language name for ISO code "en_GB". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (United Kingdom)"),
        2,
        "n != 1",
    ),
    (
        "en_IE",
        # Translators: Language name for ISO code "en_IE". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (Ireland)"),
        2,
        "n != 1",
    ),
    (
        "en_IN",
        # Translators: Language name for ISO code "en_IN". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (India)"),
        2,
        "n != 1",
    ),
    (
        "en_NZ",
        # Translators: Language name for ISO code "en_NZ". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (New Zealand)"),
        2,
        "n != 1",
    ),
    (
        "en_PH",
        # Translators: Language name for ISO code "en_PH". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (Philippines)"),
        2,
        "n != 1",
    ),
    (
        "en_US",
        # Translators: Language name for ISO code "en_US". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (United States)"),
        2,
        "n != 1",
    ),
    (
        "en_XA",
        # Translators: Language name for ISO code "en_XA". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (XA pseudolocale)"),
        2,
        "n != 1",
    ),
    (
        "en_ZA",
        # Translators: Language name for ISO code "en_ZA". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (South Africa)"),
        2,
        "n != 1",
    ),
    (
        "en_devel",
        # Translators: Language name for ISO code "en_devel". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (Developer)"),
        2,
        "n != 1",
    ),
    (
        "enm",
        # Translators: Language name for ISO code "enm". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("English (Middle)"),
        2,
        "n != 1",
    ),
    (
        "eo",
        # Translators: Language name for ISO code "eo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Esperanto"),
        2,
        "n != 1",
    ),
    (
        "es",
        # Translators: Language name for ISO code "es". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish"),
        2,
        "n != 1",
    ),
    (
        "es_419",
        # Translators: Language name for ISO code "es_419". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Latin America)"),
        2,
        "n != 1",
    ),
    (
        "es_AR",
        # Translators: Language name for ISO code "es_AR". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Argentina)"),
        2,
        "n != 1",
    ),
    (
        "es_BO",
        # Translators: Language name for ISO code "es_BO". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Bolivia)"),
        2,
        "n != 1",
    ),
    (
        "es_CL",
        # Translators: Language name for ISO code "es_CL". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Chile)"),
        2,
        "n != 1",
    ),
    (
        "es_CO",
        # Translators: Language name for ISO code "es_CO". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Colombia)"),
        2,
        "n != 1",
    ),
    (
        "es_CR",
        # Translators: Language name for ISO code "es_CR". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Costa Rica)"),
        2,
        "n != 1",
    ),
    (
        "es_DO",
        # Translators: Language name for ISO code "es_DO". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Dominican Republic)"),
        2,
        "n != 1",
    ),
    (
        "es_EC",
        # Translators: Language name for ISO code "es_EC". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Ecuador)"),
        2,
        "n != 1",
    ),
    (
        "es_MX",
        # Translators: Language name for ISO code "es_MX". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Mexico)"),
        2,
        "n != 1",
    ),
    (
        "es_NI",
        # Translators: Language name for ISO code "es_NI". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Nicaragua)"),
        2,
        "n != 1",
    ),
    (
        "es_PA",
        # Translators: Language name for ISO code "es_PA". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Panama)"),
        2,
        "n != 1",
    ),
    (
        "es_PE",
        # Translators: Language name for ISO code "es_PE". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Peru)"),
        2,
        "n != 1",
    ),
    (
        "es_PR",
        # Translators: Language name for ISO code "es_PR". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Puerto Rico)"),
        2,
        "n != 1",
    ),
    (
        "es_SV",
        # Translators: Language name for ISO code "es_SV". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (El Salvador)"),
        2,
        "n != 1",
    ),
    (
        "es_US",
        # Translators: Language name for ISO code "es_US". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (American)"),
        2,
        "n != 1",
    ),
    (
        "es_UY",
        # Translators: Language name for ISO code "es_UY". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Uruguay)"),
        2,
        "n != 1",
    ),
    (
        "es_VE",
        # Translators: Language name for ISO code "es_VE". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Spanish (Venezuela)"),
        2,
        "n != 1",
    ),
    (
        "et",
        # Translators: Language name for ISO code "et". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Estonian"),
        2,
        "n != 1",
    ),
    (
        "eu",
        # Translators: Language name for ISO code "eu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Basque"),
        2,
        "n != 1",
    ),
    (
        "ewo",
        # Translators: Language name for ISO code "ewo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ewondo"),
        2,
        "n != 1",
    ),
    (
        "ext",
        # Translators: Language name for ISO code "ext". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Extremaduran"),
        2,
        "n != 1",
    ),
    (
        "fa",
        # Translators: Language name for ISO code "fa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Persian"),
        2,
        "n > 1",
    ),
    (
        "fa_AF",
        # Translators: Language name for ISO code "fa_AF". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dari"),
        2,
        "n > 1",
    ),
    (
        "fan",
        # Translators: Language name for ISO code "fan". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Fang (Equatorial Guinea)"),
        2,
        "n != 1",
    ),
    (
        "fat",
        # Translators: Language name for ISO code "fat". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Fanti"),
        2,
        "n != 1",
    ),
    (
        "ff",
        # Translators: Language name for ISO code "ff". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Fulah"),
        2,
        "n > 1",
    ),
    (
        "fi",
        # Translators: Language name for ISO code "fi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Finnish"),
        2,
        "n != 1",
    ),
    (
        "fil",
        # Translators: Language name for ISO code "fil". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Filipino"),
        2,
        "n != 1 && n != 2 && n != 3 && (n % 10 == 4 || n % 10 == 6 || n % 10 == 9)",
    ),
    (
        "fj",
        # Translators: Language name for ISO code "fj". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Fijian"),
        2,
        "n != 1",
    ),
    (
        "fo",
        # Translators: Language name for ISO code "fo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Faroese"),
        2,
        "n != 1",
    ),
    (
        "fon",
        # Translators: Language name for ISO code "fon". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Fon"),
        2,
        "n != 1",
    ),
    (
        "fr",
        # Translators: Language name for ISO code "fr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("French"),
        2,
        "n > 1",
    ),
    (
        "fr_AG",
        # Translators: Language name for ISO code "fr_AG". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("French (Antigua and Barbuda)"),
        2,
        "n > 1",
    ),
    (
        "fr_BE",
        # Translators: Language name for ISO code "fr_BE". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("French (Belgium)"),
        2,
        "n > 1",
    ),
    (
        "fr_CA",
        # Translators: Language name for ISO code "fr_CA". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("French (Canada)"),
        2,
        "n > 1",
    ),
    (
        "fr_CH",
        # Translators: Language name for ISO code "fr_CH". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("French (Switzerland)"),
        2,
        "n > 1",
    ),
    (
        "fr_LU",
        # Translators: Language name for ISO code "fr_LU". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("French (Luxembourg)"),
        2,
        "n > 1",
    ),
    (
        "frm",
        # Translators: Language name for ISO code "frm". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("French (Middle)"),
        2,
        "n != 1",
    ),
    (
        "fro",
        # Translators: Language name for ISO code "fro". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("French (Old)"),
        2,
        "n != 1",
    ),
    (
        "frp",
        # Translators: Language name for ISO code "frp". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Franco-Provençal"),
        2,
        "n > 1",
    ),
    (
        "frr",
        # Translators: Language name for ISO code "frr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Frisian (Northern)"),
        2,
        "n != 1",
    ),
    (
        "frs",
        # Translators: Language name for ISO code "frs". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Frisian (Eastern)"),
        2,
        "n != 1",
    ),
    (
        "fur",
        # Translators: Language name for ISO code "fur". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Friulian"),
        2,
        "n != 1",
    ),
    (
        "fy",
        # Translators: Language name for ISO code "fy". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Frisian"),
        2,
        "n != 1",
    ),
    (
        "ga",
        # Translators: Language name for ISO code "ga". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Irish"),
        5,
        "n==1 ? 0 : n==2 ? 1 : (n>2 && n<7) ? 2 :(n>6 && n<11) ? 3 : 4",
    ),
    (
        "gaa",
        # Translators: Language name for ISO code "gaa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ga"),
        2,
        "n != 1",
    ),
    (
        "gay",
        # Translators: Language name for ISO code "gay". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gayo"),
        2,
        "n != 1",
    ),
    (
        "gba",
        # Translators: Language name for ISO code "gba". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gbaya (Central African Republic)"),
        2,
        "n != 1",
    ),
    (
        "gbm",
        # Translators: Language name for ISO code "gbm". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Garhwali"),
        2,
        "n != 1",
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
        "gez",
        # Translators: Language name for ISO code "gez". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ge'ez"),
        2,
        "n != 1",
    ),
    (
        "gil",
        # Translators: Language name for ISO code "gil". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gilbertese"),
        2,
        "n != 1",
    ),
    (
        "gl",
        # Translators: Language name for ISO code "gl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Galician"),
        2,
        "n != 1",
    ),
    (
        "gmh",
        # Translators: Language name for ISO code "gmh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("High German (Middle)"),
        2,
        "n != 1",
    ),
    (
        "gn",
        # Translators: Language name for ISO code "gn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Guarani"),
        2,
        "n != 1",
    ),
    (
        "goh",
        # Translators: Language name for ISO code "goh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("High German (Old)"),
        2,
        "n != 1",
    ),
    (
        "gon",
        # Translators: Language name for ISO code "gon". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gondi"),
        2,
        "n != 1",
    ),
    (
        "gor",
        # Translators: Language name for ISO code "gor". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gorontalo"),
        2,
        "n != 1",
    ),
    (
        "got",
        # Translators: Language name for ISO code "got". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gothic"),
        2,
        "n != 1",
    ),
    (
        "grb",
        # Translators: Language name for ISO code "grb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Grebo"),
        2,
        "n != 1",
    ),
    (
        "grc",
        # Translators: Language name for ISO code "grc". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Greek (Ancient)"),
        3,
        "n==1 ? 0 : n==2 ? 1 : 2",
    ),
    (
        "gsw",
        # Translators: Language name for ISO code "gsw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Alemannic"),
        2,
        "n != 1",
    ),
    (
        "gu",
        # Translators: Language name for ISO code "gu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gujarati"),
        2,
        "n > 1",
    ),
    (
        "gu_IN",
        # Translators: Language name for ISO code "gu_IN". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gujarati (India)"),
        2,
        "n > 1",
    ),
    (
        "gug",
        # Translators: Language name for ISO code "gug". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Guaraní (Paraguayan)"),
        2,
        "n > 1",
    ),
    (
        "gun",
        # Translators: Language name for ISO code "gun". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Guaraní (Mbyá)"),
        2,
        "n > 1",
    ),
    (
        "guw",
        # Translators: Language name for ISO code "guw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gun"),
        2,
        "n > 1",
    ),
    (
        "gv",
        # Translators: Language name for ISO code "gv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Manx"),
        4,
        "(n % 10 == 1) ? 0 : ((n % 10 == 2) ? 1 : ((n % 100 == 0 || n % 100 == 20 || n % 100 == 40 || n % 100 == 60 || n % 100 == 80) ? 2 : 3))",
    ),
    (
        "gwi",
        # Translators: Language name for ISO code "gwi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gwichʼin"),
        2,
        "n != 1",
    ),
    (
        "ha",
        # Translators: Language name for ISO code "ha". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hausa"),
        2,
        "n != 1",
    ),
    (
        "hai",
        # Translators: Language name for ISO code "hai". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Haida"),
        2,
        "n != 1",
    ),
    (
        "haw",
        # Translators: Language name for ISO code "haw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hawaiian"),
        2,
        "n != 1",
    ),
    (
        "he",
        # Translators: Language name for ISO code "he". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hebrew"),
        4,
        "(n == 1) ? 0 : ((n == 2) ? 1 : ((n > 10 && n % 10 == 0) ? 2 : 3))",
    ),
    (
        "he_IL",
        # Translators: Language name for ISO code "he_IL". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hebrew (Israel)"),
        4,
        "(n == 1) ? 0 : ((n == 2) ? 1 : ((n > 10 && n % 10 == 0) ? 2 : 3))",
    ),
    (
        "hi",
        # Translators: Language name for ISO code "hi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hindi"),
        2,
        "n > 1",
    ),
    (
        "hi_Latn",
        # Translators: Language name for ISO code "hi_Latn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hindi (latin)"),
        2,
        "n > 1",
    ),
    (
        "hil",
        # Translators: Language name for ISO code "hil". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hiligaynon"),
        2,
        "n != 1",
    ),
    (
        "hit",
        # Translators: Language name for ISO code "hit". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hittite"),
        2,
        "n != 1",
    ),
    (
        "hmn",
        # Translators: Language name for ISO code "hmn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hmong"),
        2,
        "n != 1",
    ),
    (
        "hne",
        # Translators: Language name for ISO code "hne". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chhattisgarhi"),
        2,
        "n != 1",
    ),
    (
        "ho",
        # Translators: Language name for ISO code "ho". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hiri Motu"),
        2,
        "n != 1",
    ),
    (
        "hr",
        # Translators: Language name for ISO code "hr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Croatian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "hrx",
        # Translators: Language name for ISO code "hrx". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hunsrik"),
        2,
        "n != 1",
    ),
    (
        "hsb",
        # Translators: Language name for ISO code "hsb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Upper Sorbian"),
        4,
        "(n % 100 == 1) ? 0 : ((n % 100 == 2) ? 1 : ((n % 100 == 3 || n % 100 == 4) ? 2 : 3))",
    ),
    (
        "ht",
        # Translators: Language name for ISO code "ht". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Haitian"),
        2,
        "n != 1",
    ),
    (
        "hu",
        # Translators: Language name for ISO code "hu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hungarian"),
        2,
        "n != 1",
    ),
    (
        "hup",
        # Translators: Language name for ISO code "hup". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Hupa"),
        2,
        "n != 1",
    ),
    (
        "hus",
        # Translators: Language name for ISO code "hus". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Huastec"),
        2,
        "n != 1",
    ),
    (
        "hy",
        # Translators: Language name for ISO code "hy". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Armenian"),
        2,
        "n > 1",
    ),
    (
        "hz",
        # Translators: Language name for ISO code "hz". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Herero"),
        2,
        "n != 1",
    ),
    (
        "ia",
        # Translators: Language name for ISO code "ia". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Interlingua"),
        2,
        "n != 1",
    ),
    (
        "iba",
        # Translators: Language name for ISO code "iba". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Iban"),
        2,
        "n != 1",
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
        "ie",
        # Translators: Language name for ISO code "ie". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Occidental"),
        2,
        "n != 1",
    ),
    (
        "ig",
        # Translators: Language name for ISO code "ig". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Igbo"),
        1,
        "0",
    ),
    (
        "ii",
        # Translators: Language name for ISO code "ii". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nuosu"),
        1,
        "0",
    ),
    (
        "ik",
        # Translators: Language name for ISO code "ik". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Inupiaq"),
        2,
        "n != 1",
    ),
    (
        "ilo",
        # Translators: Language name for ISO code "ilo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Iloko"),
        2,
        "n != 1",
    ),
    (
        "inh",
        # Translators: Language name for ISO code "inh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ingush"),
        2,
        "n != 1",
    ),
    (
        "io",
        # Translators: Language name for ISO code "io". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ido"),
        2,
        "n != 1",
    ),
    (
        "is",
        # Translators: Language name for ISO code "is". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Icelandic"),
        2,
        "n % 10 != 1 || n % 100 == 11",
    ),
    (
        "it",
        # Translators: Language name for ISO code "it". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Italian"),
        2,
        "n != 1",
    ),
    (
        "iu",
        # Translators: Language name for ISO code "iu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Inuktitut"),
        3,
        "(n == 1) ? 0 : ((n == 2) ? 1 : 2)",
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
        "ja_KS",
        # Translators: Language name for ISO code "ja_KS". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Japanese (Kansai)"),
        1,
        "0",
    ),
    (
        "jam",
        # Translators: Language name for ISO code "jam". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Jamaican Patois"),
        2,
        "n != 1",
    ),
    (
        "jbo",
        # Translators: Language name for ISO code "jbo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lojban"),
        1,
        "0",
    ),
    (
        "jgo",
        # Translators: Language name for ISO code "jgo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ngomba"),
        2,
        "n != 1",
    ),
    (
        "jmc",
        # Translators: Language name for ISO code "jmc". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Machame"),
        2,
        "n != 1",
    ),
    (
        "jpr",
        # Translators: Language name for ISO code "jpr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Judeo-Persian"),
        2,
        "n != 1",
    ),
    (
        "jrb",
        # Translators: Language name for ISO code "jrb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Judeo-Arabic"),
        2,
        "n != 1",
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
        "n != 1",
    ),
    (
        "kaa",
        # Translators: Language name for ISO code "kaa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kara-Kalpak"),
        2,
        "n != 1",
    ),
    (
        "kab",
        # Translators: Language name for ISO code "kab". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kabyle"),
        2,
        "n > 1",
    ),
    (
        "kac",
        # Translators: Language name for ISO code "kac". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kachin"),
        2,
        "n != 1",
    ),
    (
        "kaj",
        # Translators: Language name for ISO code "kaj". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Jju"),
        2,
        "n != 1",
    ),
    (
        "kam",
        # Translators: Language name for ISO code "kam". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kamba (Kenya)"),
        2,
        "n != 1",
    ),
    (
        "kaw",
        # Translators: Language name for ISO code "kaw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kawi"),
        2,
        "n != 1",
    ),
    (
        "kbd",
        # Translators: Language name for ISO code "kbd". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kabardian"),
        2,
        "n != 1",
    ),
    (
        "kcg",
        # Translators: Language name for ISO code "kcg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tyap"),
        2,
        "n != 1",
    ),
    (
        "kde",
        # Translators: Language name for ISO code "kde". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Makonde"),
        1,
        "0",
    ),
    (
        "kea",
        # Translators: Language name for ISO code "kea". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kabuverdianu"),
        1,
        "0",
    ),
    (
        "kg",
        # Translators: Language name for ISO code "kg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kongo"),
        2,
        "n != 1",
    ),
    (
        "kha",
        # Translators: Language name for ISO code "kha". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Khasi"),
        2,
        "n != 1",
    ),
    (
        "kho",
        # Translators: Language name for ISO code "kho". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Khotanese"),
        2,
        "n != 1",
    ),
    (
        "ki",
        # Translators: Language name for ISO code "ki". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Gikuyu"),
        2,
        "n != 1",
    ),
    (
        "kj",
        # Translators: Language name for ISO code "kj". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kwanyama"),
        2,
        "n != 1",
    ),
    (
        "kk",
        # Translators: Language name for ISO code "kk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kazakh"),
        2,
        "n != 1",
    ),
    (
        "kkj",
        # Translators: Language name for ISO code "kkj". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kako"),
        2,
        "n != 1",
    ),
    (
        "kl",
        # Translators: Language name for ISO code "kl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Greenlandic"),
        2,
        "n != 1",
    ),
    (
        "km",
        # Translators: Language name for ISO code "km". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Khmer (Central)"),
        1,
        "0",
    ),
    (
        "kmb",
        # Translators: Language name for ISO code "kmb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kimbundu"),
        2,
        "n != 1",
    ),
    (
        "kmr",
        # Translators: Language name for ISO code "kmr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kurdish (Northern)"),
        2,
        "n != 1",
    ),
    (
        "kmr_Latn",
        # Translators: Language name for ISO code "kmr_Latn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kurdish (Northern, Latin)"),
        2,
        "n != 1",
    ),
    (
        "kn",
        # Translators: Language name for ISO code "kn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kannada"),
        2,
        "n > 1",
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
        "kok",
        # Translators: Language name for ISO code "kok". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Konkani"),
        2,
        "n != 1",
    ),
    (
        "kos",
        # Translators: Language name for ISO code "kos". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kosraean"),
        1,
        "0",
    ),
    (
        "kpe",
        # Translators: Language name for ISO code "kpe". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kpelle"),
        2,
        "n != 1",
    ),
    (
        "kr",
        # Translators: Language name for ISO code "kr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kanuri"),
        2,
        "n != 1",
    ),
    (
        "krc",
        # Translators: Language name for ISO code "krc". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Karachay-Balkar"),
        2,
        "n != 1",
    ),
    (
        "krl",
        # Translators: Language name for ISO code "krl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Karelian"),
        2,
        "n != 1",
    ),
    (
        "kru",
        # Translators: Language name for ISO code "kru". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kurukh"),
        2,
        "n != 1",
    ),
    (
        "ks",
        # Translators: Language name for ISO code "ks". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kashmiri"),
        2,
        "n != 1",
    ),
    (
        "ksb",
        # Translators: Language name for ISO code "ksb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Shambala"),
        2,
        "n != 1",
    ),
    (
        "ksh",
        # Translators: Language name for ISO code "ksh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Colognian"),
        3,
        "n==0 ? 0 : n==1 ? 1 : 2",
    ),
    (
        "ku",
        # Translators: Language name for ISO code "ku". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kurdish"),
        2,
        "n != 1",
    ),
    (
        "kum",
        # Translators: Language name for ISO code "kum". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kumyk"),
        2,
        "n != 1",
    ),
    (
        "kut",
        # Translators: Language name for ISO code "kut". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kutenai"),
        2,
        "n != 1",
    ),
    (
        "kv",
        # Translators: Language name for ISO code "kv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Komi"),
        2,
        "n != 1",
    ),
    (
        "kw",
        # Translators: Language name for ISO code "kw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Cornish"),
        6,
        "(n == 0) ? 0 : ((n == 1) ? 1 : (((n % 100 == 2 || n % 100 == 22 || n % 100 == 42 || n % 100 == 62 || n % 100 == 82) || n % 1000 == 0 && (n % 100000 >= 1000 && n % 100000 <= 20000 || n % 100000 == 40000 || n % 100000 == 60000 || n % 100000 == 80000) || n != 0 && n % 1000000 == 100000) ? 2 : ((n % 100 == 3 || n % 100 == 23 || n % 100 == 43 || n % 100 == 63 || n % 100 == 83) ? 3 : ((n != 1 && (n % 100 == 1 || n % 100 == 21 || n % 100 == 41 || n % 100 == 61 || n % 100 == 81)) ? 4 : 5))))",
    ),
    (
        "ky",
        # Translators: Language name for ISO code "ky". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kyrgyz"),
        2,
        "n != 1",
    ),
    (
        "la",
        # Translators: Language name for ISO code "la". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Latin"),
        2,
        "n != 1",
    ),
    (
        "lad",
        # Translators: Language name for ISO code "lad". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ladino"),
        2,
        "n != 1",
    ),
    (
        "lag",
        # Translators: Language name for ISO code "lag". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Langi"),
        3,
        "(n == 0) ? 0 : ((n == 1) ? 1 : 2)",
    ),
    (
        "lah",
        # Translators: Language name for ISO code "lah". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lahnda"),
        2,
        "n != 1",
    ),
    (
        "lam",
        # Translators: Language name for ISO code "lam". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lamba"),
        2,
        "n != 1",
    ),
    (
        "lb",
        # Translators: Language name for ISO code "lb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Luxembourgish"),
        2,
        "n != 1",
    ),
    (
        "lez",
        # Translators: Language name for ISO code "lez". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lezghian"),
        2,
        "n != 1",
    ),
    (
        "lg",
        # Translators: Language name for ISO code "lg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Luganda"),
        2,
        "n != 1",
    ),
    (
        "li",
        # Translators: Language name for ISO code "li". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Limburgish"),
        2,
        "n != 1",
    ),
    (
        "lki",
        # Translators: Language name for ISO code "lki". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Laki"),
        2,
        "n != 1",
    ),
    (
        "lkt",
        # Translators: Language name for ISO code "lkt". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lakota"),
        1,
        "0",
    ),
    (
        "ln",
        # Translators: Language name for ISO code "ln". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lingala"),
        2,
        "n > 1",
    ),
    (
        "lo",
        # Translators: Language name for ISO code "lo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lao"),
        1,
        "0",
    ),
    (
        "lol",
        # Translators: Language name for ISO code "lol". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mongo"),
        2,
        "n != 1",
    ),
    (
        "loz",
        # Translators: Language name for ISO code "loz". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lozi"),
        2,
        "n != 1",
    ),
    (
        "lt",
        # Translators: Language name for ISO code "lt". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lithuanian"),
        3,
        "(n % 10 == 1 && (n % 100 < 11 || n % 100 > 19)) ? 0 : ((n % 10 >= 2 && n % 10 <= 9 && (n % 100 < 11 || n % 100 > 19)) ? 1 : 2)",
    ),
    (
        "ltg",
        # Translators: Language name for ISO code "ltg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Latgalian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n != 0 ? 1 : 2",
    ),
    (
        "lu",
        # Translators: Language name for ISO code "lu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Luba-Katanga"),
        2,
        "n != 1",
    ),
    (
        "lua",
        # Translators: Language name for ISO code "lua". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Luba-Lulua"),
        2,
        "n != 1",
    ),
    (
        "lui",
        # Translators: Language name for ISO code "lui". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Luiseno"),
        2,
        "n != 1",
    ),
    (
        "lun",
        # Translators: Language name for ISO code "lun". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lunda"),
        2,
        "n != 1",
    ),
    (
        "luo",
        # Translators: Language name for ISO code "luo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Luo (Kenya and Tanzania)"),
        2,
        "n != 1",
    ),
    (
        "lus",
        # Translators: Language name for ISO code "lus". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Lushai"),
        2,
        "n != 1",
    ),
    (
        "lv",
        # Translators: Language name for ISO code "lv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Latvian"),
        3,
        "(n % 10 == 0 || n % 100 >= 11 && n % 100 <= 19) ? 0 : ((n % 10 == 1 && n % 100 != 11) ? 1 : 2)",
    ),
    (
        "mad",
        # Translators: Language name for ISO code "mad". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Madurese"),
        2,
        "n != 1",
    ),
    (
        "mag",
        # Translators: Language name for ISO code "mag". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Magahi"),
        2,
        "n != 1",
    ),
    (
        "mai",
        # Translators: Language name for ISO code "mai". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Maithili"),
        2,
        "n != 1",
    ),
    (
        "mak",
        # Translators: Language name for ISO code "mak". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Makasar"),
        2,
        "n != 1",
    ),
    (
        "man",
        # Translators: Language name for ISO code "man". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mandingo"),
        2,
        "n != 1",
    ),
    (
        "mas",
        # Translators: Language name for ISO code "mas". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Masai"),
        2,
        "n != 1",
    ),
    (
        "mdf",
        # Translators: Language name for ISO code "mdf". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Moksha"),
        2,
        "n != 1",
    ),
    (
        "mdr",
        # Translators: Language name for ISO code "mdr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mandar"),
        2,
        "n != 1",
    ),
    (
        "me",
        # Translators: Language name for ISO code "me". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Montenegrin"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "men",
        # Translators: Language name for ISO code "men". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mende (Sierra Leone)"),
        2,
        "n != 1",
    ),
    (
        "mfe",
        # Translators: Language name for ISO code "mfe". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Morisyen"),
        2,
        "n > 1",
    ),
    (
        "mg",
        # Translators: Language name for ISO code "mg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Malagasy"),
        2,
        "n > 1",
    ),
    (
        "mga",
        # Translators: Language name for ISO code "mga". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Irish (Middle)"),
        2,
        "n != 1",
    ),
    (
        "mgo",
        # Translators: Language name for ISO code "mgo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Metaʼ"),
        2,
        "n != 1",
    ),
    (
        "mh",
        # Translators: Language name for ISO code "mh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Marshallese"),
        2,
        "n != 1",
    ),
    (
        "mhr",
        # Translators: Language name for ISO code "mhr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Meadow Mari"),
        2,
        "n != 1",
    ),
    (
        "mi",
        # Translators: Language name for ISO code "mi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Maori"),
        2,
        "n > 1",
    ),
    (
        "mia",
        # Translators: Language name for ISO code "mia". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Miami"),
        2,
        "n > 1",
    ),
    (
        "mic",
        # Translators: Language name for ISO code "mic". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mi'kmaq"),
        2,
        "n != 1",
    ),
    (
        "min",
        # Translators: Language name for ISO code "min". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Minangkabau"),
        2,
        "n != 1",
    ),
    (
        "mjw",
        # Translators: Language name for ISO code "mjw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Karbi"),
        2,
        "n != 1",
    ),
    (
        "mk",
        # Translators: Language name for ISO code "mk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Macedonian"),
        2,
        "n==1 || n%10==1 ? 0 : 1",
    ),
    (
        "ml",
        # Translators: Language name for ISO code "ml". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Malayalam"),
        2,
        "n != 1",
    ),
    (
        "mn",
        # Translators: Language name for ISO code "mn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mongolian"),
        2,
        "n != 1",
    ),
    (
        "mnc",
        # Translators: Language name for ISO code "mnc". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Manchu"),
        2,
        "n != 1",
    ),
    (
        "mni",
        # Translators: Language name for ISO code "mni". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Manipuri"),
        2,
        "n != 1",
    ),
    (
        "mnk",
        # Translators: Language name for ISO code "mnk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mandinka"),
        3,
        "n==0 ? 0 : n==1 ? 1 : 2",
    ),
    (
        "moh",
        # Translators: Language name for ISO code "moh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mohawk"),
        2,
        "n != 1",
    ),
    (
        "mos",
        # Translators: Language name for ISO code "mos". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mossi"),
        2,
        "n != 1",
    ),
    (
        "mr",
        # Translators: Language name for ISO code "mr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Marathi"),
        2,
        "n != 1",
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
        "ms_Arab",
        # Translators: Language name for ISO code "ms_Arab". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Malay (Jawi)"),
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
        "n==1 ? 0 : n==0 || ( n%100>1 && n%100<11) ? 1 : (n%100>10 && n%100<20 ) ? 2 : 3",
    ),
    (
        "mus",
        # Translators: Language name for ISO code "mus". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Creek"),
        2,
        "n != 1",
    ),
    (
        "mwl",
        # Translators: Language name for ISO code "mwl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Mirandese"),
        2,
        "n != 1",
    ),
    (
        "mwr",
        # Translators: Language name for ISO code "mwr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Marwari"),
        2,
        "n != 1",
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
        "myv",
        # Translators: Language name for ISO code "myv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Erzya"),
        2,
        "n != 1",
    ),
    (
        "na",
        # Translators: Language name for ISO code "na". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nauru"),
        2,
        "n != 1",
    ),
    (
        "nah",
        # Translators: Language name for ISO code "nah". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nahuatl"),
        2,
        "n != 1",
    ),
    (
        "nan",
        # Translators: Language name for ISO code "nan". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chinese (Min Nan)"),
        2,
        "n != 1",
    ),
    (
        "nap",
        # Translators: Language name for ISO code "nap". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Neapolitan"),
        2,
        "n != 1",
    ),
    (
        "naq",
        # Translators: Language name for ISO code "naq". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nama"),
        3,
        "(n == 1) ? 0 : ((n == 2) ? 1 : 2)",
    ),
    (
        "nb_NO",
        # Translators: Language name for ISO code "nb_NO". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Norwegian Bokmål"),
        2,
        "n != 1",
    ),
    (
        "nd",
        # Translators: Language name for ISO code "nd". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ndebele (Northern)"),
        2,
        "n != 1",
    ),
    (
        "nds",
        # Translators: Language name for ISO code "nds". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("German (Low)"),
        2,
        "n != 1",
    ),
    (
        "ne",
        # Translators: Language name for ISO code "ne". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nepali"),
        2,
        "n != 1",
    ),
    (
        "new",
        # Translators: Language name for ISO code "new". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Newari"),
        2,
        "n != 1",
    ),
    (
        "ng",
        # Translators: Language name for ISO code "ng". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ndonga"),
        2,
        "n != 1",
    ),
    (
        "nia",
        # Translators: Language name for ISO code "nia". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nias"),
        2,
        "n != 1",
    ),
    (
        "niu",
        # Translators: Language name for ISO code "niu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Niuean"),
        2,
        "n != 1",
    ),
    (
        "nl",
        # Translators: Language name for ISO code "nl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dutch"),
        2,
        "n != 1",
    ),
    (
        "nl_BE",
        # Translators: Language name for ISO code "nl_BE". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Dutch (Belgium)"),
        2,
        "n != 1",
    ),
    (
        "nn",
        # Translators: Language name for ISO code "nn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Norwegian Nynorsk"),
        2,
        "n != 1",
    ),
    (
        "nnh",
        # Translators: Language name for ISO code "nnh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ngiemboon"),
        2,
        "n != 1",
    ),
    (
        "nog",
        # Translators: Language name for ISO code "nog". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nogai"),
        2,
        "n != 1",
    ),
    (
        "non",
        # Translators: Language name for ISO code "non". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Norse (Old)"),
        2,
        "n != 1",
    ),
    (
        "nqo",
        # Translators: Language name for ISO code "nqo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("N’Ko"),
        1,
        "0",
    ),
    (
        "nr",
        # Translators: Language name for ISO code "nr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ndebele (Southern)"),
        2,
        "n != 1",
    ),
    (
        "nso",
        # Translators: Language name for ISO code "nso". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Pedi"),
        2,
        "n > 1",
    ),
    (
        "nv",
        # Translators: Language name for ISO code "nv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Navaho"),
        2,
        "n != 1",
    ),
    (
        "nwc",
        # Translators: Language name for ISO code "nwc". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Newari (Classical)"),
        2,
        "n != 1",
    ),
    (
        "ny",
        # Translators: Language name for ISO code "ny". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nyanja"),
        2,
        "n != 1",
    ),
    (
        "nym",
        # Translators: Language name for ISO code "nym". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nyamwezi"),
        2,
        "n != 1",
    ),
    (
        "nyn",
        # Translators: Language name for ISO code "nyn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nyankole"),
        2,
        "n != 1",
    ),
    (
        "nyo",
        # Translators: Language name for ISO code "nyo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nyoro"),
        2,
        "n != 1",
    ),
    (
        "nzi",
        # Translators: Language name for ISO code "nzi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Nzima"),
        2,
        "n != 1",
    ),
    (
        "oc",
        # Translators: Language name for ISO code "oc". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Occitan"),
        2,
        "n > 1",
    ),
    (
        "oj",
        # Translators: Language name for ISO code "oj". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ojibwe"),
        2,
        "n != 1",
    ),
    (
        "om",
        # Translators: Language name for ISO code "om". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Oromo"),
        2,
        "n != 1",
    ),
    (
        "or",
        # Translators: Language name for ISO code "or". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Odia"),
        2,
        "n != 1",
    ),
    (
        "os",
        # Translators: Language name for ISO code "os". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ossetian"),
        2,
        "n != 1",
    ),
    (
        "osa",
        # Translators: Language name for ISO code "osa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Osage"),
        1,
        "0",
    ),
    (
        "ota",
        # Translators: Language name for ISO code "ota". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Turkish (Ottoman)"),
        2,
        "n != 1",
    ),
    (
        "otk",
        # Translators: Language name for ISO code "otk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kokturk"),
        2,
        "n != 1",
    ),
    (
        "pa",
        # Translators: Language name for ISO code "pa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Punjabi"),
        2,
        "n > 1",
    ),
    (
        "pag",
        # Translators: Language name for ISO code "pag". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Pangasinan"),
        2,
        "n != 1",
    ),
    (
        "pal",
        # Translators: Language name for ISO code "pal". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Pahlavi"),
        2,
        "n != 1",
    ),
    (
        "pam",
        # Translators: Language name for ISO code "pam". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Pampanga"),
        2,
        "n != 1",
    ),
    (
        "pap",
        # Translators: Language name for ISO code "pap". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Papiamento"),
        2,
        "n != 1",
    ),
    (
        "pau",
        # Translators: Language name for ISO code "pau". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Palauan"),
        2,
        "n != 1",
    ),
    (
        "peo",
        # Translators: Language name for ISO code "peo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Persian (Old)"),
        2,
        "n != 1",
    ),
    (
        "phn",
        # Translators: Language name for ISO code "phn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Phoenician"),
        2,
        "n != 1",
    ),
    (
        "pi",
        # Translators: Language name for ISO code "pi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Pali"),
        2,
        "n != 1",
    ),
    (
        "pl",
        # Translators: Language name for ISO code "pl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Polish"),
        3,
        "n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "pms",
        # Translators: Language name for ISO code "pms". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Piemontese"),
        2,
        "n != 1",
    ),
    (
        "pon",
        # Translators: Language name for ISO code "pon". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Pohnpeian"),
        2,
        "n != 1",
    ),
    (
        "pr",
        # Translators: Language name for ISO code "pr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Pirate"),
        2,
        "n != 1",
    ),
    (
        "prg",
        # Translators: Language name for ISO code "prg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Prussian"),
        3,
        "(n % 10 == 0 || n % 100 >= 11 && n % 100 <= 19) ? 0 : ((n % 10 == 1 && n % 100 != 11) ? 1 : 2)",
    ),
    (
        "pro",
        # Translators: Language name for ISO code "pro". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Provençal (Old)"),
        2,
        "n != 1",
    ),
    (
        "ps",
        # Translators: Language name for ISO code "ps". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Pashto"),
        2,
        "n != 1",
    ),
    (
        "pt",
        # Translators: Language name for ISO code "pt". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Portuguese"),
        2,
        "n > 1",
    ),
    (
        "pt_AO",
        # Translators: Language name for ISO code "pt_AO". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Portuguese (Angola)"),
        2,
        "n > 1",
    ),
    (
        "pt_BR",
        # Translators: Language name for ISO code "pt_BR". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Portuguese (Brazil)"),
        2,
        "n > 1",
    ),
    (
        "pt_PT",
        # Translators: Language name for ISO code "pt_PT". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Portuguese (Portugal)"),
        2,
        "n > 1",
    ),
    (
        "qu",
        # Translators: Language name for ISO code "qu". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Quechua"),
        2,
        "n != 1",
    ),
    (
        "quc",
        # Translators: Language name for ISO code "quc". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("K'iche'"),
        2,
        "n != 1",
    ),
    (
        "raj",
        # Translators: Language name for ISO code "raj". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Rajasthani"),
        2,
        "n != 1",
    ),
    (
        "rap",
        # Translators: Language name for ISO code "rap". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Rapanui"),
        2,
        "n != 1",
    ),
    (
        "rar",
        # Translators: Language name for ISO code "rar". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Rarotongan"),
        2,
        "n != 1",
    ),
    (
        "rcf",
        # Translators: Language name for ISO code "rcf". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Réunion Creole"),
        2,
        "n != 1",
    ),
    (
        "rm",
        # Translators: Language name for ISO code "rm". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Romansh"),
        2,
        "n != 1",
    ),
    (
        "rn",
        # Translators: Language name for ISO code "rn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Rundi"),
        2,
        "n != 1",
    ),
    (
        "ro",
        # Translators: Language name for ISO code "ro". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Romanian"),
        3,
        "n==1 ? 0 : (n==0 || (n%100 > 0 && n%100 < 20)) ? 1 : 2",
    ),
    (
        "ro_MD",
        # Translators: Language name for ISO code "ro_MD". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Moldavian"),
        3,
        "(n == 1) ? 0 : ((n == 0 || n % 100 >= 2 && n % 100 <= 19) ? 1 : 2)",
    ),
    (
        "rof",
        # Translators: Language name for ISO code "rof". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Rombo"),
        2,
        "n != 1",
    ),
    (
        "rom",
        # Translators: Language name for ISO code "rom". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Romany"),
        2,
        "n != 1",
    ),
    (
        "ru",
        # Translators: Language name for ISO code "ru". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Russian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "ru_UA",
        # Translators: Language name for ISO code "ru_UA". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Russian (Ukraine)"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "rue",
        # Translators: Language name for ISO code "rue". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Rusyn"),
        2,
        "n != 1",
    ),
    (
        "rup",
        # Translators: Language name for ISO code "rup". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Macedo-Romanian"),
        2,
        "n != 1",
    ),
    (
        "rw",
        # Translators: Language name for ISO code "rw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kinyarwanda"),
        2,
        "n != 1",
    ),
    (
        "rwk",
        # Translators: Language name for ISO code "rwk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Rwa"),
        2,
        "n != 1",
    ),
    (
        "sa",
        # Translators: Language name for ISO code "sa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sanskrit"),
        3,
        "n==1 ? 0 : n==2 ? 1 : 2",
    ),
    (
        "sad",
        # Translators: Language name for ISO code "sad". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sandawe"),
        2,
        "n != 1",
    ),
    (
        "sah",
        # Translators: Language name for ISO code "sah". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Yakut"),
        1,
        "0",
    ),
    (
        "sai",
        # Translators: Language name for ISO code "sai". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("South American Indian (Other)"),
        2,
        "n != 1",
    ),
    (
        "sam",
        # Translators: Language name for ISO code "sam". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Samaritan Aramaic"),
        2,
        "n != 1",
    ),
    (
        "saq",
        # Translators: Language name for ISO code "saq". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Samburu"),
        2,
        "n != 1",
    ),
    (
        "sas",
        # Translators: Language name for ISO code "sas". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sasak"),
        2,
        "n != 1",
    ),
    (
        "sat",
        # Translators: Language name for ISO code "sat". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Santali"),
        2,
        "n != 1",
    ),
    (
        "sc",
        # Translators: Language name for ISO code "sc". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sardinian"),
        2,
        "n != 1",
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
    (
        "sco",
        # Translators: Language name for ISO code "sco". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Scots"),
        2,
        "n != 1",
    ),
    (
        "sd",
        # Translators: Language name for ISO code "sd". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sindhi"),
        2,
        "n != 1",
    ),
    (
        "sdh",
        # Translators: Language name for ISO code "sdh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kurdish (Southern)"),
        2,
        "n != 1",
    ),
    (
        "se",
        # Translators: Language name for ISO code "se". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sami (Northern)"),
        3,
        "(n == 1) ? 0 : ((n == 2) ? 1 : 2)",
    ),
    (
        "seh",
        # Translators: Language name for ISO code "seh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sena"),
        2,
        "n != 1",
    ),
    (
        "sel",
        # Translators: Language name for ISO code "sel". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Selkup"),
        2,
        "n != 1",
    ),
    (
        "ses",
        # Translators: Language name for ISO code "ses". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Koyraboro Senni"),
        1,
        "0",
    ),
    (
        "sg",
        # Translators: Language name for ISO code "sg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sango"),
        1,
        "0",
    ),
    (
        "sga",
        # Translators: Language name for ISO code "sga". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Irish (Old)"),
        2,
        "n != 1",
    ),
    (
        "sgn",
        # Translators: Language name for ISO code "sgn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sign Languages"),
        2,
        "n != 1",
    ),
    (
        "shi",
        # Translators: Language name for ISO code "shi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tachelhit"),
        3,
        "(n == 0 || n == 1) ? 0 : ((n >= 2 && n <= 10) ? 1 : 2)",
    ),
    (
        "shn",
        # Translators: Language name for ISO code "shn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Shan"),
        2,
        "n != 1",
    ),
    (
        "si",
        # Translators: Language name for ISO code "si". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sinhala"),
        2,
        "n > 1",
    ),
    (
        "sid",
        # Translators: Language name for ISO code "sid". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sidamo"),
        2,
        "n != 1",
    ),
    (
        "sk",
        # Translators: Language name for ISO code "sk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Slovak"),
        3,
        "(n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2",
    ),
    (
        "sl",
        # Translators: Language name for ISO code "sl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Slovenian"),
        4,
        "n%100==1 ? 0 : n%100==2 ? 1 : n%100==3 || n%100==4 ? 2 : 3",
    ),
    (
        "sm",
        # Translators: Language name for ISO code "sm". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Samoan"),
        2,
        "n != 1",
    ),
    (
        "sma",
        # Translators: Language name for ISO code "sma". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sami (Southern)"),
        3,
        "(n == 1) ? 0 : ((n == 2) ? 1 : 2)",
    ),
    (
        "smi",
        # Translators: Language name for ISO code "smi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sami"),
        3,
        "(n == 1) ? 0 : ((n == 2) ? 1 : 2)",
    ),
    (
        "smj",
        # Translators: Language name for ISO code "smj". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sami (Lule)"),
        3,
        "(n == 1) ? 0 : ((n == 2) ? 1 : 2)",
    ),
    (
        "sml",
        # Translators: Language name for ISO code "sml". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sama (Central)"),
        2,
        "n != 1",
    ),
    (
        "smn",
        # Translators: Language name for ISO code "smn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sami (Inari)"),
        3,
        "(n == 1) ? 0 : ((n == 2) ? 1 : 2)",
    ),
    (
        "sms",
        # Translators: Language name for ISO code "sms". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sami (Skolt)"),
        3,
        "(n == 1) ? 0 : ((n == 2) ? 1 : 2)",
    ),
    (
        "sn",
        # Translators: Language name for ISO code "sn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Shona"),
        2,
        "n != 1",
    ),
    (
        "snk",
        # Translators: Language name for ISO code "snk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Soninke"),
        2,
        "n != 1",
    ),
    (
        "so",
        # Translators: Language name for ISO code "so". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Somali"),
        2,
        "n != 1",
    ),
    (
        "sog",
        # Translators: Language name for ISO code "sog". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sogdian"),
        2,
        "n != 1",
    ),
    (
        "son",
        # Translators: Language name for ISO code "son". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Songhai"),
        1,
        "0",
    ),
    (
        "sq",
        # Translators: Language name for ISO code "sq". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Albanian"),
        2,
        "n != 1",
    ),
    (
        "sr",
        # Translators: Language name for ISO code "sr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Serbian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "sr@ijekavian",
        # Translators: Language name for ISO code "sr@ijekavian". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ijekavian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "sr@ijekavian_Latn",
        # Translators: Language name for ISO code "sr@ijekavian_Latn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ijekavian (latin)"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "sr_Cyrl",
        # Translators: Language name for ISO code "sr_Cyrl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Serbian (cyrillic)"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "sr_Latn",
        # Translators: Language name for ISO code "sr_Latn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Serbian (latin)"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "srn",
        # Translators: Language name for ISO code "srn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sranan Tongo"),
        2,
        "n != 1",
    ),
    (
        "srr",
        # Translators: Language name for ISO code "srr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Serer"),
        2,
        "n != 1",
    ),
    (
        "ss",
        # Translators: Language name for ISO code "ss". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Swati"),
        2,
        "n != 1",
    ),
    (
        "ssy",
        # Translators: Language name for ISO code "ssy". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Saho"),
        2,
        "n != 1",
    ),
    (
        "st",
        # Translators: Language name for ISO code "st". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sotho (Southern)"),
        2,
        "n != 1",
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
        "suk",
        # Translators: Language name for ISO code "suk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sukuma"),
        2,
        "n != 1",
    ),
    (
        "sus",
        # Translators: Language name for ISO code "sus". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Susu"),
        2,
        "n != 1",
    ),
    (
        "sux",
        # Translators: Language name for ISO code "sux". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sumerian"),
        2,
        "n != 1",
    ),
    (
        "sv",
        # Translators: Language name for ISO code "sv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Swedish"),
        2,
        "n != 1",
    ),
    (
        "sw",
        # Translators: Language name for ISO code "sw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Swahili"),
        2,
        "n != 1",
    ),
    (
        "sw_CD",
        # Translators: Language name for ISO code "sw_CD". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Swahili (Congo)"),
        2,
        "n != 1",
    ),
    (
        "sw_TZ",
        # Translators: Language name for ISO code "sw_TZ". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Swahili (Tanzania)"),
        2,
        "n != 1",
    ),
    (
        "syc",
        # Translators: Language name for ISO code "syc". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Syriac (Classical)"),
        2,
        "n != 1",
    ),
    (
        "syr",
        # Translators: Language name for ISO code "syr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Syriac"),
        2,
        "n != 1",
    ),
    (
        "szl",
        # Translators: Language name for ISO code "szl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Silesian"),
        3,
        "n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "ta",
        # Translators: Language name for ISO code "ta". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tamil"),
        2,
        "n != 1",
    ),
    (
        "ta_LK",
        # Translators: Language name for ISO code "ta_LK". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tamil (Sri Lanka)"),
        2,
        "n != 1",
    ),
    (
        "te",
        # Translators: Language name for ISO code "te". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Telugu"),
        2,
        "n != 1",
    ),
    (
        "tem",
        # Translators: Language name for ISO code "tem". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Timne"),
        2,
        "n != 1",
    ),
    (
        "teo",
        # Translators: Language name for ISO code "teo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Teso"),
        2,
        "n != 1",
    ),
    (
        "ter",
        # Translators: Language name for ISO code "ter". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tereno"),
        2,
        "n != 1",
    ),
    (
        "tet",
        # Translators: Language name for ISO code "tet". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tetum"),
        2,
        "n != 1",
    ),
    (
        "tg",
        # Translators: Language name for ISO code "tg". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tajik"),
        1,
        "0",
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
        "n > 1",
    ),
    (
        "tig",
        # Translators: Language name for ISO code "tig". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tigre"),
        2,
        "n != 1",
    ),
    (
        "tiv",
        # Translators: Language name for ISO code "tiv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tiv"),
        2,
        "n != 1",
    ),
    (
        "tk",
        # Translators: Language name for ISO code "tk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Turkmen"),
        2,
        "n != 1",
    ),
    (
        "tkl",
        # Translators: Language name for ISO code "tkl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tokelau"),
        2,
        "n != 1",
    ),
    (
        "tl",
        # Translators: Language name for ISO code "tl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tagalog"),
        2,
        "n != 1 && n != 2 && n != 3 && (n % 10 == 4 || n % 10 == 6 || n % 10 == 9)",
    ),
    (
        "tlh-qaak",
        # Translators: Language name for ISO code "tlh-qaak". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Klingon (pIqaD)"),
        1,
        "0",
    ),
    (
        "tlh",
        # Translators: Language name for ISO code "tlh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Klingon"),
        1,
        "0",
    ),
    (
        "tli",
        # Translators: Language name for ISO code "tli". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tlingit"),
        2,
        "n != 1",
    ),
    (
        "tmh",
        # Translators: Language name for ISO code "tmh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tamashek"),
        2,
        "n != 1",
    ),
    (
        "tn",
        # Translators: Language name for ISO code "tn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tswana"),
        2,
        "n != 1",
    ),
    (
        "to",
        # Translators: Language name for ISO code "to". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tongan"),
        1,
        "0",
    ),
    (
        "tog",
        # Translators: Language name for ISO code "tog". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tonga (Nyasa)"),
        2,
        "n != 1",
    ),
    (
        "tpi",
        # Translators: Language name for ISO code "tpi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tok Pisin"),
        2,
        "n != 1",
    ),
    (
        "tr",
        # Translators: Language name for ISO code "tr". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Turkish"),
        2,
        "n != 1",
    ),
    (
        "trv",
        # Translators: Language name for ISO code "trv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Taroko"),
        2,
        "n != 1",
    ),
    (
        "ts",
        # Translators: Language name for ISO code "ts". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tsonga"),
        2,
        "n != 1",
    ),
    (
        "tsi",
        # Translators: Language name for ISO code "tsi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tsimshian"),
        2,
        "n != 1",
    ),
    (
        "tsj",
        # Translators: Language name for ISO code "tsj". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tshangla"),
        2,
        "n != 1",
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
        "tt@iqtelif",
        # Translators: Language name for ISO code "tt@iqtelif". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tatar (IQTElif)"),
        1,
        "0",
    ),
    (
        "tum",
        # Translators: Language name for ISO code "tum". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tumbuka"),
        2,
        "n != 1",
    ),
    (
        "tvl",
        # Translators: Language name for ISO code "tvl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tuvalu"),
        2,
        "n != 1",
    ),
    (
        "tw",
        # Translators: Language name for ISO code "tw". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Twi"),
        2,
        "n != 1",
    ),
    (
        "ty",
        # Translators: Language name for ISO code "ty". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tahitian"),
        2,
        "n != 1",
    ),
    (
        "tyv",
        # Translators: Language name for ISO code "tyv". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tuvinian"),
        2,
        "n != 1",
    ),
    (
        "tzj",
        # Translators: Language name for ISO code "tzj". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tz'utujil"),
        2,
        "n != 1",
    ),
    (
        "tzm",
        # Translators: Language name for ISO code "tzm". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tamazight (Central Atlas)"),
        2,
        "n >= 2 && (n < 11 || n > 99)",
    ),
    (
        "udm",
        # Translators: Language name for ISO code "udm". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Udmurt"),
        2,
        "n != 1",
    ),
    (
        "ug",
        # Translators: Language name for ISO code "ug". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Uyghur"),
        2,
        "n != 1",
    ),
    (
        "uga",
        # Translators: Language name for ISO code "uga". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ugaritic"),
        2,
        "n != 1",
    ),
    (
        "uk",
        # Translators: Language name for ISO code "uk". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Ukrainian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "umb",
        # Translators: Language name for ISO code "umb". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Umbundu"),
        2,
        "n != 1",
    ),
    (
        "und",
        # Translators: Language name for ISO code "und". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Undetermined"),
        2,
        "n != 1",
    ),
    (
        "ur",
        # Translators: Language name for ISO code "ur". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Urdu"),
        2,
        "n != 1",
    ),
    (
        "ur_IN",
        # Translators: Language name for ISO code "ur_IN". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Urdu (India)"),
        2,
        "n != 1",
    ),
    (
        "ur_PK",
        # Translators: Language name for ISO code "ur_PK". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Urdu (Pakistan)"),
        2,
        "n != 1",
    ),
    (
        "uz",
        # Translators: Language name for ISO code "uz". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Uzbek"),
        2,
        "n != 1",
    ),
    (
        "uz_Latn",
        # Translators: Language name for ISO code "uz_Latn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Uzbek (latin)"),
        2,
        "n != 1",
    ),
    (
        "vai",
        # Translators: Language name for ISO code "vai". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Vai"),
        2,
        "n != 1",
    ),
    (
        "ve",
        # Translators: Language name for ISO code "ve". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Venda"),
        2,
        "n != 1",
    ),
    (
        "vec",
        # Translators: Language name for ISO code "vec". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Venetian"),
        2,
        "n != 1",
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
        "vls",
        # Translators: Language name for ISO code "vls". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Flemish (West)"),
        2,
        "n != 1",
    ),
    (
        "vo",
        # Translators: Language name for ISO code "vo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Volapük"),
        2,
        "n != 1",
    ),
    (
        "vot",
        # Translators: Language name for ISO code "vot". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Votic"),
        2,
        "n != 1",
    ),
    (
        "vun",
        # Translators: Language name for ISO code "vun". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Vunjo"),
        2,
        "n != 1",
    ),
    (
        "wa",
        # Translators: Language name for ISO code "wa". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Walloon"),
        2,
        "n > 1",
    ),
    (
        "wae",
        # Translators: Language name for ISO code "wae". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("German (Walser)"),
        2,
        "n != 1",
    ),
    (
        "wal",
        # Translators: Language name for ISO code "wal". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Wolaytta"),
        2,
        "n != 1",
    ),
    (
        "war",
        # Translators: Language name for ISO code "war". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Waray (Philippines)"),
        2,
        "n != 1",
    ),
    (
        "was",
        # Translators: Language name for ISO code "was". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Washo"),
        2,
        "n != 1",
    ),
    (
        "wen",
        # Translators: Language name for ISO code "wen". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Sorbian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "wo",
        # Translators: Language name for ISO code "wo". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Wolof"),
        1,
        "0",
    ),
    (
        "xal",
        # Translators: Language name for ISO code "xal". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Kalmyk"),
        2,
        "n != 1",
    ),
    (
        "xh",
        # Translators: Language name for ISO code "xh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Xhosa"),
        2,
        "n != 1",
    ),
    (
        "xog",
        # Translators: Language name for ISO code "xog". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Soga"),
        2,
        "n != 1",
    ),
    (
        "yao",
        # Translators: Language name for ISO code "yao". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Yao"),
        2,
        "n != 1",
    ),
    (
        "yap",
        # Translators: Language name for ISO code "yap". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Yapese"),
        2,
        "n != 1",
    ),
    (
        "yi",
        # Translators: Language name for ISO code "yi". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Yiddish"),
        2,
        "n != 1",
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
        "yue",
        # Translators: Language name for ISO code "yue". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Yue"),
        1,
        "0",
    ),
    (
        "za",
        # Translators: Language name for ISO code "za". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Zhuang"),
        2,
        "n != 1",
    ),
    (
        "zap",
        # Translators: Language name for ISO code "zap". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Zapotec"),
        2,
        "n != 1",
    ),
    (
        "zbl",
        # Translators: Language name for ISO code "zbl". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Blissymbols"),
        2,
        "n != 1",
    ),
    (
        "zen",
        # Translators: Language name for ISO code "zen". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Zenaga"),
        2,
        "n != 1",
    ),
    (
        "zgh",
        # Translators: Language name for ISO code "zgh". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Tamazight (Standard Moroccan)"),
        2,
        "n != 1",
    ),
    (
        "zh_Hans",
        # Translators: Language name for ISO code "zh_Hans". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chinese (Simplified)"),
        1,
        "0",
    ),
    (
        "zh_Hans_SG",
        # Translators: Language name for ISO code "zh_Hans_SG". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chinese (Simplified, Singapore)"),
        1,
        "0",
    ),
    (
        "zh_Hant",
        # Translators: Language name for ISO code "zh_Hant". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chinese (Traditional)"),
        1,
        "0",
    ),
    (
        "zh_Hant_HK",
        # Translators: Language name for ISO code "zh_Hant_HK". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chinese (Traditional, Hong Kong)"),
        1,
        "0",
    ),
    (
        "zh_Latn",
        # Translators: Language name for ISO code "zh_Latn". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Chinese (Pinyin)"),
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
        "n > 1",
    ),
    (
        "zun",
        # Translators: Language name for ISO code "zun". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Zuni"),
        2,
        "n != 1",
    ),
    (
        "zza",
        # Translators: Language name for ISO code "zza". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("Zaza"),
        2,
        "n != 1",
    ),
)

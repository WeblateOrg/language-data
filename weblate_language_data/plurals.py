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
        _("Northern Sami"),
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

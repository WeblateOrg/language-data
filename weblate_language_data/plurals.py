#
# Copyright © 2012 - 2020 Michal Čihař <michal@cihar.com>
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
        # Translators: Language name, ISO code: br
        _("Breton"),
        2,
        "n > 1",
    ),
    (
        "cgg",
        # Translators: Language name, ISO code: cgg
        _("Chiga"),
        1,
        "0",
    ),
    (
        "cy",
        # Translators: Language name, ISO code: cy
        _("Welsh"),
        2,
        "(n==2) ? 1 : 0",
    ),
    (
        "cy",
        # Translators: Language name, ISO code: cy
        _("Welsh"),
        4,
        "(n==1) ? 0 : (n==2) ? 1 : (n != 8 && n != 11) ? 2 : 3",
    ),
    (
        "dsb",
        # Translators: Language name, ISO code: dsb
        _("Lower Sorbian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "fil",
        # Translators: Language name, ISO code: fil
        _("Filipino"),
        2,
        "(n > 1)",
    ),
    (
        "ga",
        # Translators: Language name, ISO code: ga
        _("Irish"),
        3,
        "n==1 ? 0 : n==2 ? 1 : 2",
    ),
    (
        "he",
        # Translators: Language name, ISO code: he
        _("Hebrew"),
        2,
        "(n != 1)",
    ),
    (
        "he",
        # Translators: Language name, ISO code: he
        _("Hebrew"),
        3,
        "n==1 ? 0 : n==2 ? 2 : 1",
    ),
    (
        "hsb",
        # Translators: Language name, ISO code: hsb
        _("Upper Sorbian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2",
    ),
    (
        "jv",
        # Translators: Language name, ISO code: jv
        _("Javanese"),
        2,
        "(n != 1)",
    ),
    (
        "ka",
        # Translators: Language name, ISO code: ka
        _("Georgian"),
        1,
        "0",
    ),
    (
        "kw",
        # Translators: Language name, ISO code: kw
        _("Cornish"),
        3,
        "(n == 1) ? 0 : ((n == 2) ? 1 : 2)",
    ),
    (
        "kw",
        # Translators: Language name, ISO code: kw
        _("Cornish"),
        4,
        "(n==1) ? 0 : (n==2) ? 1 : (n == 3) ? 2 : 3",
    ),
    (
        "lt",
        # Translators: Language name, ISO code: lt
        _("Lithuanian"),
        4,
        "n==1 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : n%10==0 || (n%100>10 && n%100<20) ? 2 : 3",
    ),
    (
        "lt",
        # Translators: Language name, ISO code: lt
        _("Lithuanian"),
        3,
        "(n%10==1 && n%100!=11 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : 2)",
    ),
    (
        "lv",
        # Translators: Language name, ISO code: lv
        _("Latvian"),
        3,
        "n%10==1 && n%100!=11 ? 0 : n != 0 ? 1 : 2",
    ),
    (
        "lv",
        # Translators: Language name, ISO code: lv
        _("Latvian"),
        3,
        "(n%10==1 && n%100!=11 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : 2)",
    ),
    (
        "se",
        # Translators: Language name, ISO code: se
        _("Northern Sami"),
        2,
        "(n != 1)",
    ),
    (
        "sl",
        # Translators: Language name, ISO code: sl
        _("Slovenian"),
        4,
        "(n%100==1 ? 1 : n%100==2 ? 2 : n%100==3 || n%100==4 ? 3 : 0)",
    ),
    (
        "ro_MD",
        # Translators: Language name, ISO code: ro_MD
        _("Moldavian"),
        3,
        "(n == 1) ? 0 : ((n == 0 || n != 1 && n % 100 >= 1 && n % 100 <= 19) ? 1 : 2)",
    ),
)

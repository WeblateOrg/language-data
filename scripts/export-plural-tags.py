#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import csv
import json
import pprint
import subprocess

BASE_FILE = "modules/cldr-json/cldr-json/cldr-core/supplemental/plurals.json"
ALIASES_FILE = "modules/cldr-json/cldr-json/cldr-core/supplemental/aliases.json"

HEADER = '''# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""
Language data definitions.

This is an automatically generated file, see scripts/export-plural-tags.py

Do not edit, please adjust language definitions in following repository:
https://github.com/WeblateOrg/language-data
"""
# pylint: disable=line-too-long,too-many-lines


'''

TAG_MAP = {
    "(n != 1)": ["one", "other"],
    "(n > 1)": ["one", "other"],
    "(n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : (n%100>=3 && n%100<=10) ? 3 : n%100>=11 ? 4 : 5)": [
        "zero",
        "one",
        "two",
        "few",
        "many",
        "other",
    ],
    "(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)": [
        "one",
        "few",
        "many",
    ],
    "0": ["other"],
    "((n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2)": ["one", "few", "many"],
    "(n==0 ? 0 : n==1 ? 1 : (n>=2 && n<=5) ? 2 : n==6 ? 3 : 4)": [
        "zero",
        "one",
        "few",
        "many",
        "other",
    ],
    "(n==1 ? 0 : n==2 ? 1 : 2)": ["one", "two", "other"],
    "(n==1 ? 0 : (n%10==4 || n%10==6 || n%10== 9) ? 1 : 2)": ["zero", "one", "other"],
    "(n==1 || n==11) ? 0 : (n==2 || n==12) ? 1 : (n > 2 && n < 20) ? 2 : 3": [
        "one",
        "two",
        "few",
        "other",
    ],
    "(n%10==1 && n%100!=11 ? 0 : 1)": ["one", "other"],
    "(n%10==1 && n%100!=11 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : 2)": [
        "one",
        "few",
        "many",
    ],
    "(n%10==1 && n%100!=11 ? 0 : n != 0 ? 1 : 2)": ["one", "other", "zero"],
    "(n%100==1 ? 0 : n%100==2 ? 1 : 2)": ["one", "two", "other"],
    "(n==1 ? 0 : (n==0 || (n%100>=1 && n%100<=10)) ? 1 : (n%100>=11 && n%100<=19) ? 2 : 3)": [
        "one",
        "zero",
        "few",
        "other",
    ],
    "(n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2)": [
        "one",
        "few",
        "many",
    ],
    "(n==1 ? 0 : (n==0 || (n%100 > 0 && n%100 < 20)) ? 1 : 2)": ["one", "few", "other"],
    "(n%100==1 ? 0 : n%100==2 ? 1 : n%100==3 || n%100==4 ? 2 : 3)": [
        "one",
        "two",
        "few",
        "other",
    ],
}

result = {}
decimals = {}
decimal_extras = {}

with open(BASE_FILE) as handle:
    data = json.load(handle)

for locale, rules in data["supplemental"]["plurals-type-cardinal"].items():
    result[locale] = [
        name.replace("pluralRule-count-", "")
        for name, rule in rules.items()
        if "@integer" in rule
    ]
    decimals[locale] = [name.replace("pluralRule-count-", "") for name in rules]
    only_decimals = set(decimals[locale]) - set(result[locale])
    if only_decimals:
        decimal_extras[locale] = list(only_decimals)

# Process CLDR
with open(ALIASES_FILE) as handle:
    aliases = json.load(handle)

for code, alias in aliases["supplemental"]["metadata"]["alias"][
    "languageAlias"
].items():
    # Skip aliases with -
    if "-" in code:
        continue
    replacement = alias["_replacement"]
    # Remove variant from replacement
    if replacement not in result and "-" in replacement:
        replacement = replacement.split("-", 1)[0]
    if replacement in result:
        result[code] = result[replacement]

# Read Weblate aliases
with open("aliases.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    ALIASES = [alias for alias in reader if alias[0] != "#"]

for code, alias in ALIASES:
    replacement = alias
    # Remove variant from replacement
    if replacement not in result and "_" in replacement:
        replacement = replacement.split("_", 1)[0]
    if replacement in result:
        if "_" in code and result.get(code.split("_", 1)[0]) == result[replacement]:
            continue
        result[code] = result[replacement]

# Read qt plurals
with open("qt.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    qtplurals = {row[0]: TAG_MAP[row[3]] for row in reader}

# Write plural tags
with open("weblate_language_data/plural_tags.py", "w") as output:
    output.write(HEADER)
    output.write(f"PLURAL_TAGS = {pprint.pformat(result)}\n\n")
    output.write(f"DECIMAL_PLURAL_TAGS = {pprint.pformat(decimals)}\n")
    output.write(f"DECIMAL_EXTRA_TAGS = {pprint.pformat(decimal_extras)}\n")
    output.write(f"QT_PLURAL_TAGS = {pprint.pformat(qtplurals)}\n")

# Apply coding style
subprocess.run(
    ["pre-commit", "run", "--files", "weblate_language_data/plural_tags.py"],
    check=False,
)

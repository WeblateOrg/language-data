#!/usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Helper script to generate Python code with ambiguous."""

import csv
import subprocess
from collections import defaultdict
from io import StringIO
from pprint import pprint
from urllib.request import Request, urlopen

BASE_URL = "https://iso639-3.sil.org/sites/iso639-3/files/downloads/"
URL = f"{BASE_URL}iso-639-3-macrolanguages.tab"

# List of ambiguous codes to include, this is opt-in as we don't want to push
# disambiguation for languages where it doesn't seem to be needed (for example Arabic)
LANGUAGES = {"kur"}

HEADER = '''# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""
Language data definitions.

This is an automatically generated file, see scripts/export-macrolanguages.py

Do not edit, please adjust language definitions in following repository:
https://github.com/WeblateOrg/language-data
"""
# pylint: disable=line-too-long,too-many-lines


'''

request = Request(URL, headers={"User-Agent": "Mozilla/5.0"})

# Read data from URL
with urlopen(request) as handle:
    content = handle.read().decode()

# Parse tsv
reader = csv.reader(StringIO(content), delimiter="\t")
macrolanguages = list(reader)[1:]

# Generate dict
result = defaultdict(list)
for macro, lang, _kind in macrolanguages:
    if macro not in LANGUAGES:
        continue
    result[macro].append(lang)

# Read aliases
with open("aliases.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    ALIASES = dict([alias for alias in reader if alias[0] != "#"])

# Add aliased entries, needs to happen on snapshot of keys as
# we are updating the dict
for macro in list(result.keys()):
    alias = ALIASES.get(macro)
    if alias and len(alias) == 2:  # noqa: PLR2004
        result[ALIASES[macro]] = result[macro]

# Generate output
with open("weblate_language_data/ambiguous.py", "w") as output:
    output.write(HEADER)
    output.write("# List of ambiguous codes based on ISO-639-3 macrolanguages\n")
    output.write("AMBIGUOUS = ")
    pprint(dict(result), output)
    output.write("\n")

# Black format code
subprocess.run(
    ["prek", "run", "--files", "weblate_language_data/ambiguous.py"],
    check=False,
)

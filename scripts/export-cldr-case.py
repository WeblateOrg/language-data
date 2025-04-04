#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import csv
import json

# Read languages
with open("languages.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    LANGUAGE_CODES = {lang[0] for lang in reader}

# Read
with open("case-insensitive.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    CASES = list(reader)
    CASE_INSENSITIVE_CODES = {lang[0] for lang in CASES}

# Load CLDR
with open("modules/cldr-json/cldr-json/cldr-core/scriptMetadata.json") as handle:
    SCRIPTS = json.load(handle)["scriptMetadata"]
with open(
    "modules/cldr-json/cldr-json/cldr-core/supplemental/languageData.json",
) as handle:
    LANGUAGES: dict[str, dict[str, str]] = json.load(handle)["supplemental"][
        "languageData"
    ]

base: str
script: str | None
for code in LANGUAGE_CODES:
    if "_" in code:
        base, script = code.split("_", 1)
    else:
        base = code
        script = None
    if script is None or script not in SCRIPTS:
        if base in LANGUAGES:
            for script in LANGUAGES[base]["_scripts"]:
                if SCRIPTS[script]["hasCase"] != "YES":
                    CASE_INSENSITIVE_CODES.add(base)
    elif SCRIPTS[script]["hasCase"] != "YES":
        CASE_INSENSITIVE_CODES.add(code)

with open("case-insensitive.csv", "w") as handle:
    handle.write("code,\n")
    for code in sorted(CASE_INSENSITIVE_CODES):
        handle.write(f"{code},\n")

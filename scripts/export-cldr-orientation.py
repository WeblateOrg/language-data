#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import csv
import json
from pathlib import Path

RTL_SCRIPTS = [
    "Arab",
    "Hebr",
    "Syrc",
    "Thaa",
    "Nkoo",
    "Adlm",
    "Mand",
    "Samr",
]
# Tfng is not listed as only some languages are RTL
RTL_TAGS = [f"-{script}-" for script in RTL_SCRIPTS]

# Read languages
with open("languages.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    LANGUAGES = list(reader)
    LANGUAGE_CODES = {lang[0] for lang in LANGUAGES}

# Read RTL
with open("rtl.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    RTLS = list(reader)
    RTL_CODES = {lang[0] for lang in RTLS}

# Process layout data
LAYOUTDIR = Path("modules/cldr-json/cldr-json/cldr-misc-full/main/")

for layout_file in LAYOUTDIR.glob("*/layout.json"):
    json_text = layout_file.read_text()
    data = json.loads(json_text)
    for key, value in data["main"].items():
        code = key.replace("-", "_")
        if code not in LANGUAGE_CODES:
            continue
        character_order = value["layout"]["orientation"]["characterOrder"]
        if character_order == "right-to-left":
            RTL_CODES.add(code)
        elif character_order != "left-to-right":
            print(f"Unknown order for {code}: {character_order})")

# Process likely subtags for default scripts
SUBTAGS = Path("modules/cldr-json/cldr-json/cldr-core/supplemental/likelySubtags.json")
json_text = SUBTAGS.read_text()
data = json.loads(json_text)
for code, subtags in data["supplemental"]["likelySubtags"].items():
    if code in LANGUAGE_CODES and any(tag in subtags for tag in RTL_SCRIPTS):
        RTL_CODES.add(code)

with open("rtl.csv", "w") as handle:
    handle.write("code,\n")
    for code in sorted(RTL_CODES):
        handle.write(f"{code},\n")

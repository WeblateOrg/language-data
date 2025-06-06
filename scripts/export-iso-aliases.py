#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import csv
import json

ALIASES = "modules/cldr-json/cldr-json/cldr-core/supplemental/aliases.json"

names = {}

EXCEPTIONS = {
    "zh": "zh_Hans",
    "sh": "sr_Latn",
    "nb": "nb_NO",
    "no": "nb_NO",
}


def parse_csv(name):
    result = {}
    with open(name) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        for data in reader:
            if data[0] == "#":
                continue
            if data[0] in result:
                raise ValueError(f"Duplicate {data[0]} in {name}!")
            result[data[0]] = data
    return result


def add_name(item):
    if "alpha_2" not in item:
        return
    target = item["alpha_2"]
    if target in EXCEPTIONS:
        target = EXCEPTIONS[target]
    if "alpha_3" in item:
        names[item["alpha_3"]] = target
    if "bibliographic" in item:
        names[item["bibliographic"]] = target


with open("modules/iso-codes/data/iso_639-2.json") as handle:
    for item in json.load(handle)["639-2"]:
        add_name(item)

with open("modules/iso-codes/data/iso_639-3.json") as handle:
    for item in json.load(handle)["639-3"]:
        add_name(item)

# Read languages
with open("languages.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    LANGUAGES = list(reader)
    LANGUAGE_CODES = {lang[0] for lang in LANGUAGES}

with open(ALIASES) as handle:
    aliases = json.load(handle)

    for code, alias in aliases["supplemental"]["metadata"]["alias"][
        "languageAlias"
    ].items():
        # Skip aliases with -
        if "-" in code:
            continue
        replacement = alias["_replacement"]
        if code in LANGUAGE_CODES:
            print(f"Existing language {code}: {alias}")
            continue
        if replacement not in LANGUAGE_CODES:
            print(f"Missing target {code}: {alias}")
            continue
        if code in names:
            if names[code] != replacement:
                print(
                    f"Conflicting replacement for {code}: {names[code]} != {replacement} {alias}",
                )
            continue
        names[code] = replacement


aliases = parse_csv("aliases.csv")

lines = []
for name, alias in sorted(names.items()):
    if name not in aliases:
        lines.append(f"{name},{alias}\n")

with open("aliases.csv", "a") as handle:
    handle.writelines(sorted(lines))

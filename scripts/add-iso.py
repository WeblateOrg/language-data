#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import csv
import json
import sys
from operator import itemgetter
from urllib.request import urlopen

names = {}


def convert_name(name: str) -> str:
    if "," in name:
        base, extra = name.split(",", 1)
        return f"{base.strip()} ({extra.strip()})"
    return name


# See https://github.com/WeblateOrg/language-data/issues/103
PLURALDATA = "https://jibecfed.fedorapeople.org/partage/languages-data/{}.json"

with open("modules/iso-codes/data/iso_639-2.json") as handle:
    for item in json.load(handle)["639-2"]:
        for value in ("alpha_2", "alpha_3"):
            if value in item:
                names[item[value]] = convert_name(
                    item.get("inverted_name", item["name"])
                )

with open("modules/iso-codes/data/iso_639-3.json") as handle:
    for item in json.load(handle)["639-3"]:
        for value in ("alpha_2", "alpha_3"):
            if value in item:
                names[item[value]] = convert_name(
                    item.get("inverted_name", item["name"])
                )

lines: list[list[str]]

with open("languages.csv", newline="") as handle:
    reader = csv.reader(handle, delimiter=",")
    header = next(reader)
    lines = list(reader)

for code in sys.argv[1:]:
    plurals = 2
    formula = "n != 1"
    try:
        with urlopen(PLURALDATA.format(code)) as handle:
            data = json.load(handle)
            for plural in data[code]["Plural-Forms"]:
                if not plural or "INTEGER" in plural:
                    continue
                parts = plural.split(";", 1)
                plurals = int(parts[0].split("=")[1].strip())
                if "plural" in parts[1]:
                    formula = parts[1].split("=", 1)[1].strip().rstrip(";")
                else:
                    formula = parts[1]
                if formula.replace(" ", "") == "(n!=1)":
                    formula = "n != 1"
                if formula == "n != 1":
                    continue
                break
    except (OSError, KeyError):
        sys.stderr.write(f"Failed to load data for {code}, using defaults\n")
    lines.append(
        [
            code,
            names[code].split(";")[-1].strip(),
            str(plurals),
            formula,
        ],
    )

with open("languages.csv", "w", newline="") as handle:
    writer = csv.writer(handle, delimiter=",", lineterminator="\n")
    writer.writerow(header)
    writer.writerows(
        sorted(
            lines,
            key=itemgetter(0),  # type: ignore[arg-type]
        )
    )

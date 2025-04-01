#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import csv
import json
import subprocess

IGNORE = {"nb", "no", "zh", "zxx", "lah"}


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


languages = parse_csv("languages.csv")
aliases = parse_csv("aliases.csv")

with open("modules/iso-codes/data/iso_639-2.json") as handle:
    for item in json.load(handle)["639-2"]:
        if "languages" in item["name"]:
            # Language groups
            continue
        if "-" in item["alpha_3"]:
            # Ranges
            continue
        if "alpha_2" in item:
            if item["alpha_2"] not in IGNORE and item["alpha_2"] not in languages:
                subprocess.run(["./scripts/add-iso.py", item["alpha_2"]], check=True)
        elif item["alpha_3"] not in IGNORE and item["alpha_3"] not in languages:
            subprocess.run(["./scripts/add-iso.py", item["alpha_3"]], check=True)

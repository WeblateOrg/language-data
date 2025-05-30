#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import csv
import subprocess

THRESHOLD = 1_000_000

# Read population data
with open("population.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    POPULATION = dict(reader)

# Read languages
with open("languages.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    LANGUAGES = list(reader)
    LANGUAGE_CODES = {lang[0] for lang in LANGUAGES}

# Read aliases
with open("aliases.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    ALIASES = [alias[0] for alias in reader if alias[0] != "#"]


for code, population in POPULATION.items():
    if "_" in code:
        continue
    if int(population) <= THRESHOLD:
        continue
    if code not in LANGUAGE_CODES and code not in ALIASES:
        print(f"Adding {code} ({population})")
        subprocess.run(
            ["./scripts/add-iso.py", code],
            check=False,
        )

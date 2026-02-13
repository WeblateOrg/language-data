#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import json
from collections import defaultdict

MAPPING = {
    "zh": "zh_Hans",
    "pa_Arab": "pa",
}

with open(
    "modules/cldr-json/cldr-json/cldr-core/supplemental/territoryInfo.json",
) as handle:
    languages: dict[str, float] = defaultdict(float)
    for code, territory in json.load(handle)["supplemental"]["territoryInfo"].items():
        population = int(territory["_population"])
        if "languagePopulation" not in territory:
            print(f"Skipping {code}: {territory}")
            continue
        for language_cldr, data in territory["languagePopulation"].items():
            language = MAPPING.get(language_cldr, language_cldr)
            factor = float(data["_populationPercent"]) / 100
            languages[language] += population * factor
            languages[f"{language}_{code}"] += population * factor

with open("population.csv", "w") as handle:
    handle.write("code,population\n")
    for code in sorted(languages):
        handle.write(f"{code},{int(languages[code])}\n")

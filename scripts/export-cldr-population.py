#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import json
from collections import defaultdict
from collections.abc import Generator

MAPPING = {
    "zh": "zh_Hans",
    "pa_Arab": "pa",
}
REGIONS: list[str] = [
    "150",
    "419",
]
REGION_LANGUAGES: set[str] = {"en", "es"}

with open(
    "modules/cldr-json/cldr-json/cldr-core/supplemental/territoryContainment.json",
) as handle:
    CONTAINMENT = json.load(handle)["supplemental"]["territoryContainment"]


def get_region_countries(text: str) -> Generator[str]:
    for code in CONTAINMENT[text]["_contains"]:
        if code.isdigit():
            yield from get_region_countries(code)
        else:
            yield code


REGION_COUNTRIES: dict[str, str] = {}
for code in REGIONS:
    for country in get_region_countries(code):
        REGION_COUNTRIES[country] = code

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
            if code in REGION_COUNTRIES and language in REGION_LANGUAGES:
                languages[f"{language}_{REGION_COUNTRIES[code]}"] += population * factor

with open("population.csv", "w") as handle:
    handle.write("code,population\n")
    for code in sorted(languages):
        handle.write(f"{code},{int(languages[code])}\n")

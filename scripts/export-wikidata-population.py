#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""
Export fallback speaker counts for languages not covered by CLDR territory data.

This is a maintenance helper and is intentionally not part of the default build.
It queries Wikidata and emits rows for base language codes that are missing or
zero in population.csv. The resulting CSV can be reviewed and committed as
population-fallback.csv.
"""

from __future__ import annotations

import csv
import io
import sys
import urllib.parse
import urllib.request
from collections import defaultdict

QUERY = """
SELECT ?item ?code ?tag ?speakers ?date WHERE {
  ?item p:P1098 ?statement .
  ?statement psv:P1098 ?speaker_value .
  ?speaker_value wikibase:quantityAmount ?speakers .
  OPTIONAL { ?statement pq:P585 ?date . }
  OPTIONAL { ?item wdt:P220 ?code . }
  OPTIONAL { ?item wdt:P305 ?tag . }
  FILTER(BOUND(?code) || BOUND(?tag))
}
"""


def load_zero_population_codes() -> list[str]:
    with open("languages.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        languages = [
            row[0] for row in reader if "_" not in row[0] and "@" not in row[0]
        ]

    with open("population.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        populations = dict(reader)

    return [code for code in languages if int(populations.get(code, "0")) == 0]


def fetch_wikidata_rows() -> list[dict[str, str]]:
    params = urllib.parse.urlencode({"query": QUERY})
    request = urllib.request.Request(
        f"https://query.wikidata.org/sparql?{params}",
        headers={
            "Accept": "text/csv",
            "User-Agent": "weblate-language-data population refresh",
        },
    )
    with urllib.request.urlopen(request) as handle:
        return list(csv.DictReader(io.TextIOWrapper(handle, encoding="utf-8")))


def get_best_row(rows: list[dict[str, str]]) -> dict[str, str] | None:
    positive = {
        (row["item"], row["speakers"], row["date"]): row
        for row in rows
        if float(row["speakers"]) > 0
    }.values()
    if not positive:
        return None
    return max(positive, key=lambda row: (row["date"] or "", float(row["speakers"])))


def main() -> None:
    rows_by_code: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    rows_by_tag: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    for row in fetch_wikidata_rows():
        if row["code"]:
            rows_by_code[row["code"]].append(row)
        if row["tag"]:
            rows_by_tag[row["tag"]].append(row)

    writer = csv.writer(sys.stdout)
    writer.writerow(["code", "population", "source", "date", "url"])
    for code in sorted(load_zero_population_codes()):
        best_row = get_best_row(rows_by_code[code] + rows_by_tag[code])
        if best_row is None:
            continue
        writer.writerow(
            [
                code,
                int(float(best_row["speakers"])),
                "wikidata",
                best_row["date"][:10],
                best_row["item"],
            ]
        )


if __name__ == "__main__":
    main()

#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Export translate-toolkit language definitions."""

import csv

from translate.lang.data import languages

output = []
state = 0
for code, data in languages.items():
    output.append(
        {
            "code": code,
            "name": data[0].split(";")[0],
            "nplurals": data[1],
            "formula": data[2],
        },
    )

with open("translate.csv", "w") as handle:
    writer = csv.DictWriter(
        handle,
        fieldnames=["code", "name", "nplurals", "formula"],
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(sorted(output, key=lambda x: x["code"]))

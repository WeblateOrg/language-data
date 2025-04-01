#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Export l10n guide plurals."""

import re

MATCH = re.compile(r"\s*([^,]+),\s*([^,#]+)( \[#f[0-9]*\]_)?,\s*(nplurals.*)\s*")

with open("modules/l10n-guide/docs/l10n/pluralforms.rst") as handle:
    content = handle.read()

output = []
state = 0
for line in content.splitlines():
    if "csv-table" in line:
        state = 1
        continue
    if state == 1:
        matches = MATCH.match(line)
        if matches:
            plural_parts = matches[4].split(";")
            output.append(
                "{},{},{},{}\n".format(
                    matches[1],
                    matches[2],
                    int(plural_parts[0].split("=")[1]),
                    plural_parts[1].split("=", 1)[1].rstrip(";"),
                ),
            )

with open("l10n-guide.csv", "w") as handle:
    handle.write("code,name,nplurals,formula\n")
    handle.writelines(sorted(output))

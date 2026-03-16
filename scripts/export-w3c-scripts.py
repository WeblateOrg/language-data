#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import csv
import re
from urllib.request import urlopen

URL = "https://www.w3.org/International/questions/qa-scripts"
CODE_RE = re.compile(r"\[([a-z]{2,3})\]")

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

# Fetch URL and read RTL languages
with urlopen(URL) as response:
    text = response.read().decode("utf-8")
    W3C_CODES = set(CODE_RE.findall(text))
    RTL_CODES.update(LANGUAGE_CODES & W3C_CODES)


with open("rtl.csv", "w") as handle:
    handle.write("code,\n")
    handle.writelines(f"{code},\n" for code in sorted(RTL_CODES))

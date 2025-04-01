#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""Export CLDR language names into po file."""

import glob
import json
import os
import re
import sys

BASE = "modules/cldr-json/cldr-json/cldr-localenames-full/main/en/languages.json"
HEADER = """# CLDR language names for {0}
# Automatically generated using tools available at
# https://github.com/WeblateOrg/language-data

msgid ""
msgstr ""
"Project-Id-Version: Weblate\\n"
"Language: {0}\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"X-Generator: Weblate\\n"
"""
ROW = """
msgid "{}"
msgstr "{}"
"""


def extract_names(data):
    code, langs = next(iter(data["main"].items()))
    return code, langs["localeDisplayNames"]["languages"]


# Parse language names
with open(BASE) as handle:
    data = json.load(handle)
names = extract_names(data)[1]

# Process all files or only subset?
match = sys.argv[1] if len(sys.argv) > 1 else "*"

# Remove current files, we overwrite them anyway and this ensures
# that no stale files are there
for old in glob.glob(f"languages-po/{match}.po"):
    os.unlink(old)

path = f"modules/cldr-json/cldr-json/cldr-localenames-full/main/{match}/languages.json"

# Process translations
for lang in glob.glob(path):
    if lang == BASE:
        continue

    with open(lang) as handle:
        data = json.load(handle)

    result = {}

    language_code, language_names = extract_names(data)

    for code, name in language_names.items():
        if code == name or code not in names:
            continue
        name_tokens = set(re.findall(r"\w+", name))
        code_tokens = set(code.split("-alt")[0].split("-"))
        if name_tokens & code_tokens:
            continue

        result[names[code]] = name

    with open(f"languages-po/{language_code}.po", "w") as handle:
        handle.write(HEADER.format(language_code))
        for msgid, msgstr in sorted(result.items()):
            handle.write(ROW.format(msgid, msgstr))

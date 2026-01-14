#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import csv
import gettext

IGNOREDCODES = {
    # Obsolete language codes
    "in",
    "iw",
    "jw",
    "ji",
    "no",
    "es_ES",
    "mo",
    "sh",
    "zh_TW",
    "zh_HK",
    "zh_CN",
    # Ignore some variants
    "es_419",
    "ar_001",
}


def fmt_plural(data):
    return f"nplurals={data[2]}; plural={data[3]};".replace("|", "\\|")


def compare_definition(first, second, meta=True):
    if meta and (
        first[0] != second[0] or first[1] != second[1] or first[2] != second[2]
    ):
        return False
    # Convert formulas to functions
    ours = gettext.c2py(first[3])
    theirs = gettext.c2py(second[3])

    # Compare equation results
    # It would be better to compare formulas,
    # but this was easier to implement and the performance
    # is still okay.
    return all(ours(i) == theirs(i) for i in range(-10, 200))


# Read the definitions
def parse_csv(name):
    result = {}
    with open(name) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        for data in reader:
            if data[0] in result:
                print(f"Duplicate {data[0]} in {name}!")
                continue
            result[data[0]] = data
    return result


def show_diff(name, data):
    for code in sorted(set(data) & set(LANGUAGES)):
        if not compare_definition(data[code], LANGUAGES[code]):
            print(f"Definition for {code} differs:")
            print("Languages:", LANGUAGES[code])
            print(name, ":", data[code])
            print()


def show_missing(name, data):
    for code in sorted(set(data) - set(LANGUAGES) - IGNOREDCODES):
        print(f"Definition for {code} missing in languages:")
        print(name, ":", data[code])
        print()


LANGUAGES = parse_csv("languages.csv")
CLDR = parse_csv("cldr.csv")
GETTEXT = parse_csv("gettext.csv")
TRANSLATE = parse_csv("translate.csv")

# List differences
show_diff("CLDR", CLDR)
show_diff("Gettext", GETTEXT)
show_diff("Translate", TRANSLATE)

# List missing ones
show_missing("CLDR", CLDR)
show_missing("Gettext", GETTEXT)
show_missing("Translate", TRANSLATE)

with open("PLURALS_DIFF.md", "w") as handle:
    handle.write(
        """
## Difference in plurals

This table lists differences in plurals between various sources.
The Plurals column lists data in languages.csv which is used in Weblate

Code | Name | Plurals | CLDR plurals | Gettext plurals | Translate toolkit
---- | ---- | --------| ------------ | --------------- | -----------------
""",
    )
    for code in sorted(set(LANGUAGES)):
        handle.write(f"`{code}`")
        handle.write(" | ")
        handle.write(LANGUAGES[code][1])
        handle.write(" | ")
        handle.write(fmt_plural(LANGUAGES[code]))
        handle.write(" | ")
        if code in CLDR:
            if not compare_definition(LANGUAGES[code], CLDR[code], False):
                handle.write(fmt_plural(CLDR[code]))
            else:
                handle.write("✔")
        handle.write(" | ")
        if code in GETTEXT:
            if not compare_definition(LANGUAGES[code], GETTEXT[code], False):
                handle.write(fmt_plural(GETTEXT[code]))
            else:
                handle.write("✔")
        handle.write(" | ")
        if code in TRANSLATE:
            if not compare_definition(LANGUAGES[code], TRANSLATE[code], False):
                handle.write(fmt_plural(TRANSLATE[code]))
            else:
                handle.write("✔")
        handle.write("\n")

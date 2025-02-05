#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import csv
import os
import re

ALIASES = {
    "Chinese": ("Chinese (Simplified Han script)", "Chinese (Traditional Han script)"),
    "WesternFrisian": ("Frisian",),
    "Interlingue": (),  # Ignore, duplicate for Interlingua
    "Khmer": ("Khmer (Central)",),
    "Kirghiz": ("Kyrgyz",),
    "NorthernSotho": ("Pedi",),
    "NorwegianBokmal": ("Norwegian Bokmål",),
    "NorwegianNynorsk": ("Norwegian Nynorsk",),
    "Oriya": ("Odia",),
    "SouthernSotho": ("Sotho (Southern)",),
    "Uigur": ("Uyghur",),
    "Volapuk": ("Volapük",),
    "Divehi": ("Dhivehi",),
    "Inupiak": ("Inupiaq",),
    "NorthernSami": ("Sami (Northern)",),
    "PortugueseBrasil": ("Portuguese (Brazil)",),
    "Ganda": ("Luganda",),
}


def parse_csv(name):
    result = {}
    with open(name) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        for data in reader:
            if data[0] == "#":
                continue
            if data[1] in result:
                raise ValueError(f"Duplicate {data[1]} in {name}!")
            result[data[1]] = data
    return result


DEFINITIONS = parse_csv("languages.csv")

plural_definition = re.compile(
    r'{\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^,]+)\s*,\s*"nplurals=([0-9]+); plural=([^"]+);"\s}',
)

LANGUAGES = {}
PLURALS = {}


def handle_language(parts):
    text = "".join(parts).replace("\n", "")[31:]
    name = text.split("[", 1)[0]
    # Remove duplicate definition
    if name == "frenchStyleLanguages":
        text = text.replace("QLocale::Filipino,", "")
    # Workaround to deal with frenchStyleCountries
    if name == "frenchStyleLanguages":
        text = text.replace("Portuguese", "PortugueseBrasil")
    LANGUAGES[name] = (
        text.split("{")[1]
        .split("}")[0]
        .replace(",", "")
        .replace("EOL", "")
        .replace("QLocale::", "")
        .replace("Language", "")
        .split()
    )


def handle_table(parts):
    text = "".join(parts).replace("\n", "")[50:]
    for match in plural_definition.findall(text):
        PLURALS[match[3]] = int(match[5]), match[6]


in_language = False
in_table = False
parts = []
with open("modules/qttools/src/linguist/shared/numerus.cpp") as handle:
    for line in handle:
        if in_language:
            if not line.strip().startswith("//"):
                parts.append(line)
            if ";" in line:
                handle_language(parts)
                in_language = False
        elif in_table:
            parts.append(line)
            if "};" in line:
                handle_table(parts)
                in_table = False
        elif line.startswith("static const QLocale::Language"):
            parts = [line]
            if ";" in line:
                handle_language(parts)
            else:
                in_language = True
        elif line.startswith("static const NumerusTableEntry numerusTable"):
            parts = [line]
            in_table = True

output = []
processed = set()


def generate(group, name):
    definition = DEFINITIONS[name]
    plural = PLURALS[group]
    if definition[0] in processed:
        raise ValueError(f"Duplicate definition for {definition[0]}")
    output.append(
        (
            definition[0],
            definition[1],
            plural[0],
            plural[1],
        ),
    )
    processed.add(definition[0])


for group, languages in LANGUAGES.items():
    for language in languages:
        if language in ALIASES:
            for aliased in ALIASES[language]:
                generate(group, aliased)
        else:
            generate(group, language)

os.unlink("qt.csv")

with open("qt.csv", "w") as handle:
    handle.write("code,name,nplurals,formula\n")
    for line in sorted(output):
        handle.write("{},{},{},{}\n".format(*line))

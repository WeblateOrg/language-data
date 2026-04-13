#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import csv
import os
from gettext import c2py
from itertools import chain


def parse_csv(name):
    result = {}
    with open(name) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        for data in reader:
            if data[0] == "#":
                continue
            if data[0] in result:
                raise ValueError(f"Duplicate {data[0]} in {name}!")
            result[data[0]] = data
    return result


def normalize_supported_locale(locale):
    return locale.split(".", 1)[0].lower()


def is_supported_locale(locale, languages, aliases, default_countries):
    candidates = [locale]
    normalized = locale

    if "@" in normalized:
        base, modifier = normalized.split("@", 1)
        if modifier == "euro":
            candidates.append(base)
            normalized = base
        else:
            language = base.split("_", 1)[0]
            candidates.extend((f"{language}@{modifier}", base))
            normalized = base

    if "_" in normalized:
        language = normalized.split("_", 1)[0]
        candidates.append(language)
        if normalized in default_countries:
            candidates.append(language)

    return any(
        candidate in languages or candidate in aliases for candidate in candidates
    )


def validate_supported_locales(languages, aliases, default_countries):
    supported_path = "/usr/share/i18n/SUPPORTED"
    if not os.path.exists(supported_path):
        return

    missing = set()

    with open(supported_path) as handle:
        for line in handle:
            if not line.strip():
                continue
            locale = normalize_supported_locale(line.split()[0])
            if locale in {"c", "posix"}:
                continue
            if not is_supported_locale(locale, languages, aliases, default_countries):
                missing.add(locale)

    if missing:
        raise ValueError(
            "Missing locales from /usr/share/i18n/SUPPORTED: "
            + ", ".join(sorted(missing))
        )


languages = parse_csv("languages.csv")
aliases = parse_csv("aliases.csv")
cldr = parse_csv("cldr.csv")
parse_csv("qt.csv")
default_countries = parse_csv("default_countries.csv")

for alias in aliases:
    if not alias.islower():
        raise ValueError(f"Alias {alias} is not lower cased!")

missing = {alias[1] for alias in aliases.values()} - set(languages.keys())
if missing:
    raise ValueError(f"Missing target for aliases: {missing}")

overlap = set(languages.keys()) & set(aliases.keys())
if overlap:
    raise ValueError(f"Overlapping languages and aliases: {overlap}")

missing = set(cldr.keys()) - set(languages.keys())
# Remove aliases (these use lower case)
missing -= {miss for miss in missing if miss.lower() in aliases}
# Remove default countries (these use lower case)
missing -= {miss for miss in missing if miss.lower() in default_countries}
# Remove unwanted languages
missing -= {"ar_001"}
if missing:
    raise ValueError(f"Missing from CLDR: {missing}")

# Validate CLDR plural rules match
exceptions = {"es", "it", "ca"}
matching = set(cldr.keys()) & set(languages.keys())
for match in matching:
    if match.split("_")[0] in exceptions:
        continue
    plural_our = languages[match][3]
    plural_cldr = cldr[match][3]
    if plural_our == "n != 1" and plural_cldr != "n != 1":
        raise ValueError(
            f"Mismatching plural form for {match} between CLDR and languages: {plural_our!r} != {plural_cldr!r}"
        )


# Validate plural count
for code, _name, plural_count, plural_formula in languages.values():
    plural = c2py(plural_formula)
    # Get maximal plural
    calculated = (
        max(
            plural(x)
            for x in chain(range(-10, 200), [1000, 10000, 100000, 1000000, 10000000])
        )
        + 1
    )
    if calculated != int(plural_count):
        raise ValueError(
            f"Mismatching plural count for {code}: {plural_count} != {calculated}",
        )

validate_supported_locales(
    set(languages.keys()), aliases, set(default_countries.keys())
)

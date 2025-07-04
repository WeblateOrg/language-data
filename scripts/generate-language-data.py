#!/usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""
Helper script to generate Python code from language-data repository.

See https://github.com/WeblateOrg/language-data
"""

import csv
import json
import re
from itertools import chain

SPLIT_RE = re.compile(
    r"(?:\&(?:nbsp|rsaquo|lt|gt|amp|ldquo|rdquo|times|quot);|"
    r'[() ,.^`"\'\\/_<>!?;:|{}*^@%#&~=+\r\n✓—-…\[\]0-9-])+',
)

HEADER = '''# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""
Language data definitions.

This is an automatically generated file, see scripts/generate-language-data.py

Do not edit, please adjust language definitions in following repository:
https://github.com/WeblateOrg/language-data
"""
# pylint: disable=line-too-long,too-many-lines

'''

TEMPLATE = """    (
        "{0}",
        # Translators: Language name for ISO code "{0}". The parenthesis clarifies
        # variant of the language. It could contain a region, age (Old, Middle, ...)
        # or other variant.
        _("{1}"),
        {2},
        "{3}",
    ),
"""
TYPE_HINT = "tuple[tuple[str, str, int, str], ...]"


def escape(value: str) -> str:
    """Escape  string for use in template."""
    return value.replace('"', r"\"")


# Read languages
with open("languages.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    LANGUAGES = list(reader)
    LANGUAGE_CODES = {lang[0] for lang in LANGUAGES}
    LANGUAGE_PLURAL_NO = {lang[0]: lang[2] for lang in LANGUAGES}
    LANGUAGE_NAMES = {lang[0]: lang[1] for lang in LANGUAGES}

# Read population data
with open("population.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    POPULATION = dict(reader)


def get_population(code):
    if code in POPULATION:
        return POPULATION[code]
    if "@" in code:
        return get_population(code.split("@")[0])
    if "_" in code:
        language, variant = code.split("_", 1)
        # This can be really wrong, but better than zero
        if variant in (
            "Cyrl",
            "Latn",
            "Hans",
            "Hant",
            "devel",
            "Latn_pehoeji",
            "Latn_tailo",
        ):
            return get_population(language)
    return 0


# Read aliases
with open("aliases.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    ALIASES = [alias for alias in reader if alias[0] != "#"]
    for source, target in ALIASES:
        if not source.islower():
            raise ValueError(f"Source for alias {source};{target} is not lowercase!")
        if target not in LANGUAGE_CODES:
            raise ValueError(f"Target for alias {source};{target} does not exist!")

# Generate list of codes
CODES = {item[0].lower() for item in chain(ALIASES, LANGUAGES)}

# Read country codes
COUNTRIES = set()
with open("modules/iso-codes/data/iso_3166-1.json") as handle:
    for item in json.load(handle)["3166-1"]:
        COUNTRIES.add(item["alpha_2"].lower())
        COUNTRIES.add(item["alpha_3"].lower())

# Read extra plurals
with open("extraplurals.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    EXTRAPLURALS = list(reader)

# Read qt plurals
with open("qt.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    QTPLURALS = list(reader)

# Parse extra CLDR plurals
with open("cldr.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    CLDRPLURALS = []
    for code, _name, number, equation in reader:
        try:
            existing = LANGUAGE_PLURAL_NO[code]
        except KeyError:
            continue
        if existing != number:
            CLDRPLURALS.append([code, LANGUAGE_NAMES[code], number, equation])

# Read default countries
with open("default_countries.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    DEFAULT_COUNTRIES = list(reader)

# Read RTL
with open("rtl.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    RTLS = list(reader)
    RTL_CODES = {lang[0] for lang in RTLS}

# Read case-insensitive
with open("case-insensitive.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    CASES = list(reader)
    CASE_INSENSITIVE_CODES = {lang[0] for lang in CASES}

# Write language definitions
with open("weblate_language_data/languages.py", "w") as output:
    output.write(HEADER)
    output.write("from .utils import gettext_noop as _\n\n")
    output.write("# Language definitions\n")
    output.write(f"LANGUAGES: {TYPE_HINT} = (\n")
    output.writelines(
        TEMPLATE.format(row[0], escape(row[1]), row[2], row[3]) for row in LANGUAGES
    )
    output.write(")\n")
with open("weblate_language_data/population.py", "w") as output:
    output.write(HEADER)
    output.write("# Language definitions\n")
    output.write("POPULATION: dict[str, int] = {\n")
    for row in LANGUAGES:
        code = row[0]
        output.write(f'    "{escape(code)}": {get_population(code)},\n')
    output.write("}\n")
with open("weblate_language_data/plurals.py", "w") as output:
    output.write(HEADER)
    output.write("from .utils import gettext_noop as _\n\n")
    output.write("# Additional plural rules definitions\n")
    output.write(f"EXTRAPLURALS: {TYPE_HINT} = (\n")
    for row in EXTRAPLURALS:
        output.write(TEMPLATE.format(row[0], escape(row[1]), row[2], row[3]))
    output.write(")\n")
    output.write("\n")
    output.write(f"CLDRPLURALS: {TYPE_HINT} = (\n")
    for row in CLDRPLURALS:
        output.write(TEMPLATE.format(row[0], escape(row[1]), row[2], row[3]))
    output.write(")\n")
    output.write("\n")
    output.write(f"QTPLURALS: {TYPE_HINT} = (\n")
    for row in QTPLURALS:
        output.write(TEMPLATE.format(row[0], escape(row[1]), row[2], row[3]))
    output.write(")\n")
with open("weblate_language_data/aliases.py", "w") as output:
    output.write(HEADER)
    output.write("# Language aliases\n")
    output.write("ALIASES: dict[str, str] = {\n")
    for row in ALIASES:
        output.write("""    "{}": "{}",\n""".format(*row))
    output.write("}\n")
with open("weblate_language_data/countries.py", "w") as output:
    output.write(HEADER)
    output.write("# List of default languages, omitting country code should be okay\n")
    output.write("DEFAULT_LANGS: tuple[str, ...] = (\n")
    for row in DEFAULT_COUNTRIES:
        output.write(f'    "{escape(row[0])}",\n')
    output.write(")\n")
with open("weblate_language_data/rtl.py", "w") as output:
    output.write(HEADER)
    output.write("# List of RTL languages\n")
    output.write("RTL_LANGS: set[str] = {\n")
    for code in sorted(RTL_CODES):
        output.write(f'    "{code}",\n')
    output.write("}\n")

with open("weblate_language_data/case_insensitive.py", "w") as output:
    output.write(HEADER)
    output.write("# List of case-insensitive languages\n")
    output.write("CASE_INSENSITIVE_LANGS: set[str] = {\n")
    for code in sorted(CASE_INSENSITIVE_CODES):
        output.write(f'    "{code}",\n')
    output.write("}\n")

# Generate same check exception list
words = set()


def add_word(word):
    words.update(SPLIT_RE.split(word.lower()))


def process_iso(name):
    with open(f"modules/iso-codes/data/iso_{name}.json") as handle:
        for item in json.load(handle)[name]:
            add_word(item["name"])
            if "inverted_name" in item:
                add_word(item["inverted_name"])
            if "common_name" in item:
                add_word(item["common_name"])


# Our languages data
for row in LANGUAGES:
    add_word(row[1])

# iso-codes
process_iso("639-2")
process_iso("639-3")
process_iso("639-5")
process_iso("15924")
process_iso("3166-1")
process_iso("3166-2")
process_iso("3166-3")
process_iso("4217")

words.difference_update(
    {
        "administered",
        "administrative",
        "air",
        "and",
        "are",
        "association",
        "autonomous",
        "auxiliary",
        "based",
        "bassin",
        "bath",
        "bay",
        "big",
        "canal",
        "canton",
        "country",
        "county",
        "early",
        "east",
        "eastern",
        "family",
        "language",
        "languages",
        "long",
        "metropolitan",
        "miscellaneous",
        "neutral",
        "new",
        "north",
        "northeast",
        "northeastern",
        "northern",
        "northwest",
        "northwestern",
        "region",
        "see",
        "small",
        "south",
        "southeast",
        "southeastern",
        "southern",
        "southwest",
        "southwestern",
        "state",
        "states",
        "testing",
        "transactions",
        "trust",
        "use",
        "west",
        "western",
    },
)

# Write same check exclude list
with open("weblate_language_data/check_languages.py", "w") as output:
    output.write(HEADER)
    output.write("# Language names to ignore in the same check\n")
    output.write("LANGUAGES: set[str] = {\n")
    for word in sorted(words):
        if len(word) <= 2:  # noqa: PLR2004
            continue
        output.write(f'    "{escape(word)}",\n')
    output.write("}\n")


# Write language codes
with open("weblate_language_data/language_codes.py", "w") as output:
    output.write(HEADER)
    output.write("# Known language codes\n")
    output.write("LANGUAGES: set[str] = {\n")
    for word in sorted(CODES):
        output.write('    "{}",\n'.format(word.replace('"', '\\"')))
    output.write("}\n")

# Write country codes
with open("weblate_language_data/country_codes.py", "w") as output:
    output.write(HEADER)
    output.write("# Known country codes\n")
    output.write("COUNTRIES: set[str] = {\n")
    for word in sorted(COUNTRIES):
        output.write('    "{}",\n'.format(word.replace('"', '\\"')))
    output.write("}\n")

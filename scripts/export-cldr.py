#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import csv
import json
import re
from typing import Literal, TypedDict

MAPPINGS = {
    "ar_001": "ar",
    "es_419": "es",
}

SIMPLIFICATIONS = {
    "n >= 0 && n <= 2 && n != 2": "n == 0 || n == 1",
    "n != 0 && n != 1": "n > 1",
    "(n == 0 || n == 1) && n != 0": "n == 1",
}

with open("languages.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    ALL_LANGUAGE_CODES = {lang[0]: lang for lang in reader}


def map_code(code: str) -> str:
    return code.replace("-", "_")


def reduce_formula(formula: str) -> str:
    return SIMPLIFICATIONS.get(formula, formula)


def expand_chunk(what: str, op: str, value: str) -> str:
    if re.match(r"^\d+$", value):
        return f"{what} {op} {value}"
    if match := re.match(r"^(\d+)\.\.(\d+)$", value):
        start = int(match.group(1))
        end = int(match.group(2))
        if (end - start) == 1:
            if op == "==":
                return f"({what} == {start} || {what} == {end})"
            return f"{what} != {start} && {what} == {end}"
        if op == "==":
            return f"{what} >= {start} && {what} <= {end}"
        if what == "n" and start <= 0:
            return f"{what} > {end}"
        return f"({what} < {start} || {what} > {end})"
    raise ValueError(f"Unhandled range '{value}'")


def expand_atom(atom: str) -> str:
    if match := re.match(r"^(n(?: % \d+)?) (==|!=) (\d+(?:\.\.\d+|,\d+)+)$", atom):
        what = match.group(1)
        op = match.group(2)
        if op not in ("==", "!="):
            raise ValueError(f"Unsupported operator {op} in {atom}")
        chunks = []
        for value in match.group(3).split(","):
            chunks.append(expand_chunk(what, op, value))

        if len(chunks) == 1:
            return chunks[0]

        if op == "==":
            return f"({' || '.join(chunks)})"
        return " && ".join(chunks)
    raise ValueError(f"Unable to expand '{atom}'")


def convert_atom(atom: str) -> str | bool:
    result = atom.replace(" = ", " == ").replace("i", "n")

    if re.match(r"^n( % \d+)? (!=|==) \d+$", result):
        return result

    if re.match(r"^n( % \d+)? (!=|==) \d+(,\d+|\.\.\d+)+$", result):
        return expand_atom(result)

    if match := re.match(r"^(?:v|w)(?: % 10+)? == (\d+)(?:\.\.\d+)?$", result):
        # For gettext: v == 0, w == 0
        return int(match.group(1)) == 0
    if match := re.match(r"^(?:v|w)(?: % 10+)? != (\d+)(?:\.\.\d+)?$", result):
        # For gettext: v == 0, w == 0
        return int(match.group(1)) != 0
    if match := re.match(r"^(?:f|t|c|e)(?: % 10+)? == (\d+)(?:\.\.\d+)?$", result):
        # For gettext: f == empty, t == empty, c == empty, e == empty
        return int(match.group(1)) == 0
    if match := re.match(r"^(?:f|t|c|e)(?: % 10+)? != (\d+)(?:\.\.\d+)?$", result):
        # For gettext: f == empty, t == empty, c == empty, e == empty
        return int(match.group(1)) != 0
    raise ValueError(
        f"Unable to convert the formula chunk '{atom}' from CLDR to gettext",
    )


def convert_formula(cldr_formula_and_examples: str) -> str | bool:
    # Skip formulas which do not trigger integer
    if "@integer" not in cldr_formula_and_examples:
        return False

    # Normalize whitespace
    cldr_formula_and_examples = " ".join(cldr_formula_and_examples.split())

    # Extract formula from examples
    if not (
        match := re.match(
            "^([^@]*)(?:@integer([^@]+))?(?:@decimal(?:[^@]+))?$",
            cldr_formula_and_examples,
        )
    ):
        raise ValueError(f"Invalid CLDR category rule: {cldr_formula_and_examples}")
    cldr_formula = match.group(1).strip()

    # Sanity checkign
    if "(" in cldr_formula or ")" in cldr_formula:
        raise ValueError(
            f"Unable to convert the formula '{cldr_formula}': parenthesis handling not implemented",
        )

    # Blank formula for other
    if not cldr_formula:
        return True

    chunks = []

    for chunk in cldr_formula.split(" or "):
        output = None
        and_chunks = []
        for atom in chunk.split(" and "):
            gettext = convert_atom(atom)
            if gettext is False:
                # One atom joined by 'and' always evaluates to false => the whole 'and' group is always false
                output = False
                break
            if gettext is not True:
                and_chunks.append(gettext)

        if output is not False:
            if not and_chunks:
                # All the atoms joined by 'and' always evaluate to true => the whole 'and' group is always true
                # One part of the formula joined with the others by 'or' always evaluates to true => the whole formula always evaluates to true
                return True

            chunks.append(reduce_formula(" && ".join(and_chunks)))

    if not chunks:
        # All the parts joined by 'or' always evaluate to false => the whole formula always evaluates to false
        return False

    return " || ".join(chunks)


def reverse_formula(formula: str | bool) -> str:
    if isinstance(formula, bool):
        raise TypeError(f"Unable to reverse the formula {formula!r}")
    if re.match(r"^n( % \d+)? == \d+(\.\.\d+|,\d+)*?$", formula):
        return formula.replace(" == ", " != ")
    if re.match(r"^n( % \d+)? != \d+(\.\.\d+|,\d+)*?$", formula):
        return formula.replace(" != ", " == ")
    if re.match(r"^\(?n == \d+ \|\| n == \d+\)?$", formula):
        return formula.replace(" == ", " != ").replace(" || ", " && ").strip("()")

    if match := re.match(
        r"^(n(?: % \d+)?) == (\d+) && (n(?: % \d+)?) != (\d+)$",
        formula,
    ):
        return f"{match.group(1)} != {match.group(2)} || {match.group(3)} == {match.group(4)}"

    if (
        formula
        == "(n == 1 || n == 2 || n == 3) || n % 10 != 4 && n % 10 != 6 && n % 10 != 9"
    ):
        return (
            "n != 1 && n != 2 && n != 3 && (n % 10 == 4 || n % 10 == 6 || n % 10 == 9)"
        )
    if formula == "(n == 0 || n == 1) || n >= 11 && n <= 99":
        return "n >= 2 && (n < 11 || n > 99)"

    raise ValueError(f"Unable to reverse the formula {formula!r}")


def merge_formulas(formulas: list[str | Literal[True]]) -> str:
    max_n = len(formulas) - 1
    formula = f"{max_n}"
    for n in range(max_n - 1, -1, -1):
        part = formulas[n]
        if isinstance(part, bool):
            raise TypeError(f"Not supported part {part!r}")

        if not re.match(r"^\([^()]+\)$", part):
            part = f"({part})"
        formula = f"{reduce_formula(part)} ? {n} : {formula}"
        if n > 0:
            formula = f"({formula})"

    return formula


class LanguageDict(TypedDict, total=False):
    code: str
    name: str
    plurals: int
    formula: str


LANGUAGES: dict[str, LanguageDict]
# Load language names
with open(
    "modules/cldr-json/cldr-json/cldr-localenames-full/main/en/languages.json",
) as handle:
    data = json.load(handle)
    LANGUAGES = {
        map_code(cldr_code): {"name": name}
        for cldr_code, name in data["main"]["en"]["localeDisplayNames"][
            "languages"
        ].items()
    }

missing = {
    "guw": "Gun",
    "nah": "Nahuatl",
    "smi": "Sami",
    "lld": "Ladin",
}

for code, name in missing.items():
    if code in LANGUAGES:
        raise ValueError(f"{code} is no longer missing!")
    LANGUAGES[code] = {"name": name}

# former Javanese
LANGUAGES["jw"] = LANGUAGES["jv"].copy()
# former Moldavian
LANGUAGES["mo"] = LANGUAGES["ro"].copy()
LANGUAGES["mo"]["name"] = "Moldavian"


# Parse plurals
with open("modules/cldr-json/cldr-json/cldr-core/supplemental/plurals.json") as handle:
    data = json.load(handle)
    for cldr_code, categories in data["supplemental"]["plurals-type-cardinal"].items():
        code = map_code(cldr_code)
        if len(categories) == 1:
            # Just one category
            LANGUAGES[code]["plurals"] = 1
            LANGUAGES[code]["formula"] = "0"
            continue
        formulas = [convert_formula(category) for category in categories.values()]
        if len(categories) == 2:  # noqa: PLR2004
            LANGUAGES[code]["plurals"] = 2
            LANGUAGES[code]["formula"] = reduce_formula(reverse_formula(formulas[0]))
        else:
            cleaned_up_formula = [
                formula for formula in formulas if formula is not False
            ]
            LANGUAGES[code]["plurals"] = len(cleaned_up_formula)
            LANGUAGES[code]["formula"] = merge_formulas(cleaned_up_formula)

# Map some plurals to alternate names
for new, old in MAPPINGS.items():
    for key in ("plurals", "formula"):
        if existing := LANGUAGES[new].get(key):
            raise ValueError(f"{new} already has {key}: {existing}")
        LANGUAGES[new][key] = LANGUAGES[old][key]

# Remove the languages for which we don't have plurals
for code in sorted(LANGUAGES.keys()):
    if "plurals" not in LANGUAGES[code]:
        del LANGUAGES[code]

# Add aliases to the base language
for code, existing in ALL_LANGUAGE_CODES.items():
    # Skip existing and base codes
    if "_" not in code or code in LANGUAGES:
        continue
    base = code.split("_", 1)[0]
    if data := LANGUAGES.get(base):
        LANGUAGES[code] = {
            "name": existing[1],
            "plurals": data["plurals"],
            "formula": data["formula"],
        }


# Remove languages we do not want
del LANGUAGES["und"]  # Unknown language

# Dump as CSV
with open("cldr.csv", "w") as handle:
    writer = csv.writer(handle, delimiter=",", lineterminator="\n")
    writer.writerow(["code", "name", "nplurals", "formula"])
    for code in sorted(LANGUAGES):
        data = LANGUAGES[code]
        writer.writerow(
            [
                code,
                data["name"],
                data["plurals"],
                data["formula"],
            ],
        )

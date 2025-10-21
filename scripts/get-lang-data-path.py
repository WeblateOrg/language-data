#! /usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

from importlib.resources import as_file, files

ref = files("translate") / "lang" / "data.py"
with as_file(ref) as path:
    print(path)

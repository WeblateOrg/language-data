#!/usr/bin/env python3
#
# Copyright © 2012 - 2020 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate Client <https://github.com/WeblateOrg/language-data>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import os
from distutils.command.build import build
from distutils.core import Command
from distutils.dep_util import newer
from glob import glob
from itertools import chain

from setuptools import setup
from setuptools.command.build_py import build_py
from translate.tools.pocompile import convertmo

LOCALE_MASKS = [
    "weblate_language_data/locale/*/LC_MESSAGES/*.po",
]

with open("requirements.txt") as handle:
    REQUIRES = handle.read().split()


class BuildMo(Command):
    description = "update MO files to match PO"
    user_options = []

    def initialize_options(self):
        self.build_base = None

    def finalize_options(self):
        self.set_undefined_options("build", ("build_base", "build_base"))

    def run(self):
        for name in chain.from_iterable(glob(mask) for mask in LOCALE_MASKS):
            output = os.path.splitext(name)[0] + ".mo"
            if not newer(name, output):
                continue
            print(f"compiling {name} -> {output}")
            with open(name) as pofile, open(output, "wb") as mofile:
                convertmo(pofile, mofile, None)


class WeblateBuild(build):
    """Override the default build with new subcommands."""

    # The build_mo has to be before build_data
    sub_commands = [("build_mo", lambda self: True)] + build.sub_commands


setup(
    install_requires=REQUIRES,
    cmdclass={"build_mo": BuildMo, "build": WeblateBuild},
)

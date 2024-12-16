#!/usr/bin/env python3

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

import os
from distutils.command.build import build
from distutils.core import Command
from distutils.dep_util import newer
from glob import glob
from itertools import chain

from setuptools import setup
from translate.tools.pocompile import convertmo

LOCALE_MASKS = [
    "weblate_language_data/locale/*/LC_MESSAGES/*.po",
]


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
            with open(name, "rb") as pofile, open(output, "wb") as mofile:
                convertmo(pofile, mofile, None)


class WeblateBuild(build):
    """Override the default build with new subcommands."""

    # The build_mo has to be before build_data
    sub_commands = [("build_mo", lambda self: True), *build.sub_commands]


setup(
    cmdclass={"build_mo": BuildMo, "build": WeblateBuild},
)

#!/bin/sh

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

REGX='^\("POT-Creation-Date: [0-9 +:-]*\)'

# Grab date from other branch
REPL=$(sed -n "s/$REGX.*/\\1/p" "$1")

# Push it into other files
sed -i -e "s/$REGX/$REPL/" "$2"

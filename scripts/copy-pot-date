#!/bin/sh

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

REGX='^"POT-Creation-Date:.*'

# Grab date from other branch
REPL=$(grep "$REGX" "$1" | sed -e 's/\\\\/\\\\\\\\/')

# Push it into other files
sed -i -e "s/$REGX/$REPL/" "$2"

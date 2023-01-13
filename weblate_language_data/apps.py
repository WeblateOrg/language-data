# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

from django.apps import AppConfig


class LanguageDataConfig(AppConfig):
    name = "weblate_language_data"
    label = "weblate_language_data"
    verbose_name = "Weblate Language Data"

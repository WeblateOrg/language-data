.. image:: https://s.weblate.org/cdn/Logo-Darktext-borders.png
   :alt: Weblate
   :target: https://weblate.org/
   :height: 80px

**Weblate is a copylefted libre software web-based continuous localization system,
used by over 1150 libre projects and companies in more than 115 countries.**

Language definitions used by `Weblate`_ and free to use by others.

.. image:: https://img.shields.io/badge/website-weblate.org-blue.svg
    :alt: Website
    :target: https://weblate.org/

.. image:: https://hosted.weblate.org/widgets/weblate/-/svg-badge.svg
    :alt: Translation status
    :target: https://hosted.weblate.org/engage/weblate/?utm_source=widget

.. image:: https://bestpractices.coreinfrastructure.org/projects/552/badge
    :alt: CII Best Practices
    :target: https://bestpractices.coreinfrastructure.org/projects/552

.. image:: https://img.shields.io/pypi/v/weblate-language-data.svg
    :target: https://pypi.org/project/weblate-language-data/
    :alt: PyPI package

.. image:: https://readthedocs.org/projects/weblate/badge/
    :alt: Documentation
    :target: https://docs.weblate.org/

Usage
=====

The Python module can be installed from the PyPI:

.. code-block:: sh

    pip install weblate-language-data

It contains several modules containing language definitions abd Gettext
translations for them (in a way that they would be discovered by Django when
used as an Django application).

CSV Files
=========

The repository also contains CSV files which are used to generate the Python
code and can be used independently.

* Semicolon delimited files
* Contains language code, name, number of plurals and plural equation

languages.csv
-------------

* Combined from several sources, plurals should match CLDR when available
* Used by `Weblate`_ for language definitions
* Manually edited

aliases.csv
-----------

* Language aliases to map non standard or legacy locales to ones in `languages.csv`
* Manually edited

default_countries.csv
---------------------

* List of default country specific locales
* Used to map them to ones in `languages.csv`
* Manually edited

extraplurals.csv
----------------

* Additional plural variants for some languages
* Usually used in Gettext
* Manually edited

cldr.csv
--------

* Based purely on the CLDR data
* Generated using export-cldr from https://github.com/mlocati/cldr-to-gettext-plural-rules

gettext.csv
-----------

* Based on Gettext defaults
* Generated using export-gettext

translate.csv
-------------

* Extracted from `translate-toolkit`_
* Generated using export-translate

l10n-guide.csv
--------------

* Extracted from the `l10n guide`_
* Generated using export-l10n-guide

languages-po
------------

* Directory containing PO files with langauge names translations
* Extracted from CLDR data

.. _Weblate: https://weblate.org/
.. _translate-toolkit: https://toolkit.translatehouse.org/
.. _l10n guide: https://docs.translatehouse.org/projects/localization-guide/en/latest/

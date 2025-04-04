# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: MIT

"""
Language data definitions.

This is an automatically generated file, see scripts/generate-language-data.py

Do not edit, please adjust language definitions in following repository:
https://github.com/WeblateOrg/language-data
"""
# pylint: disable=line-too-long,too-many-lines

# Known country codes
COUNTRIES: set[str] = {
    "abw",
    "ad",
    "ae",
    "af",
    "afg",
    "ag",
    "ago",
    "ai",
    "aia",
    "al",
    "ala",
    "alb",
    "am",
    "and",
    "ao",
    "aq",
    "ar",
    "are",
    "arg",
    "arm",
    "as",
    "asm",
    "at",
    "ata",
    "atf",
    "atg",
    "au",
    "aus",
    "aut",
    "aw",
    "ax",
    "az",
    "aze",
    "ba",
    "bb",
    "bd",
    "bdi",
    "be",
    "bel",
    "ben",
    "bes",
    "bf",
    "bfa",
    "bg",
    "bgd",
    "bgr",
    "bh",
    "bhr",
    "bhs",
    "bi",
    "bih",
    "bj",
    "bl",
    "blm",
    "blr",
    "blz",
    "bm",
    "bmu",
    "bn",
    "bo",
    "bol",
    "bq",
    "br",
    "bra",
    "brb",
    "brn",
    "bs",
    "bt",
    "btn",
    "bv",
    "bvt",
    "bw",
    "bwa",
    "by",
    "bz",
    "ca",
    "caf",
    "can",
    "cc",
    "cck",
    "cd",
    "cf",
    "cg",
    "ch",
    "che",
    "chl",
    "chn",
    "ci",
    "civ",
    "ck",
    "cl",
    "cm",
    "cmr",
    "cn",
    "co",
    "cod",
    "cog",
    "cok",
    "col",
    "com",
    "cpv",
    "cr",
    "cri",
    "cu",
    "cub",
    "cuw",
    "cv",
    "cw",
    "cx",
    "cxr",
    "cy",
    "cym",
    "cyp",
    "cz",
    "cze",
    "de",
    "deu",
    "dj",
    "dji",
    "dk",
    "dm",
    "dma",
    "dnk",
    "do",
    "dom",
    "dz",
    "dza",
    "ec",
    "ecu",
    "ee",
    "eg",
    "egy",
    "eh",
    "er",
    "eri",
    "es",
    "esh",
    "esp",
    "est",
    "et",
    "eth",
    "fi",
    "fin",
    "fj",
    "fji",
    "fk",
    "flk",
    "fm",
    "fo",
    "fr",
    "fra",
    "fro",
    "fsm",
    "ga",
    "gab",
    "gb",
    "gbr",
    "gd",
    "ge",
    "geo",
    "gf",
    "gg",
    "ggy",
    "gh",
    "gha",
    "gi",
    "gib",
    "gin",
    "gl",
    "glp",
    "gm",
    "gmb",
    "gn",
    "gnb",
    "gnq",
    "gp",
    "gq",
    "gr",
    "grc",
    "grd",
    "grl",
    "gs",
    "gt",
    "gtm",
    "gu",
    "guf",
    "gum",
    "guy",
    "gw",
    "gy",
    "hk",
    "hkg",
    "hm",
    "hmd",
    "hn",
    "hnd",
    "hr",
    "hrv",
    "ht",
    "hti",
    "hu",
    "hun",
    "id",
    "idn",
    "ie",
    "il",
    "im",
    "imn",
    "in",
    "ind",
    "io",
    "iot",
    "iq",
    "ir",
    "irl",
    "irn",
    "irq",
    "is",
    "isl",
    "isr",
    "it",
    "ita",
    "jam",
    "je",
    "jey",
    "jm",
    "jo",
    "jor",
    "jp",
    "jpn",
    "kaz",
    "ke",
    "ken",
    "kg",
    "kgz",
    "kh",
    "khm",
    "ki",
    "kir",
    "km",
    "kn",
    "kna",
    "kor",
    "kp",
    "kr",
    "kw",
    "kwt",
    "ky",
    "kz",
    "la",
    "lao",
    "lb",
    "lbn",
    "lbr",
    "lby",
    "lc",
    "lca",
    "li",
    "lie",
    "lk",
    "lka",
    "lr",
    "ls",
    "lso",
    "lt",
    "ltu",
    "lu",
    "lux",
    "lv",
    "lva",
    "ly",
    "ma",
    "mac",
    "maf",
    "mar",
    "mc",
    "mco",
    "md",
    "mda",
    "mdg",
    "mdv",
    "me",
    "mex",
    "mf",
    "mg",
    "mh",
    "mhl",
    "mk",
    "mkd",
    "ml",
    "mli",
    "mlt",
    "mm",
    "mmr",
    "mn",
    "mne",
    "mng",
    "mnp",
    "mo",
    "moz",
    "mp",
    "mq",
    "mr",
    "mrt",
    "ms",
    "msr",
    "mt",
    "mtq",
    "mu",
    "mus",
    "mv",
    "mw",
    "mwi",
    "mx",
    "my",
    "mys",
    "myt",
    "mz",
    "na",
    "nam",
    "nc",
    "ncl",
    "ne",
    "ner",
    "nf",
    "nfk",
    "ng",
    "nga",
    "ni",
    "nic",
    "niu",
    "nl",
    "nld",
    "no",
    "nor",
    "np",
    "npl",
    "nr",
    "nru",
    "nu",
    "nz",
    "nzl",
    "om",
    "omn",
    "pa",
    "pak",
    "pan",
    "pcn",
    "pe",
    "per",
    "pf",
    "pg",
    "ph",
    "phl",
    "pk",
    "pl",
    "plw",
    "pm",
    "pn",
    "png",
    "pol",
    "pr",
    "pri",
    "prk",
    "prt",
    "pry",
    "ps",
    "pse",
    "pt",
    "pw",
    "py",
    "pyf",
    "qa",
    "qat",
    "re",
    "reu",
    "ro",
    "rou",
    "rs",
    "ru",
    "rus",
    "rw",
    "rwa",
    "sa",
    "sau",
    "sb",
    "sc",
    "sd",
    "sdn",
    "se",
    "sen",
    "sg",
    "sgp",
    "sgs",
    "sh",
    "shn",
    "si",
    "sj",
    "sjm",
    "sk",
    "sl",
    "slb",
    "sle",
    "slv",
    "sm",
    "smr",
    "sn",
    "so",
    "som",
    "spm",
    "sr",
    "srb",
    "ss",
    "ssd",
    "st",
    "stp",
    "sur",
    "sv",
    "svk",
    "svn",
    "swe",
    "swz",
    "sx",
    "sxm",
    "sy",
    "syc",
    "syr",
    "sz",
    "tc",
    "tca",
    "tcd",
    "td",
    "tf",
    "tg",
    "tgo",
    "th",
    "tha",
    "tj",
    "tjk",
    "tk",
    "tkl",
    "tkm",
    "tl",
    "tls",
    "tm",
    "tn",
    "to",
    "ton",
    "tr",
    "tt",
    "tto",
    "tun",
    "tur",
    "tuv",
    "tv",
    "tw",
    "twn",
    "tz",
    "tza",
    "ua",
    "ug",
    "uga",
    "ukr",
    "um",
    "umi",
    "ury",
    "us",
    "usa",
    "uy",
    "uz",
    "uzb",
    "va",
    "vat",
    "vc",
    "vct",
    "ve",
    "ven",
    "vg",
    "vgb",
    "vi",
    "vir",
    "vn",
    "vnm",
    "vu",
    "vut",
    "wf",
    "wlf",
    "ws",
    "wsm",
    "ye",
    "yem",
    "yt",
    "za",
    "zaf",
    "zm",
    "zmb",
    "zw",
    "zwe",
}

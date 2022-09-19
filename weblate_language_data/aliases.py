#
# Copyright © 2012–2022 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

"""Language data definitions.

This is an automatically generated file, see scripts/generate-language-data

Do not edit, please adjust language definitions in following repository:
https://github.com/WeblateOrg/language-data
"""
# pylint: disable=line-too-long,too-many-lines


# Language aliases
ALIASES = {
    "braz_por": "pt_BR",
    "chinese": "zh_Hans",
    "chinese_chs": "zh_Hans",
    "schinese": "zh_Hans",
    "chinese_zh": "zh_Hans",
    "tchinese": "zh_Hant",
    "dutch_be": "nl_BE",
    "flemish": "nl_BE",
    "english_uk": "en_GB",
    "portuguese_br": "pt_BR",
    "portuguese_portugal": "pt_PT",
    "serbo_croatian": "sr_Latn",
    "mspanish": "es_MX",
    "norwegian": "nb_NO",
    "xbelorussian": "be",
    "be_rby": "be_Latn",
    "qz_mm": "my@Zawgyi",
    "es_la": "es",
    "val_es": "ca@valencia",
    "no_nb": "nb_NO",
    "nb_nb": "nb_NO",
    "no_no": "nb_NO",
    "es_eu": "eu",
    "ru_r": "ru",
    "ru_rr": "ru",
    "ar_ar": "ar",
    "jp": "ja",
    "ba_ck": "ba",
    "ca_ps": "ca",
    "by": "be",
    "ua": "uk",
    "ua_ua": "uk",
    "uk_uk": "uk",
    "en_en": "en",
    "cn": "zh_Hans",
    "sl_sl": "sl",
    "pu": "pa",
    "ja_ja": "ja",
    "ko_ko": "ko",
    "cs_cs": "cs",
    "la_la": "la",
    "da_da": "da",
    "et_et": "et",
    "fil_fil": "fil",
    "he_he": "he",
    "in": "id",
    "iw": "he",
    "iw_il": "he",
    "iw_he": "he",
    "in_id": "id",
    "ji": "yi",
    "jw": "jv",
    "mo": "ro_MD",
    "scc": "sr",
    "scr": "hr",
    "sh": "sr_Latn",
    "no": "nb_NO",
    "np": "ne",
    "pk": "ur_PK",
    "sr_cs": "sr",
    "sr_me": "cnr",
    "sr_latn_rs": "sr_Latn",
    "sr_cyrl_rs": "sr_Cyrl",
    "bs_latn_ba": "bs_Latn",
    "nb": "nb_NO",
    "be@latin": "be_Latn",
    "sr@latin": "sr_Latn",
    "sr_rs@latin": "sr_Latn",
    "sr@cyrillic": "sr_Cyrl",
    "sr_rs@cyrillic": "sr_Cyrl",
    "uz@latin": "uz_Latn",
    "uz@latn": "uz_Latn",
    "uz@cyrillic": "uz",
    "zh": "zh_Hans",
    "zhcn": "zh_Hans",
    "zh_cn": "zh_Hans",
    "zh_chs": "zh_Hans",
    "zh_sg": "zh_Hans_SG",
    "zhtw": "zh_Hant",
    "zh_tw": "zh_Hant",
    "zh_hant_tw": "zh_Hant",
    "zh_hant@zh": "zh_Hant",
    "cmn": "zh_Hans",
    "zh_hk": "zh_Hant_HK",
    "zh_hans_cn": "zh_Hans",
    "zh_cmn_hans": "zh_Hans",
    "zh_cmn_hant": "zh_Hant",
    "zh_latn_pinyin": "zh_Latn",
    "zh_latn@pinyin": "zh_Latn",
    "ku_iq": "kmr",
    "az_ir": "azb",
    "ary": "ar_MA",
    "kk@latin": "kk_Latn",
    "kk_cyrl": "kk",
    "pr": "en@pirate",
    "sr@ije": "sr@ijekavian",
    "sr@ijekavianlatin": "sr@ijekavian_Latn",
    "base": "en",
    "source": "en",
    "de_fo": "de@formal",
    "de_form": "de@formal",
    "de_de_x_formal": "de@formal",
    "de_de_x_informal": "de@informal",
    "fr_fo": "fr@formal",
    "fr_form": "fr@formal",
    "fr_fr_x_formal": "fr@formal",
    "fr_fr_x_informal": "fr@informal",
    "lah": "pa_PK",
    "pa_arab": "pa_PK",
    "pa_arab_pk": "pa_PK",
    "pnb": "pa_PK",
    "dk": "da",
    "me": "cnr",
    "me_cyrl": "cnr_Cyrl",
    "gr": "el",
    "rs": "sr",
    "kz": "kk",
    "lk": "si",
    "us": "en_US",
    "vn": "vi",
    "bd": "bn",
    "eg": "ar_EG",
    "ca_es@valencia": "ca@valencia",
    "ca_xv": "ca@valencia",
    "ca_valencia": "ca@valencia",
    "va": "ca@valencia",
    "ang@latin": "ang",
    "cz": "cs",
    "svk": "sk",
    "ptb": "pt_BR",
    "enu": "en_US",
    "bgr": "bg",
    "ptg": "pt",
    "esp": "es",
    "cht": "zh_Hant",
    "chs": "zh_Hans",
    "sve": "sv",
    "csy": "cs",
    "plk": "pl",
    "trk": "tr",
    "des": "de_CH",
    "ena": "en_AU",
    "enp": "en",
    "frb": "fr_BE",
    "gae": "gd",
    "its": "it_CH",
    "nlb": "nl_BE",
    "sky": "sk",
    "srl": "sr_Latn",
    "srb": "sr_Cyrl",
    "aar": "aa",
    "abk": "ab",
    "afr": "af",
    "aka": "ak",
    "alb": "sq",
    "amh": "am",
    "ara": "ar",
    "arg": "an",
    "arm": "hy",
    "asm": "as",
    "ava": "av",
    "ave": "ae",
    "aym": "ay",
    "aze": "az",
    "bak": "ba",
    "bam": "bm",
    "baq": "eu",
    "bel": "be",
    "ben": "bn",
    "bih": "bh",
    "bis": "bi",
    "bod": "bo",
    "bos": "bs",
    "bre": "br",
    "bul": "bg",
    "bur": "my",
    "cat": "ca",
    "ces": "cs",
    "cha": "ch",
    "che": "ce",
    "chi": "zh_Hans",
    "chu": "cu",
    "chv": "cv",
    "cor": "kw",
    "cos": "co",
    "cre": "cr",
    "cym": "cy",
    "cze": "cs",
    "dan": "da",
    "deu": "de",
    "div": "dv",
    "dut": "nl",
    "dzo": "dz",
    "ell": "el",
    "eng": "en",
    "epo": "eo",
    "est": "et",
    "eus": "eu",
    "ewe": "ee",
    "fao": "fo",
    "fas": "fa",
    "fij": "fj",
    "fin": "fi",
    "fra": "fr",
    "fre": "fr",
    "fry": "fy",
    "ful": "ff",
    "geo": "ka",
    "ger": "de",
    "gla": "gd",
    "gle": "ga",
    "glg": "gl",
    "glv": "gv",
    "gre": "el",
    "grn": "gn",
    "guj": "gu",
    "hat": "ht",
    "hau": "ha",
    "hbs": "sr_Latn",
    "heb": "he",
    "her": "hz",
    "hin": "hi",
    "hmo": "ho",
    "hrv": "hr",
    "hun": "hu",
    "hye": "hy",
    "ibo": "ig",
    "ice": "is",
    "ido": "io",
    "iii": "ii",
    "iku": "iu",
    "ile": "ie",
    "ina": "ia",
    "ind": "id",
    "ipk": "ik",
    "isl": "is",
    "ita": "it",
    "jav": "jv",
    "jpn": "ja",
    "kal": "kl",
    "kan": "kn",
    "kas": "ks",
    "kat": "ka",
    "kau": "kr",
    "kaz": "kk",
    "khm": "km",
    "kik": "ki",
    "kin": "rw",
    "kir": "ky",
    "kom": "kv",
    "kon": "kg",
    "kor": "ko",
    "kua": "kj",
    "kur": "ku",
    "lao": "lo",
    "lat": "la",
    "lav": "lv",
    "lim": "li",
    "lin": "ln",
    "lit": "lt",
    "ltz": "lb",
    "lub": "lu",
    "lug": "lg",
    "mac": "mk",
    "mah": "mh",
    "mal": "ml",
    "mao": "mi",
    "mar": "mr",
    "may": "ms",
    "mkd": "mk",
    "mlg": "mg",
    "mlt": "mt",
    "mon": "mn",
    "mri": "mi",
    "msa": "ms",
    "mya": "my",
    "nau": "na",
    "nav": "nv",
    "nbl": "nr",
    "nde": "nd",
    "ndo": "ng",
    "nep": "ne",
    "nld": "nl",
    "nno": "nn",
    "nob": "nb_NO",
    "nor": "nb_NO",
    "nya": "ny",
    "oci": "oc",
    "oji": "oj",
    "ori": "or",
    "orm": "om",
    "oss": "os",
    "pan": "pa",
    "per": "fa",
    "pli": "pi",
    "pol": "pl",
    "por": "pt",
    "pus": "ps",
    "que": "qu",
    "roh": "rm",
    "ron": "ro",
    "rum": "ro",
    "run": "rn",
    "rus": "ru",
    "sag": "sg",
    "san": "sa",
    "sin": "si",
    "slk": "sk",
    "slo": "sk",
    "slv": "sl",
    "sme": "se",
    "smo": "sm",
    "sna": "sn",
    "snd": "sd",
    "som": "so",
    "sot": "st",
    "spa": "es",
    "sqi": "sq",
    "srd": "sc",
    "srp": "sr",
    "ssw": "ss",
    "sun": "su",
    "swa": "sw",
    "swe": "sv",
    "tah": "ty",
    "tam": "ta",
    "tat": "tt",
    "tel": "te",
    "tgk": "tg",
    "tgl": "tl",
    "tha": "th",
    "tib": "bo",
    "tir": "ti",
    "ton": "to",
    "tsn": "tn",
    "tso": "ts",
    "tuk": "tk",
    "tur": "tr",
    "twi": "tw",
    "uig": "ug",
    "ukr": "uk",
    "urd": "ur",
    "uzb": "uz",
    "ven": "ve",
    "vie": "vi",
    "vol": "vo",
    "wel": "cy",
    "wln": "wa",
    "wol": "wo",
    "xho": "xh",
    "yid": "yi",
    "yor": "yo",
    "zha": "za",
    "zho": "zh_Hant",
    "zul": "zu",
}

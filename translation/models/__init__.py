__all__ = ['DEFAULT', 'TRANSLATION_DICT',
    'BASE_URL_LIST', 'languageDict']

import google, youdao, iciba, baidu
from language import languageDict

DEFAULT = 'youdao'

TRANSLATION_DICT = {
    'google' : google.google,
    'youdao' : youdao.youdao,
    'iciba'  : iciba.iciba,
    'baidu'  : baidu.baidu, }

BASE_URL_LIST = {
    'google' : google.BASE_URL,
    'youdao' : youdao.BASE_URL,
    'iciba'  : iciba.BASE_URL,
    'baidu'  : baidu.BASE_URL, }

for k in TRANSLATION_DICT.keys():
    if k not in languageDict.keys():
        del TRANSLATION_DICT[k]

for k in BASE_URL_LIST.keys():
    if k not in languageDict.keys():
        del BASE_URL_LIST[k]

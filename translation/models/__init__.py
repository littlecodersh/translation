__all__ = ['DEFAULT', 'TRANSLATION_DICT',
    'BASE_URL_LIST', 'languageDict']

from . import google, youdao, iciba, baidu, bing
from .language import languageDict

DEFAULT = 'youdao'

def translation_wrapper(fn):
    def _translation_wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except:
            return ''
    return _translation_wrapper

TRANSLATION_DICT = {
    'google' : translation_wrapper(google.google),
    'youdao' : translation_wrapper(youdao.youdao),
    'iciba'  : translation_wrapper(iciba.iciba),
    'baidu'  : translation_wrapper(baidu.baidu),
    'bing'   : translation_wrapper(bing.bing), }

BASE_URL_LIST = {
    'google' : google.BASE_URL,
    'youdao' : youdao.BASE_URL,
    'iciba'  : iciba.BASE_URL,
    'baidu'  : baidu.BASE_URL, 
    'bing'   : bing.BASE_URL, }

for k in TRANSLATION_DICT.keys():
    if k not in languageDict.keys():
        del TRANSLATION_DICT[k]

for k in BASE_URL_LIST.keys():
    if k not in languageDict.keys():
        del BASE_URL_LIST[k]

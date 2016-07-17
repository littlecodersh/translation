__version__ = '1.0.5'
__all__ = ['Translation', 'TranslateError', 'ConnectError',
    'set_default_translation', 'set_default_language', 
    'set_default_proxies', 'get', 'get_all', 
    'google', 'youdao', 'iciba', 'baidu', 'bing']

from .main import Translation
from .exception import TranslateError, ConnectError

t = Translation()
set_default_translation = t.set_default_translation
set_default_language = t.set_default_language
set_default_proxies = t.set_default_proxies
get = t.get
get_all = t.get_all

def google(text, src = None, dst = None, proxies = None):
    return t.get(text, default = 'google', src = src,
        dst = dst, proxies = proxies)
def youdao(text, src = None, dst = None, proxies = None):
    return t.get(text, default = 'youdao', src = src,
        dst = dst, proxies = proxies)
def iciba(text, src = None, dst = None, proxies = None):
    return t.get(text, default = 'iciba', src = src,
        dst = dst, proxies = proxies)
def baidu(text, src = None, dst = None, proxies = None):
    return t.get(text, default = 'baidu', src = src,
        dst = dst, proxies = proxies)
def bing(text, src = None, dst = None, proxies = None):
    return t.get(text, default = 'bing', src = src,
        dst = dst, proxies = proxies)

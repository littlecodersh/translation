from .models import TRANSLATION_DICT, DEFAULT
from .tools import verify_language_flag, test_proxies
from .exception import TranslateError

class Translation(object):
    def __init__(self, default = [DEFAULT], src = 'auto',
            dst = 'zh-CN', proxies = {}):
        self.set_default_translation(default)
        self.set_default_language(src, dst)
        self.set_default_proxies(proxies)
    def set_default_translation(self, default):
        if isinstance(default, str): default = [default]
        self.default = []
        for i in default:
            if i in TRANSLATION_DICT.keys():
                self.default.append(i)
        if not self.default: self.default = [DEFAULT]
    def set_default_language(self, src, dst):
        self.src = src
        self.dst = dst
    def set_default_proxies(self, proxies):
        self.proxies = proxies
    def get(self, text, default = None, src = None,
            dst = None, proxies = None):
        if text == '': return ''
        default = default or self.default[0]
        src     = src     or self.src
        dst     = dst     or self.dst
        proxies = proxies or self.proxies
        for i in (src, dst): verify_language_flag(i, default)
        test_proxies(proxies, default)
        r =  TRANSLATION_DICT[default](text, src, dst, proxies)
        if r == '': raise TranslateError('No translation get, you may retry')
        return r
    def get_all(self, text, default = None, src = None,
            dst = None, proxies = None):
        d = {}
        for t in (default or self.default): d[t] = self.get(text, t, src, dst, proxies)
        return d

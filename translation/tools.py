import requests

from exception import TranslateError, ConnecteError
from models import TRANSLATION_DICT, BASE_URL_LIST, languageDict

def verify_language_flag(flag, defaultLanguage):
    # Whether translation is provided
    if defaultLanguage not in TRANSLATION_DICT.keys():
        raise TranslateError, 'No such translation: ' + defaultLanguage
    # Whether language flag is available
    if flag not in languageDict[defaultLanguage].keys():
        raise TranslateError, 'No language flag in %s named: %s'%(
                defaultLanguage, flag)

def test_proxies(proxies, defaultLanguage):
    try:
        requests.get(BASE_URL_LIST[defaultLanguage], proxies, timeout = 3)
    except requests.exceptions.ConnectionError, e:
        raise ConnecteError, e.message
    except requests.exceptions.ConnectTimeout:
        raise ConnecteError, ('Proxies can\'t work properly, \
                you need to set or change a proxy')
    except AttributeError:
        raise ConnecteError, ('Proxies have wrong format')

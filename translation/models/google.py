import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0', }
BASE_URL = 'http://translate.google.cn/translate_a/t'
params = {
    'client': 'p',
    'ie': 'UTF-8',
    'oe': 'UTF-8',
    'tl': None,
    'sl': None,
    'text': None, }

def google(text, src, dst, proxies):
    params['text'] = text
    params['tl'] = dst
    params['sl'] = src
    r = requests.post(BASE_URL, params, headers = headers, proxies = proxies).json()
    return r[0] if isinstance(r, list) else r

if __name__ == '__main__':
    print(google('Test', 'auto', 'zh-CN', {'http': 'http://127.0.0.1:1080'}))

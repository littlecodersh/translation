import time, json

import requests

BASE_URL = 'http://www.bing.com/translator'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0', 
    'Content-Type': 'application/json; charset=UTF-8', }

def bing(text, src, dst, proxies):
    s = requests.session()
    s.headers.update(headers)
    s.get(BASE_URL, proxies = proxies)

    data = [{
        'id'   : int(time.time() % 1e6),
        'text' : text, }]
    data = json.dumps(data, separators = (',', ':'))
    url = '%s/api/Translate/TranslateArray?from=%s&to=%s'%(
        BASE_URL, '-' if src == 'auto' else src, dst)
    j = s.post(url, data = data, proxies = proxies).json()
    return j['items'][0]['text']

if __name__ == '__main__':
    print(bing('this is a test', 'auto', 'zh-CHS', proxies = {'http': 'http://127.0.0.1:1080',}))

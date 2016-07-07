#coding=utf8
import time, re, json

import requests

BASE_URL = 'http://fanyi.baidu.com/v2transapi'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0', }
def correct_txt(text):
    url = 'http://correctxt.baidu.com/correctxt'
    jQueryFlag = 'jQuery1113014284725192946546_1466505692432'
    params = {
        'text': text,
        'callback': jQueryFlag,
        'ie': 'utf-8',
        'version': 0,
        'from': 'FanyiWeb',
        '_': int(time.time()*1e3), }
    t = requests.get(url, params, headers = headers).text
    try:
        return json.loads(re.search('%s\((.*?)\)$'%jQueryFlag, t).groups()[0])['correctxt']
    except (AttributeError, ValueError):
        return ''
def baidu(text, src, dst, proxies):
    text = correct_txt(text)
    if text == '': return ''
    url = BASE_URL
    data = {
        'from': src,
        'to': dst,
        'query': text,
        'transtype': 'realtime',
        'simple_means_flag': '3', }
    return requests.post(url, data, headers = headers, proxies = proxies
            ).json()['trans_result']['data'][0]['result'][0][1]

if __name__ == '__main__':
    print(baidu(u'测试', 'auto', 'en', {}))

from translation import Translation

t = Translation(default = ['baidu'])
print(t.get('hello', dst = 'zh'))

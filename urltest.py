import urllib.request

html = urllib.request.urlopen("http://baidu.com").read().decode('utf-8')
print(html)

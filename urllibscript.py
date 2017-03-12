#!/usr/local/bin/python3

# This brief the urllib module usage and functionality.

import urllib.request
import urllib.parse


#x = urllib.request.urlopen('https://www.google.com')
#print(x.read())
'''
url = 'http://pythonprogramming.net'
values = {'s': 'basic',
          'submit': 'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
'''

try:

    x = urllib.request.urlopen('http://www.lyricsopedia.com/search/label/Mariyaan')
    print (x.read())

except Exception as e:
    print(str(e))


try:
    url = 'https://www.google.com/search?q=test'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    req = urllib.request.Request(url,headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    print(respData)

except Exception as e:
    print(str(e))

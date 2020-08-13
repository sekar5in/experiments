#!/usr/local/bin/python3

import urllib
#import urllib2
#import requests

url = 'https://www.nseindia.com/corporates/datafiles/BM_All_Forthcoming.csv'

print("downloading with urllib")
urllib.urlretrieve(url, "code.csv")

''' print "downloading with urllib2"
f = urllib2.urlopen(url)
data = f.read()
with open("code2.zip", "wb") as code:
    code.write(data)

print "downloading with requests"
r = requests.get(url)
with open("code3.zip", "wb") as code:
    code.write(r.content)
'''
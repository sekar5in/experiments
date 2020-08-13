import pafy
import re

url = "https://www.youtube.com/playlist?list=PL7A9n1TybRSnhZxF3k4PK_rylpVk9tUmw"
playlist = pafy.get_playlist(url)

#re.search("^name: (\w+)", s)

#print(playlist['title'])

#print(playlist['author'])

#print(len(playlist['items']))
#print(playlist['items'][22])
#print(playlist['items'][22]['pafy'])
#pat = re.compile(r'(?object:).*$')
#res = re.search(pat,string)

DICT_URL = {}

for i in range(0,1):
    sampleText = playlist['items'][i]['pafy']
    pat = re.compile(r'(?::\s).*\s\[')
    res = re.search(pat, str(sampleText))
    url_id = (res.group().lstrip(': ').rstrip(' ['))
    url = "https://www.youtube.com/watch?v=%s"%(url_id)
    print(url)
    name = playlist['items'][i]['playlist_meta']['title']
    print(name)

    filmname = playlist['items'][i]['playlist_meta']['description']
    f_name = re.search("^name: (\w+)", filename)
# This is script is used to generate list data from web.priviw.com into the database based on the argument as filter.

# Author : Dhanasekara Pandian
# Email : sekar5in@quehive.com
# 07-SEP-2017 11:19:00 PM
# Free to modify and use for any purpose
# www.quehive.com
# webPriviwdbFilter.py

# REST API Call
# http://web.priviw.com:3000/api/videos?filter={"where" : {"type" : "Song", "language" : "Hindi" ,"tags" : { "regexp":".*JukeBox.*"} } }

############################################################################################################
# Importing the Libraries
###########################

import requests


def querySet(reqType, reqLanguage, reqRegEx):
    resList = []
    priviwType = reqType
    priviwLanguage = reqLanguage
    priviwRegEx = reqRegEx

    url = 'http://web.priviw.com:3000/api/videos?filter={"where" : {"type" : "' + priviwType + '", "language" : "' + priviwLanguage +'" ,"tags" : { "regexp": "' + priviwRegEx + '"} } }'

    req = requests.get(url).json()
    for url in req:
        resList.append(url['url'])

    return resList

'''
r = querySet("Song", "Tamil", ".*JukeBox.*")

for s in r:
    print(s)
'''
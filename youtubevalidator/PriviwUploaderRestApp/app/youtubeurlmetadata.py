# -*- coding: utf8 -*-

# This is script is used to generate metadata information of the youtube URL video as json output.
# and submit the json result to application url as post method to insert into the database.
# Author : Dhanasekara Pandian
# Email : sekar5in@quehive.com
# 06-SEP-2017 08:22:00 AM
# Free to modify and use for any purpose
# www.quehive.com

############################################################################################################
# Importing the Libraries
###########################
import pafy
import json
import requests
from .webPriviwdbFilter import querySet
#############################################################################################################
# Method to fetch youtube url metadata information in json result. Like Title, url, description, videoid
# and some default values like urlEmbed, Tags, authorid and list as json result as below example output.
#############################################################################################################
'''
{
    "url": "https://www.youtube.com/watch?v=CwqzXckVwHs&t=2s",
    "urlEmbed": "https://youtube.com/embed/CwqzXckVwHs",
    "title": "மனஅமைதிக்கு டாக்டரிடம் செல்ல வேண்டியதில்லை  இளையராஜா பாடல்கள் கேளுங்கள்  | Ilaiyaraja Melody Songs",
    "description": "பூங்காத்து திரும்புமா ..\nசெந்தாழம் பூவில் ...\nமாலை என் வேதனை ..\nமயங்கினேன் சொல்ல  ..  போன்ற இனிய பாடல்கள் தொகுப்பு",
    "media": "youtube",
    "videoInfo": {
        "id": "CwqzXckVwHs",
        "mediaType": "video",
        "provider": "youtube"
    },
    "language": "Tamil",
    "type": "Song",
    "tags": "JukeBox,OnlyCollection",
    "authorId": "59589025e96d3a4182c007f6",
    "thumbnail": "https://i.ytimg.com/vi/CwqzXckVwHs/mqdefault.jpg"
}
'''


def videojson_Result(url, language):

    try:
        # InitiEmpty dict
        videodict = {}

        # variable assignments
        url = url
        videometa = pafy.new(url, basic=True, gdata=True, size=True)
        object_id = videometa.videoid
        embed_url = "https://youtube.com/embed/"
        img_url = "https://i.ytimg.com/vi/"
        video_thumb = img_url+object_id+"/mqdefault.jpg"

        #metadata dictionary definition
        videodict = {'url': url, "urlEmbed": embed_url+object_id, 'title': videometa.title, 'description': videometa.description,

                     'media': 'youtube', 'videoInfo': {'id': videometa.videoid, 'mediaType': 'video', 'provider':'youtube'},
                     'language': language, 'type': 'Song', 'tags': 'JukeBox,OnlyCollection', 'authorId': '59589025e96d3a4182c007f6',
                     'thumbnail': video_thumb
                     }

        # Convert the python dict into json format with indent of 4 spaces by avoiding ascii character
        json_data = json.dumps(videodict, indent=4, ensure_ascii=False)

        # Print the data in json format
        return json_data
    except Exception as e:
        json_data = 500
        return json_data

######################################################################################
# Method to Submit the json content into the URL using request library as POST method.
#######################################################################################


def urlPost(jsonData):

    try:
        url = 'http://web.priviw.com:3000/api/videos'
        resCode = requests.post(url, json=jsonData)
        #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        return (resCode.status_code)

    except Exception as e:
        print(str(e))
        print("Unable to upload the URL")


#############################################################################################
#                                      Main Method Starts here                             #
#############################################################################################

def yturlmetadata(req_language, req_category, req_search, req_url):
    try:
        # variable initialization
        statusResp = 0
        statusString = "null"

        resp_code=[]
        resp_string=[]
        resp_url=[]

        # Language Selection
        # Tamil  | Kannada | Telugu | Hindi | Malayalam | English
        lang = req_language
        category = req_category
        search = ".*" + req_search + ".*"
        urlList = req_url

        # Priviw Database Query to fetch the URL list
        listUrl = querySet(category, lang, search)
        response = []
        # Main loop of uploading all url from the file url.txt one by one.
        for readUrlStr in urlList:
            readUrl = readUrlStr.strip()                # Remove the empty lines or space lines
            if readUrl:                                 # if line has string to proceed

                if any(readUrl in checkUrl for checkUrl in listUrl):
                        statusResp = 409
                        statusString = "Duplicate"
                else:
                        listUrl.append(readUrl)                     # Adding the readUrl URL into the list variable listUrl to compare.
                        jsonData = videojson_Result(readUrl, lang)      #
                        statusCode = urlPost(jsonData)

                        if statusCode == 200:                   # Validate the submit url status as 200 (success)
                            statusResp = 200
                            statusString = "Success"
                        else:                                   # incase of upload error
                            statusResp = statusCode
                            statusString = "Failure"

            response.append({'Code': statusResp, 'Status': statusString, 'URL': readUrl})

        return response

    except Exception as e:
        print(str(e))

#############################################################################################
#                                      Main Method Ends                                    #
#############################################################################################
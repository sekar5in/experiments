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
from webPriviwdbFilter import querySet
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
    #print(json_data)
    return json_data, object_id

######################################################################################
# Method to Submit the json content into the URL using request library as POST method.
#######################################################################################


def urlPost(jsonData):

    try:
        #print(jsonData)
        url = 'http://web.priviw.com:3000/api/videos'
        resCode = requests.post(url, json=jsonData)
        #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        #print(resCode.status_code)
        return (resCode.status_code)

    except Exception as e:
        print(str(e))
        print("Unable to upload the URL")


#############################################################################################
#                                      Main program Starts here                             #
#############################################################################################

try:
    # Language Selection
    # Tamil  | Kannada | Telugu | Hindi | Malayalam | English
    lang = "Hindi"

    # Database query intialization
    print("Querying the Database Started.\n")
    # Variable initialization
    listUrl = querySet("Song", lang, ".*JukeBox.*")

    # Database query intialization
    print("Querying the Database Completed.\n")

    # initialization of Main Program
    print("Program Started and in progressing.....\n")

    # Open file for storing the result
    status = open('urlStatus.txt', 'a')

    # Below is the steps to read line by line
    readMe = open('url.txt', 'r').readlines()

    # Main loop of uploading all url from the file url.txt one by one.
    for readUrlStr in readMe:
        readUrl = readUrlStr.strip()                # Remove the empty lines or space lines
        if readUrl:                                 # if line has string to proceed

            if any(readUrl in checkUrl for checkUrl in listUrl):
                    print("Duplicate found : %s" % readUrl)
                    statusString = "Duplicate"
            else:
                    listUrl.append(readUrl)                     # Adding the readUrl URL into the list variable listUrl to compare.
                    jsonData, objectId = videojson_Result(readUrl, lang)      #
                    statusCode = urlPost(jsonData)

                    if statusCode == 200:                   # Validate the submit url status as 200 (success)
                        print("Uploaded successfully : %s" % readUrl)
                        statusString = "Success"
                    else:                                   # incase of upload error
                        print("Failed : %s" % readUrl)
                        statusString = "Failed"

            # Write the Status and URL into the urlStatus file.
            statusString = str(statusString) + " : " + str(readUrl)
            status.write(statusString + '\n')

    # close the status file.
    status.close()

    print("Execution Completed.")

except Exception as e:
    print(str(e))
    status.close()


#############################################################################################
#                                      Main program Ends                                    #
#############################################################################################

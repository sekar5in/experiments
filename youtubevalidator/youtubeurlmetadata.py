import pafy
import json

# Empty dict
videodict = {}


# variable assignments
url = "https://www.youtube.com/watch?v=yOen62LSrfU"
videometa = pafy.new(url, basic=True, gdata=True, size=True)
object_id = videometa.videoid
embed_url = "https://youtube.com/embed/"
img_url = "https://i.ytimg.com/vi/"
video_thumb = img_url+object_id+"/mqdefault.jpg"


#metadata dictionary definition
videodict = {'url': url, "urlEmbed": embed_url+object_id, 'title': videometa.title, 'description': videometa.description,

             'media': 'youtube', 'videoInfo': {'id': videometa.videoid, 'mediaType': 'video', 'provider':'youtube'},
             'language': 'Tamil', 'type': 'Song', 'tags': 'JukeBox,OnlyCollection', 'authorId': '59589025e96d3a4182c007f6',
             'thumbnail': video_thumb
             }


# Convert the python dict into json format with indent of 4 spaces by avoiding ascii character
json_data = json.dumps(videodict, indent=4, ensure_ascii=False)


# Print the data in json format
print(json_data)


# Below syntax to write the json data into file
#with open('JSONData.json', 'w') as f:
#    json.dump(json_data, f, ensure_ascii=False, indent=None)

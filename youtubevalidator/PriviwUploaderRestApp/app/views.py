# Import libraries
from app import app
from flask import jsonify, render_template, request, abort
from .youtubeurlmetadata import yturlmetadata
import json

@app.route('/')
def index():
    return render_template("index.html")

#########################################
# Jukebox Uploader

priviwupload = {
                'language': "Tamil",
                'category': u'Song',
                'search': u'JukeBox',
                'urllist': [
                            'https://www.youtube.com/watch?v=69szQbkthxw',
                            'https://www.youtube.com/watch?v=Rsn5IEmgyZE',
                            'https://www.youtube.com/watch?v=Ufl-QHlfZm0',
                            'https://www.youtube.com/watch?v=QphiKsynK68'
                           ]
                }



@app.route('/priviw/upload/api/v1.0/jukebox', methods=['GET'])
def get_jukebox():
    return jsonify(priviwupload)


@app.route('/priviw/upload/api/v1.0/jukebox', methods=['POST'])
def post_jukebox():
    if not request.json:
        abort(400)

    content = request.get_json()

    priviwdownload = {
                        'language': content.get('language'),
                        'category': content.get('category'),
                        'search': content.get('search'),
                        'urllist':content.get('urllist')
                    }

    priviwdownload_response = yturlmetadata(priviwdownload['language'], priviwdownload['category'], priviwdownload['search'], priviwdownload['urllist'])

    if priviwdownload_response:
        return jsonify({'Priviw Response': priviwdownload_response})

    else:
        priviwdownload_response = {
            'Code': 'nul',
            'Status': 'null',
            'URL': 'null'
        }
        return jsonify({'Priviw Response': priviwdownload_response})



######################################################################################
# 404, 405 Page Not Found Error

@app.errorhandler(404)
def page_404_not_found(e):
    return render_template("404.html")

@app.errorhandler(405)
def page_405_not_found(e):
    return render_template("405.html")

@app.errorhandler(400)
def page_400_not_found(e):
    return render_template("400.html")

#########################################################################################
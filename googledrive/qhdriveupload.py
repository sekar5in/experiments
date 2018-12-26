#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Upload folder to Google Drive
"""

# Enable Python3 compatibility
from __future__ import (unicode_literals, absolute_import, print_function, division)

# Import Google libraries
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.files import GoogleDriveFileList
import googleapiclient.errors

# Import general libraries
from argparse import ArgumentParser
from os import chdir, listdir, stat
from sys import exit
import ast


# This script to upload the files/folder into google drive. The one time
# permission enabling stores in mycreds.txt file and massively upload
# content to the drive without any manual permission from end user.
# First time allow permission is required.

# Author : Dhanasekara Pandian
# Email : sekar5in@gmail.com
# License : Free to use

# Requirement 
# client_secrets.json must be download once oauth 2.0 has created for gdrive access
# mycreds.txt will be stored with authentication


def parse_args():
    """ 
        Parse arguments
    """

    parser = ArgumentParser(description="Upload local folder to Google Drive")
    parser.add_argument('-s', '--source', type=str, help='Folder to upload')
    parser.add_argument('-d', '--destination', type=str, help='Destination Folder in Google Drive')
    return parser.parse_args()


def authenticate():
    """ 
        Authenticate to Google API
    """
    gauth = GoogleAuth()

    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")

    return GoogleDrive(gauth)


def get_folder_id(drive, parent_folder_id, folder_name):
    """ 
        Check if destination folder exists and return it's ID
    """

    # Auto-iterate through all files in the parent folder.
    file_list = GoogleDriveFileList()
    try:
        file_list = drive.ListFile(
            {'q': "'{0}' in parents and trashed=false".format(parent_folder_id)}).GetList()

    # Exit if the parent folder doesn't exist
    except googleapiclient.errors.HttpError as err:

        # Parse error message
        message = ast.literal_eval(err.content)['error']['message']
        if message == 'File not found: ':
            print(message + folder_name)
            exit(1)
        # Exit with stacktrace in case of other error
        else:
            raise

    # Find the the destination folder in the parent folder's files
    for file1 in file_list:
        if file1['title'] == folder_name:
            print('title: %s, id: %s' % (file1['title'], file1['id']))
            return file1['id']


def create_folder(drive, folder_name, parent_folder_id):
    """
        Create folder on Google Drive
    """
    
    folder_metadata = {
        'title': folder_name,
        # Define the file type as folder
        'mimeType': 'application/vnd.google-apps.folder',
        # ID of the parent folder
        'parents': [{"kind": "drive#fileLink", "id": parent_folder_id}]
        }

    folder = drive.CreateFile(folder_metadata)
    folder.Upload()

    # Return folder information's
    print('title: %s, id: %s' % (folder['title'], folder['id']))
    return folder['id']


def upload_files(drive, folder_id, src_folder_name):
    """ 
        Upload files in the local folder to Google Drive
    """

    # Enter the source folder
    try:
        chdir(src_folder_name)
    # Print error if source folder doesn't exist
    except OSError:
        print(src_folder_name + 'is missing')
    # Auto-iterate through all files in the folder.
    for file1 in listdir('.'):
        # Check the file's size
        statinfo = stat(file1)
        if statinfo.st_size > 0:
            print('uploading ' + file1)
            # Upload file to folder.
            f = drive.CreateFile(
                {"parents": [{"kind": "drive#fileLink", "id": folder_id}]})
            f.SetContentFile(file1)
            f.Upload()
        # Skip the file if it's empty
        else:
            print('file {0} is empty'.format(file1))


def main():
    """ 
        Main
    """
    args = parse_args()

    src_folder_name = args.source
    dst_folder_name = args.destination

    # Authenticate to Google API
    drive = authenticate()

    # Get destination folder ID
    folder_id = get_folder_id(drive, 'root', dst_folder_name)

    # Create the folder if it doesn't exists
    if not folder_id:
        print('creating folder ' + dst_folder_name)
        folder_id = create_folder(drive, dst_folder_name, 'root')
    else:
        print('folder {0} already exists'.format(dst_folder_name))

    # Upload the files
    upload_files(drive, folder_id, src_folder_name)


if __name__ == "__main__":
    main()

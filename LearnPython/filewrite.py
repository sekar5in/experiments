#!/usr/local/bin/python3

# This script used to write a file using python3.

# String to write into the file.
dataString = "This is the test message to write into the file... Please ignore and delete the file"

# File open in write mode and place the datastring message.

saveFile = open('fileWrite.txt', 'w')
saveFile.write(dataString)
saveFile.close()
#!/usr/local/bin/python3

# This script help to append the existing file content.

appendMe = "Additional Line appending from existing data of string line"

saveFile = open('fileWrite.txt', 'a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()

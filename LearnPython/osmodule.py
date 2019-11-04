#!/usr/local/bin/python3

# Its show the basic usage of os module.

import os
import time


curDir = os.getcwd()

print(curDir)

mkDir = os.mkdir('Testfolder')


time.sleep(2)

os.rename('Testfolder', 'TestingFolder')

time.sleep(4)
os.rmdir('TestingFolder')
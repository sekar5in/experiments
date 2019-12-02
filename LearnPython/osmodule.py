#!/usr/local/bin/python3

# Its show the basic usage of os module.

import os
from time import sleep
from .classintro import calculator, calculator1


curDir = os.getcwd()

print(curDir)

mkDir = os.mkdir('Testfolder')


sleep(2)

os.rename('Testfolder', 'TestingFolder')

sleep(4)
os.rmdir('TestingFolder')



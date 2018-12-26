#!/usr/bin/python

from gtts import gTTS
import os
tts = gTTS(text='Hello World, Welcome to Pandora artificial world', lang='en')
tts.save("hello.mp3")
os.system("mpg123 hello.mp3")

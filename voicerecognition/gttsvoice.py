#!/usr/bin/python

from gtts import gTTS
import os
tts = gTTS(text='Hello World, Welcome to Pandora artificial world', lang='en')
path = os.path.join("C:\Program Files (x86)\VideoLAN\VLC\vlc.exe")
print(path)
tts.save("hello.mp3")
os.system(str(path + " hello.mp3"))

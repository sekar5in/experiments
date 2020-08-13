#!/usr/bin/python
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("Sir You said: " + data)
    except sr.UnknownValueError:
        print("Nayan Says Unable to hear you and say again")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):

    if "Nayan" in data:
        speak("Yes Darling tell me")
	
    if "how are you" in data:
        speak("I am fine")
 
    if "what time is it" in data:
        speak(ctime())

    if "Thanks" in data:
        speak("you are welcome darling")

    if "Play tamil songs" in data:
	speak("Ok sir, playing tamil latest songs from youtube")
	os.system("chromium-browser https://www.youtube.com/watch?v=dE5SLY5tKEc&list=PLvTLJAdAwUW1glJ-4mz5GbwkvDcmTxrp9")

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Darling, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
 
# initialization
time.sleep(2)
speak("sekar mama mama mama mama mama ennaaaaaaa panuringaaaaaaaaaa")
while 1:
    data = recordAudio()
    jarvis(data)

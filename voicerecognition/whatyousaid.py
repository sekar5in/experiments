#!/usr/bin/python

# This script is used to speech to text and text to speech as what you said.

import speech_recognition as sr
import pyttsx

# Function to Convert the listening speech to text
def speech_text():

    r = sr.Recognizer()
    sample_rate = 48000
    chunk_size = 2048

    with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
        r.adjust_for_ambient_noise(source)
        print("Speak:")
        audio = r.listen(source)

    try:
        speech = r.recognize_google(audio)
        print("Sir You said :- " + speech)
        return speech

    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


# Function to Convert the text to voice
def text_speech():

    try:

        engine = pyttsx.init(debug=False)
        engine.setProperty('rate', 120)

        text = speech_text()
        if text:
            engine.say('Sir you said' + text)
            engine.runAndWait()

        else:
            engine.say('Sir Can you please say again')
            engine.runAndWait()

    except ImportError as e:
        print("Unable to load the driver")
    except RuntimeError as e:
        print("Driver failed to Initialize")


# Main Program Execution
while True:

    text_speech()

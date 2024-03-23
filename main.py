import speech_recognition as sr
import win32com.client
import os
from win32com.client import Dispatch
import distutils
import pyttsx3

speaker= win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}")
    return query
if __name__ == '__main__':
    say("Hello I am jarvis A.I   ")
    while True:
        print("Listening...")
        text=takeCommand()
        print("The text:",text)
        say(text)

import datetime

import speech_recognition as sr
import win32com.client
import webbrowser
import os
from win32com.client import Dispatch
import distutils
import pyttsx3
import openai

import openai


def ai(prompt):
    openai.api_key = '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'
    messages = [{"role": "system", "content": "You are a intelligent assistant."}]

    message = prompt
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
    return reply


speaker= win32com.client.Dispatch("SAPI.SpVoice")

# todo: try to find ava like voice somwhere
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
        try:
            query=r.recognize_google(audio,language="en-in")
            print(f"User said:{query}")
            return query.lower()
        except Exception as e:
            return "Some Error Occured, Please say the Commands again"
if __name__ == '__main__':
    say("Hello I am AVA  ")

    while True:
        print("Listening...")
        query=takeCommand()
        sites=[["youtube","https://youtube.com"],["instagram","https://instagram.com"],["google","https://google.com"]]
        print("The text:",query)
        say(query)
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
        if "the time" in query:
            strftime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strftime}")
        elif "using artificial intelligence" in query:
            ai(prompt=query)
        else:
            print("chatting")
            reply=ai(query)
            say(reply)



import pyttsx3 #pip install pyttsx3
import datetime

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def speakAlgo(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    newVoiceRate = 145
    engine.setProperty('rate', newVoiceRate)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
def speakNCS(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    newVoiceRate = 165
    engine.setProperty('rate', newVoiceRate)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
def speakAF(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    newVoiceRate = 160
    engine.setProperty('rate', newVoiceRate)
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")
    speak("I am David, I am the upgrade version of Spidy, David is always at your service. What can I do for you?")






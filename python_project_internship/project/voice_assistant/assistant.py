import speech_recognition as sr
import pyttsx3
import requests
import datetime

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    speak("How can I help you?")
    audio = r.listen(source)
    command = r.recognize_google(audio).lower()

if "time" in command:
    time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {time}")

elif "weather" in command:
    speak("Weather feature is enabled")

else:
    speak("Sorry, I did not understand")

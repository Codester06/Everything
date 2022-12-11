import pyttsx3
import time

import datetime 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
# from OtherCommands import wishMe
from CommandsJR import jarvesCommards

def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Welcome back Codexter. Please tell me how may I help you")   

# print(voices[1].id)
    


def security():
    speak("Enter the password to succeed this program.")
    userpassword = input("Enter Your password sir: ")
    password = "CodesterSC"
    while(password == userpassword or password != userpassword):
        if (password == userpassword):
            speak("You may succeed sir")
            print("You may succeed sir")
            time.sleep(1)
            speak("Running jarves sir")
            wishMe()
            jarvesCommards()

            
        elif(password != userpassword):
            print("Password is incorrect,You may not succeed this Program")
            speak("Password is incorrect,You may not succeed this Program")
            
            break
# This code was taken entirely from https://www.analyticsvidhya.com/blog/2020/11/build-your-own-desktop-voice-assistant-in-python/



import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
import wikipedia
import time
import webbrowser
import requests
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
from selenium import webdriver # to control browser operations

def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio)
            print("Your question is, " + data)
            
        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")
    return data


def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)


if __name__=='__main__':
    respond("Hi, I am JARVIS your personal voice assistant!")
          
    while(1):
        respond("How can I help you?")
        text=talk().lower()
        
        if text==0:
            continue
            
        if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
            respond("Ok bye and take care")
            break
            
        if 'wikipedia' in text:
            respond('Searching Wikipedia')
            text =text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=3)
            respond("According to Wikipedia")
            print(results)
            respond(results)
                  
        elif 'time' in text:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")     
        
        elif 'search'  in text:
            text = text.replace("search", "")
            webbrowser.open_new_tab(text)
            time.sleep(5)     
            
        elif 'open google' in text:
            webbrowser.open_new_tab("https://www.google.com")
            respond("Google is open")
            time.sleep(5)
          
                
        elif "open word" in text: 
            respond("Opening Microsoft Word") 
            os.startfile('Mention location of Word in your system') 
        
        else:
           respond("Application not available")

#!/usr/bin/env python3

import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window   
import speech_recognition as sr
import pyttsx3


def textToSpeech(text):
    # initilize text-to-speech engine
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
        

def recognizeSpeech():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Say something!")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return(r.recognize_google(audio))
    except sr.UnknownValueError:
        return("App could not understand the speech.")
    except sr.RequestError as e:
        return("Could not request results from Google Speech Recognition service; {0}".format(e))


# Define the window's contents
layout = [              
            [sg.Frame(layout=[
            [sg.Text("Type the text to read:")], # User type the sentence
            [sg.Multiline(key='-TextInput-')],          # Key Proceed called the function textToSpeech
            [sg.Text(size=(42,1))],
            [sg.Button('Proceed', size=(14, 1))],], title='1. Convert text to speech', relief=sg.RELIEF_SUNKEN, tooltip='Push the buttom and convert text to speech')],
            [sg.Frame(layout=[
            #User press the buttom. Call function speechRecognition and start talking.
            [sg.Text("Press the button below and start talking")],  
            [sg.Text('Result: ', size=(40,1))],
            [sg.Text(size=(42,1), key='-OUTPUT-')],
            [sg.Text(size=(40,1))],
            [sg.Button('Start talking', size=(14, 1))], 
            ],title='2. Convert speech to text', relief=sg.RELIEF_SUNKEN, tooltip='Push the buttom and start talking. Speech will be convert to text')],
            [sg.Quit( size=(15,1))]]

# Create the window
window = sg.Window('Voice interface', layout, element_padding=(5, 5))
event, values = window.read()  

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'Proceed':
        textToSpeech(values['-TextInput-'])
    if event == 'Start talking':
        #print(recognizeSpeech()) #Displaying in console for testing purpose 
        window['-OUTPUT-'].update(recognizeSpeech())
        
window.close()    
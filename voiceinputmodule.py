#import libraries
import speech_recognition as sr
import pyaudio

#find available microphones
def find_Microphones_available():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f'{index}, {name}')

#define listening command
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google( language='en-in')
        print(f"{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

#Simple usage with while loop:
# while True:
#     takeCommand()

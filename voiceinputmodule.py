# import speech recognition module
import speech_recognition as sr

#define listening command
def take_command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    # try understanding audio using google's audio recognizer
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(query)
    # if unable to understand return back
    except Exception as e:
        print("Say that again")
        return "None"

#Simple usage using while loop:
#  while True:
#    take_command()

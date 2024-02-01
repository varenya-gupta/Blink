#import tts library
import pyttsx3

#initialize engine with microsoft sapi5
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#define speak function
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

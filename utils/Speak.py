import pyttsx3


def Speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

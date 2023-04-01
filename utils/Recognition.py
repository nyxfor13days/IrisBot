import speech_recognition as sr


def Recognition():
    recognizer = sr.Recognizer()
    # Uncomment this to see the list of microphones
    # print(sr.Microphone.list_microphone_names())
    # Change microphone to the index your mic is on
    microphone = sr.Microphone(device_index=11)

    with microphone as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en")
        return command
    except sr.RequestError:
        return "API unavailable"
    except sr.UnknownValueError:
        return "Unable to recognize speech"

Recognition()

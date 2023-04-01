import pywhatkit


def SendMessage(phone_number, message, hour, minute):
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)

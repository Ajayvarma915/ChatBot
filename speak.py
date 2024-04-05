import pyttsx3

def Speak(text):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',170)
    print(f"BOT : {text}")
    engine.say(text=text)
    engine.runAndWait()
    print()

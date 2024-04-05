import speech_recognition as sr
import pyaudio as py
def listen():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print('speak something...')
        recog.adjust_for_ambient_noise(source,duration=1)
        recog.pause_threshold=1
        audio=recog.listen(source,0,5)
    try:
        print('recognizing')
        query=recog.recognize_google(audio,language='en-in')
        print(f"You said: {query}")
    except:return ""
    query=str(query)
    print(query)
    return query.lower()    
listen() 
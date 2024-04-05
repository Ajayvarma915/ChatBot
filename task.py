import datetime
import wikipedia
from speak import Speak
import pywhatkit 
def Time():
    time=datetime.datetime.now().strftime("%H:%M")
    if int(time[:2])>=12:time=time+"PM"
    else:time=time+"AM"
    Speak(time)
    
def Date():
    date=datetime.date.today()
    Speak(date)
   
def Day():
    day=datetime.datetime.now().strftime("%A")
    Speak(day)
 
def NonInput(query):
    query=str(query).lower()
    
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()
 
def Input(tag,query):
    query=str(query).lower()
    if "wikipedia" in tag:
        name=str(query).replace("who is","").replace("tell me what is","").replace("what is","").replace("wikipedia","")
        result=wikipedia.summary(name)
        Speak(result)
    elif "google" in tag:
        query=str(query).replace("google search","").replace("search","",).replace("google","")
        pywhatkit.search(query)
        
        
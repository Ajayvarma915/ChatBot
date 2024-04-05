import random
import json
import torch
from speak import Speak
from model import NeuralNet
from Listen import listen
from bot import bag_of_words,tokenize
from task import NonInput,Input
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents=json.load(json_data)
FILE='data.pth'
data=torch.load(FILE)

input_size=data['input_size']
hidden_size=data['hidden_size']
output_size=data['output_size']
all_words=data['all_words']
tags=data['tags']
model_state=data['model_state']

model=NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name='jarvis'
def Main():
    print("Let's have a conversation! tell 'quit' to exit")
    sentence=listen()
    result=str(sentence)
    if sentence in ['signing off','quit','bye']:
        Speak('Bye!!! Take Care.')
        exit()
    sentence=tokenize(sentence)
    x=bag_of_words(sentence,all_words)
    x=x.reshape(1,x.shape[0])
    x=torch.from_numpy(x).to(device)
    
    output=model(x)
    _, predicted=torch.max(output,dim=1)
    tag=tags[predicted.item()]
    
    probs=torch.softmax(output,dim=1)
    prob=probs[0][predicted.item()]
    
    if prob.item()>0.75:
        for intent in intents['intents']:
            if tag==intent['tag']:
                reply=random.choice(intent['responses'])
                if "time" in reply:
                    NonInput(reply)
                elif "date" in reply:
                    NonInput(reply)
                elif "day" in reply:
                    NonInput(reply)
                elif "wikipedia" in reply:
                    Input(reply,sentence)
                elif "google" in reply:
                    Input(reply,result)
                    exit()
                else:
                    Speak(reply)
    else:
        Speak("I don't understand...")
while 1:
    Main()
    
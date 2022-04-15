import json
import os

def prompt_redesign(text_temp,name,term):
    if os.path.exists('./data_'+name+'.json'):
        with open('./data_'+name+'.json','r') as json_file:
            json_data = json.load(json_file)
        tr = len(json_data)
        i=1
        text_history = str()
        while True:
            if int(term)==-1:
                if i<=tr:
                    text_history += 'You:'+json_data[str(i)][0]+'\nFriend:'+json_data[str(i)][1]+'\n'
                    text = text_history+'You:'+text_temp+'\nFriend:'
                    i+=1
                else:
                    break
            elif int(term)>0:
                if i<=tr-int(term):
                    text_history += 'You:'+json_data[str(i)][0]+'\nFriend:'+json_data[str(i)][1]+'\n'
                    text = text_history+'You:'+text_temp+'\nFriend:'
                    i+=1
                else:
                    break            
            else:
                text ='\nYou:'+text_temp+'\nFriend:'
                break
        
        return text
    else:
        text ='\nYou:'+text_temp+'\nFriend:'

        return text

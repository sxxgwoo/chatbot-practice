import json

def prompt_redesign(text_temp,name):
    with open('./data_'+name+'.json','r') as json_file:
        json_data = json.load(json_file)
    tr = len(json_data)
    i=1
    while True:
        if i<=tr:
            text_history = 'You:'+json_data[str(i)][0]+'\nFriend:'+json_data[str(i)][1]
            text = text_history+'\nYou:'+text_temp+'\nFriend:'
            i+=1
        else:
            break
    
    return text

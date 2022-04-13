import json
import os
class retrieve:
    turns = 0
    a={}

    def __init__(self,name,text_temp,res,turns = None,a=None):
        self.name = name
        self.text_temp = text_temp
        self.res = res
        retrieve.turns += 1
        retrieve.a[self.turns]=[self.text_temp,self.res]

        if os.path.exists('./data_'+name+'.json'):
            with open('./data_'+name+'.json','r') as json_file:
                json_data = json.load(json_file)
            tur = len(json_data)

            json_data[tur+1]=[self.text_temp,self.res]
            with open('./data_'+name+'.json','w') as f:
                json.dump(json_data,f,ensure_ascii=False,indent=4)
        else:
            with open('./data_'+name+'.json','w') as f:
                json.dump(retrieve.a,f,ensure_ascii=False,indent=4)
   

import os
import openai
from retrieve import *
from prompt import *

openai.api_key = "my_api_key"

name = input("name:")
co = input("what do you want?(Y:start,N:Stop,T:Backup):")

while True:
  
  if co =="Y":
    text_temp = input("You:")
    if text_temp == 'stop':
      print("=========================END=========================")
      break
    else :
      text = prompt_design(text_temp)
      
      #openai 대답호출
      response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=text,
      temperature=0.5,
      max_tokens=60,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0,
      stop=["You:"]
    )
      res = response['choices'][0]['text'].replace("\n","")
    
      print("Friend:"+ res)
      turns_real=retrieve(name,text_temp,res)
      
    
  elif co =="N":
    print("=========================END=========================") 
    break

  elif co =="T" and os.path.exists(('./data_'+name+'.json')):
    t = int(input("How many turns?:"))
    if t <= 0:
      print("Try again")
      continue 
    elif t>0:
      with open('.\data_'+str(name)+'.json','r') as f:
        json_data = json.load(f)
      tr = len(json_data)
      i=0
      while True:
        if i < t:
          backup = json_data[str(tr-i)]
          print(backup)
          i+=1
        elif i >= t:
          break
      print("=================There's no file==================") 
      break
    else:
      print("Try again")
      continue
  else:
    print("========================wrong========================")
    break


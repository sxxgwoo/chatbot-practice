import os
import openai
from retrieve import *
from prompt import *

openai.api_key = ""

name = input("name:")
term = input("term?:")
co = input("what do you want?(Y:start,N:Stop,T:Backup):")

while True:
  # Y 입력시 대화시작
  if co =="Y":
    text_temp = input("You:")
    if text_temp == 'stop':
      print("=========================END=========================")
      break
    else :
      text = prompt_redesign(text_temp,name,term)
      
    # openai 대답호출
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
      
  # N 입력시 대화종료
  elif co =="N":
    print("=========================END=========================") 
    break
  # T 입력시 대화 백업
  elif co =="T" and os.path.exists(('./data_'+name+'.json')):
    with open('.\data_'+str(name)+'.json','r') as f:
      json_data = json.load(f)
    tr = len(json_data)
    t = int(input("How many turns?:"))
    if t==-1:
      i=0
      while True:
        if tr>i:
          backup_you = 'You:'+json_data[str(i+1)][0]
          backup_friend = 'Friend:'+json_data[str(i+1)][1]
          
          print(backup_you)
          print(backup_friend)
          i+=1
        elif tr<=i: 
          break
      break
    elif tr>=t>0:     
      i=0
      while True:
        if i < t:
          backup_you = 'You:'+json_data[str(tr-t+1+i)][0]
          backup_friend = 'Friend:'+json_data[str(tr-t+1+i)][1]
          
          print(backup_you)
          print(backup_friend)
          i+=1
        elif i >= t:
          break 
      break
    else:
      print("Try again")
      continue
  else: # 대화 백업요청시 입력한 사람의 대화가 없을 경우
    print("=================There's no file==================")
    break

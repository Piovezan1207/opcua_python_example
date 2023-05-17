import requests
import json
link = "http://192.168.150.200:8080/api/blocks"


blackListPositions = [1,2,3,4,5]
blueListPositions = [7,8,9]
redListPositions = [13,14,15,16]

def delet(position, storageId):
    header = {
        "Content-Type" : "application/json"
    }
    
    data = {
        "position" : position, 
        "storageId" : storageId, 
        }
    r = requests.delete(url = link ,data =  json.dumps(data), headers=header ,auth=('Auttom', '12345'))
    print(r.status_code)

def store(position, color):
    
    header = {
        "Content-Type" : "application/json"
    }
    
    data = {
        "position" : position, 
        "color": color, 
        "storageId" : 1, 
        "productionOrder" : None}
    r = requests.post(url = link ,data =  json.dumps(data), headers=header ,auth=('Auttom', '12345'))
    print(r.status_code)

for i in range(1,29): #das posições 1 a 28
    for ii in range(1,3):#Para os storages id 1 e 2
        delet(i, ii) #Remove tudo

#Adiciona as pretas
for i in blackListPositions:
    store(i, 1)
    
#Adiciona as azuis
for i in blueListPositions:
    store(i, 3)
    
#Adiciona as vermelhas
for i in redListPositions:
    store(i, 2)
    

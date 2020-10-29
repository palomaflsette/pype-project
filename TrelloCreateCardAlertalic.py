import requests
from random import randint
from TrelloSettings import token, apiKey
from AlertalicExportData import titulo, desc, _alertbid
from GraphsPortal import *

url = "https://api.trello.com/1/cards"

num1 = randint(0,1)
num2 = randint(0,50)

line = '\n' + 5*'**______**' + '\n'

query = {
   'key': apiKey,
   'token': token, 
   'name': titulo(_alertbid, num1, num2).upper(), 
   'desc':  desc(_alertbid,num1, num2) + line + obrasFornec + outrosFornec,
   'pos': 'top',
   'idList':'5f930e76a536284bc3304799' #id da list
}

response = requests.request(
   "POST",
   url,
   params=query
)

#print(response.text)
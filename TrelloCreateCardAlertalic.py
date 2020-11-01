import requests
from random import randint
from TrelloSettings import token, apiKey, idTopCardAlert, idAlertaList
from AlertalicExportData import titulo, desc, _alertbid, formatDate
from GraphsPortal import *
import TrelloPutCardOnTop

url = "https://api.trello.com/1/cards"


def AlertaLic ():
    
    num1 = randint(0,1)
    num2 = randint(0,50)
    line = '\n' + 5*'**______**' + '\n'

    query = {
    'key': apiKey,
    'token': token, 
    'name': titulo(_alertbid, num1, num2).upper(), 
    'desc':  desc(_alertbid,num1, num2) + line + obrasFornec + outrosFornec,
    'pos': 'top',
    'due' : formatDate(_alertbid, num1, num2),
    'idList': idAlertaList #id da list
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )


TrelloPutCardOnTop.PutOnTop(idTopCardAlert)
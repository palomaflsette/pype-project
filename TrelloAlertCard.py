import requests
import json
from TrelloSettings import token, apiKey, headers
from GraphsPortal import *
from TrelloPutCardOnTop import PutOnTop


def CreateAlertCard (title, descrip, date, idList):
    url = "https://api.trello.com/1/cards"
    query = {
        'key': apiKey,
        'token': token, 
        'name': title, 
        'desc':  descrip,
        'pos': 'top',
        'due' : date,
        'idList': idList #id da list
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )
    

def GetNewCardId (idList, idExistTopCard):
    url = "https://api.trello.com/1/lists/{0}/cards".format(idList)
    query = {'key': apiKey, 'token': token}

    response = requests.get(
        url,
        headers=headers,
        params=query
    )

    listData = []
    if response.status_code == 200:
        listData = json.loads(response.content.decode('UTF-8'))

    PutOnTop(idExistTopCard)
    #Pegando o id do novo card criado com o a função do módulo CreateCard
    idNewCard = listData[0]['id']
    
    return idNewCard



def CoverNewCard (idList, idExistTopCard,  color,):
    
    idNewCard = GetNewCardId(idList, idExistTopCard)
    
    url = "https://api.trello.com/1/cards/{0}/cover".format(idNewCard)
    
    query = {
        "key":apiKey,
        "token":token,
        "value":
            {
            'idAttachment': None,
            'color': color,
            'idUploadedBackground': None,
            'size': 'normal',
            'brightness': 'dark'
            }
    }
    
    response = requests.request(
    'PUT',
    url,
    headers=headers,
    json=query
    )
    
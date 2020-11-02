import json
import requests
from TrelloSettings import apiKey, token, idAlertaList, headers
from TrelloPutCardOnTop import PutOnTop

url = "https://api.trello.com/1/lists/{0}/cards".format(idAlertaList)

query = {'key': apiKey, 'token': token}

response = requests.get(
    url,
    headers=headers,
    params=query
)


listData = []
if response.status_code == 200:
    listData = json.loads(response.content.decode('UTF-8'))

PutOnTop()
#Pegando o id do novo card criado com o a função do módulo CreateCard
idNewCard = listData[1]['id']


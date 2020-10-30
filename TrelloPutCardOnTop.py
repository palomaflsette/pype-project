import requests
from TrelloSettings import token, apiKey

headers = {
   "Accept": "application/json"
}


def PutOnTop(cardId):
       url = "https://api.trello.com/1/cards/{0}".format(cardId)
       
       query = {
      'key': apiKey,
      'token': token, 
      'pos': 'top',
      }
       response = requests.request(
         "PUT",
         url,
         headers=headers,
         params=query
      )
import requests
from TrelloSettings import token, apiKey

url = "https://api.trello.com/1/cards/5f7e2d4a4628f50b3de5de85"

headers = {
   "Accept": "application/json"
}

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
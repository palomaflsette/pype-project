import requests

from TrelloSettings import apiKey, token

url = "https://api.trello.com/1/lists/5f930e76a536284bc3304799/cards"

query = {
    'key': apiKey,
    'token': token,

}

response = requests.request(
    "GET",
    url,
    params=query
)

print(response.text)

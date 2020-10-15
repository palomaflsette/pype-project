import requests
import json

from requests import api
from bid_settings import API_TOKEN, lista_url

headers = {'Accept': "application/json",
           'chave-api-dados': '{0}'.format(API_TOKEN)}


def get_data_bid():
    data_bid = []
    
    for i in range(len(lista_url)):
        api_url = '{0}'.format(lista_url[i])

        response = requests.get(api_url, headers=headers)
    
        if response.status_code == 200:  
            _bid = json.loads(response.content.decode('UTF-8'))
            data_bid.append(_bid)
        else:
            return None
          
    return data_bid
  
bid = get_data_bid()

#print(bid)




'''data_ = []
    
for i in range(len(url_contratos)):
    api_url = '{0}'.format(url_contratos)

    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:  
        _bid = json.loads(response.content.decode('UTF-8'))
        data_.append(_bid)
        

print(data_)'''
import requests
import json
from BidSettings import API_URL_BASE, headers


def get_data_bid():
    
    url = API_URL_BASE

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:  
        _bid = json.loads(response.content.decode('UTF-8'))
    else:
        return None
          
    return _bid
  
bid = get_data_bid()

#print(bid)


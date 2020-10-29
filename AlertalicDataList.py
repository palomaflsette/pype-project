import json
import requests
from AlertalicSettings import API_TOKEN_ALERTA, lista_url_alerta

headers = {'Accept': "application/json",
           'chave-api-dados': '{0}'.format(API_TOKEN_ALERTA)}


def get_alertabid():
    data_bid = []

    for i in range(len(lista_url_alerta)):
        api_url = '{0}'.format(lista_url_alerta[i])

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            _bid = json.loads(response.content.decode('UTF-8'))
            data_bid.append(_bid['licitacoes'])
        else:
            return None

    return data_bid


alertabid = get_alertabid()

#print(len(alertabid))
#print(alertabid[1][40]['id_licitacao'])


'''api_url=None

api_url = '{0}'.format(lista_url_alerta[0])

print(len(lista_url_alerta))

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    _bid = json.loads(response.content.decode('UTF-8'))
    print(_bid)'''
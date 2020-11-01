import requests
from TrelloSettings import token, apiKey, idTopCardLeads, idAlertaLeadsList
from BidDataExportLeads import ListingData, _bid
import TrelloPutCardOnTop
from datetime import datetime

url = "https://api.trello.com/1/cards"

data_hora = datetime.now()
now = data_hora.strftime('%d/%m/%Y %H:%M')

def LeadAlert ():
    query = {
    'key': apiKey,
    'token': token, 
    'name': 'ALERTA: LEAD DO DIA ' + now, #titulo(_alertbid, num1, num2).upper(), 
    'desc': '## **_Dados extraídos da Controladoria Geral da União_**\n' + ListingData(_bid[0]),
    'pos': 'top',
    'idList': idAlertaLeadsList #id da list
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )


TrelloPutCardOnTop.PutOnTop(idTopCardLeads)


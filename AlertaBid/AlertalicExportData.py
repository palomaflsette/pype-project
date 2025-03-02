from datetime import date, datetime, timezone
from AlertaBid.AlertalicDataList import get_alertabid
from random import randint
from GraphsPortal import *


_alertbid = get_alertabid()

'''now = datetime.now().isoformat()
_now = None
for i in now:
    if ':' in now:
        _now=now.replace(':', '.')
        
f = open("{0}".format(_now), 'w+')'''

def id(dic_bid, n1, n2):
    return dic_bid[n1][n2]['id_licitacao']
    
def title(dic_bid, n1, n2):
    return dic_bid[n1][n2]['titulo']

def uf(dic_bid, n1, n2):
    return dic_bid[n1][n2]['uf']

def orgao(dic_bid, n1, n2):
    return dic_bid[n1][n2]['orgao']

def objeto(dic_bid, n1, n2):
    return dic_bid[n1][n2]['objeto']

def data_hora(dic_bid, n1, n2):
    return dic_bid[n1][n2]['aberturaComHora']

def formatDate (dic_bid, n1, n2):
    data = dic_bid[n1][n2]['abertura_datetime'].split(' ')[0]
    
    return data

def data(dic_bid, n1, n2):
    return dic_bid[n1][n2]['abertura']

def link(dic_bid, n1, n2):
    return dic_bid[n1][n2]['link']

def link_externo(dic_bid, n1, n2):
    return dic_bid[n1][n2]['linkExterno']

def municipio(dic_bid, n1, n2):
    return dic_bid[n1][n2]['municipio']

def tipo(dic_bid, n1, n2):
    return dic_bid[n1][n2]['tipo']

def desc(dic_bid, n1, n2):
    text = "## ID da licitação: {0}\n\n\n- ### **Objeto: {1}**\n\n- **UF:** {2}\n\n- **Orgão:** {3}\n\n- **Data de abertura:** {4}\n\n- **Link:** {5}\n- **Link externo:** {6}\n\n- **Município:** {7}\n\n- **Tipo:** {8}".format(id(dic_bid, n1, n2),
                                                                                                                                                                                                                                  objeto(dic_bid, n1, n2),
                                                                                                                                                                                                                                  uf(dic_bid,n1,n2),
                                                                                                                                                                                                                                  orgao(dic_bid, n1, n2),
                                                                                                                                                                                                                                  data_hora(dic_bid, n1,n2),
                                                                                                                                                                                                                                  link(dic_bid,n1,n2),
                                                                                                                                                                                                                                  link_externo(dic_bid, n1, n2),
                                                                                                                                                                                                                                  municipio(dic_bid, n1, n2),
                                                                                                                                                                                                                                  tipo(dic_bid, n1, n2))
                                                                                                                                                                   
    
    return text

#print(formatDate(_alertbid, 1, 0))

num1 = randint(0,1)
num2 = randint(0,50)
line = '\n' + 5*'**______**' + '\n'

cardTitle = title(_alertbid, num1, num2).upper()
cardDescription =  desc(_alertbid,num1, num2) + line + obrasFornec + outrosFornec
dateBid = formatDate(_alertbid, num1, num2)
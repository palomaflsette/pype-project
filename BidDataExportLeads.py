from BidDataList import bid
from datetime import datetime

_bid = bid
def licitacao():
    pass


def orgao_superior():
    pass


def numero_licitacao():
    pass


def modalidade():
    pass


def valor_licitacao():
    pass


def unidade_gestora():
    pass


def data_abertura():
    pass


def ListingData(data):
    text = ''
    for k, v in data.items():
        if type(v) is not dict:
            text = "\n- ###" + k + ": " + str(v) + text
        else:
            text = text + '\n\n' + "## ****" + str(k) + "****\n### " + ListingData(v)

    return text


#print(ListingData(_bid[0]))

data_hora = datetime.now()
now = data_hora.strftime('%d/%m/%Y %H:%M')

cardTitle = 'ALERTA: LEAD DO DIA ' + now
cardDescrip = '## **_Dados extraídos da Controladoria Geral da União_**\n' + ListingData(_bid[0])
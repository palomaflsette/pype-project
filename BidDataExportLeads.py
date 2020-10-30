from BidDataList import bid

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


print(ListingData(_bid[0]))

import os
import sys 
from datetime import date, datetime, timezone
from bid_data_list import get_data_bid


_bid = get_data_bid()

'''now = datetime.now().isoformat()
_now = None
for i in now:
    if ':' in now:
        _now=now.replace(':', '.')
        
f = open("{0}".format(_now), 'w+')'''

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


def organize(data):
    for k, v in data.items():        
        if type(v) is not dict:
            print("- " + str(k) + ": "  + str(v))
            #return "- " + str(k) + ": "  + str(v)
            #print(type(item))
        else:
            print("\n")
            print("****" + str(k) + "****")
            organize(v)
            #return "\n****" + str(k) + "****" + "\t" + organize(v)
            
                
                        
print(organize(_bid[1][0]))

#print(_bid[0][0]['licitacao']['objeto'])
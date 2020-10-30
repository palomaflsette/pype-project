
from random import randint, choice

API_TOKEN = '921ea4b4c449bd40b92cf3d010e98d26'


pag = randint(1,5) #para escolher uma pagina aleatoria entre 1-5

#orgaos selecionados para filtrar contratos relacionados
lista_siafi = ['29209', '39000', '44000', '44205', '32210', '32263', '20411']

#seleção aleatoria de orgaos selecionados
cod_siafi = choice(lista_siafi)

diaIni = randint(10,30)
mesIni = randint(10,12)
anoIni = randint(2010,2015)

diaFim = randint(10,30)
mesFim = randint(10,12)
anoFim = randint(2016, 2021)

dataIni = '{0}/{1}/{2}'.format(diaIni, mesIni, anoIni)
dataFim = '{0}/{1}/{2}'.format(diaFim, mesFim, anoFim)



API_URL_BASE = 'http://www.portaltransparencia.gov.br/api-de-dados/contratos?dataInicial={0}%2F{1}%2F{2}&dataFinal={3}%2F{4}%2F{5}&codigoOrgao={6}&pagina={7}'.format(diaIni,mesIni,anoIni, diaFim,mesFim,anoFim,cod_siafi,pag)
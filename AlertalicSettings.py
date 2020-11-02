from random import randint

API_TOKEN_ALERTA = 'a27d0b3a41e73335a24af27094457098'

uf = 'RJ,SP,AL,MT,MG,RS,SE,AM'

palavras_chave = 'engenharia,pavimentacao,reforma,construcao,estrada,construtora,restauracao,obra'

cod_municipios = [] #caso a haja interesse, consultar a planilha que está no diretório para encontrar os códigos dos municípios

#Duas chamadas de API de licitações: inclui todas as licitações recentes dos estados de 'uf' com as palavras chave selecionadas.
#As urls seguintes referem-se às páginas 1 e 2, respectivamente, contendo 50 licitações em cada página.
#As primeiras 100 licitações diárias retornadas são gratuitas, as seguintes custam R$0,01 cada. 
#Cada requisisição diária diferente custa R$0,01. As requisições já feitas, no mesmo dia, não são cobradas novamente caso acessadas de novo.

#Neste caso, com este exemplo de demo, estima-se que eu estaria pagando, diariamente, apenas R$0,02 por chamadas de APIs, recebendo 100 licitações diariamente.


url_alertalic1 = 'https://alertalicitacao.com.br/api/v1/licitacoesAbertas/?uf={0}&pagina=3&palavra_chave={1}&token={2}'.format(uf, palavras_chave, API_TOKEN_ALERTA)
url_alertalic2 = 'https://alertalicitacao.com.br/api/v1/licitacoesAbertas/?uf={0}&pagina=2&palavra_chave={1}&token={2}'.format(uf, palavras_chave, API_TOKEN_ALERTA)


lista_url_alerta = [url_alertalic1, url_alertalic2]

#print(lista_url_alerta)

headers = {'Accept': "application/json",
           'chave-api-dados': '{0}'.format(API_TOKEN_ALERTA)}

'''Mais informações em:'''
#https://alertalicitacao.com.br/!api
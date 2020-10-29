
API_TOKEN = '921ea4b4c449bd40b92cf3d010e98d26'




listDic_params_lic = [{ "api": "api-de-dados/licitacoes",
                     "data_ini": "29/11/2019",
                    "data_fim": "29/12/2019",
                     "cod_org":"25000" },
                    { "api": "api-de-dados/licitacoes",
                     "data_ini": "29/01/2020",
                    "data_fim": "29/02/2020",
                     "cod_org":"25000" }]


lista_url = []
API_URL_BASE = None
for i in range(len(listDic_params_lic)):
    API_URL_BASE = 'http://www.portaltransparencia.gov.br/{0}?dataInicial={1}%2F{2}%2F{3}&dataFinal={4}%2F{5}%2F{6}&codigoOrgao={7}&pagina=2'.format(listDic_params_lic[i-1]['api'], 
                                                                                                                                        listDic_params_lic[i-1]['data_ini'][:2], 
                                                                                                                                        listDic_params_lic[i-1]['data_ini'][3:5], 
                                                                                                                                        listDic_params_lic[i-1]['data_ini'][6:10],
                                                                                                                                        listDic_params_lic[i-1]['data_fim'][:2],
                                                                                                                                        listDic_params_lic[i-1]['data_fim'][3:5], 
                                                                                                                                        listDic_params_lic[i-1]['data_fim'][6:10], 
                                                                                                                                        listDic_params_lic[i-1]['cod_org'])
    lista_url.append(API_URL_BASE)

#print(lista_url)

#url_contratos = 'http://www.portaltransparencia.gov.br/api-de-dados/licitacoes/contratos-relacionados-licitacao?codigoUG=170144&numero=000192019&codigoModalidade=6'
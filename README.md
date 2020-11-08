# pype-project
### | Insurtech Innovation Program | 

## 
## Pype
Pype é um projeto que consiste em captar informações de diferentes bases de dados, como Portal da Transparência e Alerta Licitação, e migrá-las em forma de cartões para a plataforma Trello, comunicando-se com suas respectivas APIs.


#
### Instale as pendências:
~~~
> pip install -r requirements.txt
~~~


### Execução:
~~~
> python engine.py
~~~

Atente-se para as settings em cada pasta contendo os módulos, pois deve-se inserir dados relativos a tokens e chaves para a execução do código. Deve-se incluir as devidas chaves nas variáveis que contém strings vazias.


![gif](gg_1.gif)


Link do quadro onde chegam os dados: https://trello.com/b/kYhmuA0q/pype-garantia-bid-2020


#
### Documentações
- Trello API: https://developer.atlassian.com/cloud/trello/rest/api-group-actions/
- Portal da Transparência: http://www.portaltransparencia.gov.br/swagger-ui.html
- Alerta Licitação: https://alertalicitacao.com.br/!api

#
### Roadmap
- Desenvolver um crontab em um servidor na nuvem para definir periodicidade e compilação automática diariamente.

import requests
import json as js
from trello import TrelloClient
from bid_export_data import _bid

token='6a7d2ae1e88e4efb6ff70d9eff3615407bafd09e6b18ba73d9893ed532b996a5'
api_key='933c29a6a69bbdcd0ddc33965ba9adeb'
token_secret='dfd39438bf976dc01c1089a8297136d75e6df021a3f941268cca9f21c1f629e5'

client = TrelloClient(
    api_key=api_key,
    token=token,
    token_secret=token_secret
)

'''for card in my_list.list_cards():
    print(card.name)'''


url = "https://api.trello.com/1/cards"


query = {
   'key': api_key, #from settings
   'token': token, #from settings
   'name': "Licitação: " + _bid[1][1]['licitacao']['numero'] + " / " + _bid[1][1]['modalidadeLicitacao']['descricao'], #Licitação: descricao - ModalidadeLicitacao
   'desc': _bid[1][1]['licitacao']['objeto'], #Licitacao - objeto
   'pos':"bottom",
   'due':"10-13-2020", #data de abertura
   'idList':'5f7b2f4eee08e34fc9ebe159' #id da list caixa de entrada
}



response = requests.request(
   "POST",
   url,
   params=query
)

print(response.text)



'''url = "https://trello.com/b/kYhmuA0q"

oauth_secret = 'dfd39438bf976dc01c1089a8297136d75e6df021a3f941268cca9f21c1f629e5'

query = {
   'key': '933c29a6a69bbdcd0ddc33965ba9adeb',
   'token': '6a7d2ae1e88e4efb6ff70d9eff3615407bafd09e6b18ba73d9893ed532b996a5'
}

headers = {
   "Accept": "application/json"
}


response = requests.request(
   "PUT",
   url,
   headers=headers,
   params=query
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))'''





'''class trello:

    def __init__ (self):
        self.key = '933c29a6a69bbdcd0ddc33965ba9adeb'
        self.token = '6a7d2ae1e88e4efb6ff70d9eff3615407bafd09e6b18ba73d9893ed532b996a5'
        self.board = 'kYhmuA0q'


    def getBoard(self):
        url = "https://api.trello.com/1/boards/" + self.board

        querystring = {"actions":"all","boardStars":"none","cards":"none","card_pluginData":"false","checklists":"none","customFields":"false","fields":"name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames","lists":"open","members":"none","memberships":"none","membersInvited":"none","membersInvited_fields":"all","pluginData":"false","organization":"false","organization_pluginData":"false","myPrefs":"false","tags":"false","key":self.key,"token":self.token}

        response = requests.request("GET", url, params=querystring)

        print(response.text)

    def getCards(self):
        self.limit = '30'
        url = 'https://api.trello.com/1/boards/' + self.board + '/cards/?limit=' + self.limit + '&fields=name&members=true&member_fields=fullName&key=' + self.key + '&token=' + self.token

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }

        call = requests.get(url , headers=headers)
        dic = js.loads(call.text)

        print(dic)


    def getCardID(self):
        self.idCard = '5825f7408fc73004763693d7'
        
        url = 'https://trello.com/1/boards/' + self.board + '/cards/' + self.idCard + '?key=' + self.key + '&token=' + self.token

        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }

        call = requests.get(url , headers=headers)
        dic = js.loads(call.text)

        print(dic)

    def getMember(self):
        self.member = '550a1457c58a3212b6851477'

        url = "https://api.trello.com/1/members/" + self.member

        querystring = {"boardBackgrounds":"none","boardsInvited_fields":"name,closed,idOrganization,pinned","boardStars":"false","cards":"none","customBoardBackgrounds":"none","customEmoji":"none","customStickers":"none","fields":"all","organizations":"none","organization_fields":"all","organization_paid_account":"false","organizationsInvited":"none","organizationsInvited_fields":"all","paid_account":"false","savedSearches":"false","tokens":"none","key": self.key,"token":self.token}

        response = requests.request("GET", url, params=querystring)

        print(response.text)

trello.getBoard()'''
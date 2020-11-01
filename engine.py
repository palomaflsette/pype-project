from TrelloCreateCardAlertalic import AlertaLic
from TrelloPutCardOnTop import PutOnTop
from TrelloSettings import idTopCardAlert, idTopCardLeads
from TrelloCreateCardBidLeads import LeadAlert

def main ():
    AlertaLic()
    PutOnTop(idTopCardAlert)
    LeadAlert()
    PutOnTop(idTopCardLeads)
    

if __name__ == "__main__":
    main()
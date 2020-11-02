from TrelloAlertCard import CreateAlertCard, CoverNewCard
from TrelloSettings import idTopCardLeads, idAlertaLeadsList, idTopCardLeads, idAlertaList, idTopCardAlert
from AlertalicExportData import cardTitle, cardDescription, dateBid
import BidDataExportLeads

def main ():
    CreateAlertCard(cardTitle, cardDescription, dateBid, idAlertaList)
    CoverNewCard(idAlertaList, idTopCardAlert, 'red')
    CreateAlertCard(BidDataExportLeads.cardTitle, BidDataExportLeads.cardDescrip, 'null', idAlertaLeadsList)
    CoverNewCard(idAlertaLeadsList, idTopCardLeads, 'orange')

    

if __name__ == "__main__":
    main()
from TrelloAlertCard import CreateAlertCard, CoverNewCard
from TrelloSettings import idTopCardLeads, idAlertaLeadsList, idTopCardLeads, idAlertaList, idTopCardAlert
from AlertaBid.AlertalicExportData import cardTitle, cardDescription, dateBid
import PortalTransp.BidDataExportLeads 

def main ():
    CreateAlertCard(cardTitle, cardDescription, dateBid, idAlertaList)
    CoverNewCard(idAlertaList, idTopCardAlert, 'red')
    CreateAlertCard(PortalTransp.BidDataExportLeads.cardTitle, PortalTransp.BidDataExportLeads.cardDescrip, 'null', idAlertaLeadsList)
    CoverNewCard(idAlertaLeadsList, idTopCardLeads, 'orange')

    

if __name__ == "__main__":
    main()
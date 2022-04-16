import requests 
import time
from pymongo import MongoClient

if __name__ =="__main__":

    #Connnecting to database
    client = MongoClient("mongodb+srv://mohitm12:Password1@dbcluster.x93gw.mongodb.net/StockDB?ssl=true&ssl_cert_reqs=CERT_NONE")
    db = client.get_database('StockDB')

    #Connecting to records
    aapl = db.AAPL
    hpq = db.HPQ
    ibm = db.IBM
    nke = db.NKE
    wmt = db.WMT
    pfe = db.PFE

    #Getting each stock's data from respecetive api
    
    aapl_url = "https://api.twelvedata.com/time_series?symbol=AAPL&interval=1day&apikey=e15054a89cfd4361adafd867b422fe0c"
    hpq_url = "https://api.twelvedata.com/time_series?symbol=HPQ&interval=1day&apikey=e15054a89cfd4361adafd867b422fe0c"
    ibm_url = "https://api.twelvedata.com/time_series?symbol=IBM&interval=1day&apikey=e15054a89cfd4361adafd867b422fe0c"
    nke_url = "https://api.twelvedata.com/time_series?symbol=NKE&interval=1day&apikey=e15054a89cfd4361adafd867b422fe0c"
    wmt_url = "https://api.twelvedata.com/time_series?symbol=WMT&interval=1day&apikey=e15054a89cfd4361adafd867b422fe0c"
    pfe_url = "https://api.twelvedata.com/time_series?symbol=PFE&interval=1day&apikey=e15054a89cfd4361adafd867b422fe0c"


    while True:

        #1
        aapl_records = requests.get(aapl_url)
        
        if aapl_records.status_code == 200:
            aapl_data = aapl_records.json()
            aapl.insert_one(aapl_data)
        
        else:
            print("Data insert failed!")

        #2
        hpq_records = requests.get(hpq_url)
        
        if hpq_records.status_code == 200:
            hpq_data = hpq_records.json()
            hpq.insert_one(hpq_data)
        
        else:
            print("Data insert failed!")

        #3
        ibm_records = requests.get(ibm_url)
        
        if ibm_records.status_code == 200:
            ibm_data = ibm_records.json()
            ibm.insert_one(ibm_data)
        
        else:
            print("Data insert failed!")

        #4
        nke_records = requests.get(nke_url)
        
        if nke_records.status_code == 200:
            nke_data = nke_records.json()
            nke.insert_one(nke_data)
        
        else:
            print("Data insert failed!")

        #5
        wmt_records = requests.get(wmt_url)
        
        if wmt_records.status_code == 200:
            wmt_data = wmt_records.json()
            wmt.insert_one(wmt_data)
        
        else:
            print("Data insert failed!")

        #6
        pfe_records = requests.get(pfe_url)
        
        if pfe_records.status_code == 200:
            pfe_data = pfe_records.json()
            pfe.insert_one(pfe_data)
        
        else:
            print("Data insert failed!")

        #Wait for a day
        time.sleep(86400)
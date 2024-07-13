import requests
import csv

def getCompanyOverview(companySymbol, key):

    url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol=" + companySymbol + "&apikey=" + key

    data = requests.get(url)
    return data.json()
    

def getCorporateActionDividends(companySymbol, key):
    
    url = "https://www.alphavantage.co/query?function=DIVIDENDS&symbol=" + companySymbol + "&apikey=" + key
    
    data = requests.get(url)
    return data.json()


def getCorporateActionSplits(companySymbol, key):
    
    url = "https://www.alphavantage.co/query?function=SPLITSS&symbol=" + companySymbol + "&apikey=" + key
    
    data = requests.get(url)
    return data.json()


def getIncomeStatement(companySymbol, key):
    
    url = "https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=" + companySymbol + "&apikey=" + key
    
    data = requests.get(url)
    return data.json()


def getBalanceSheet(companySymbol, key):
    
    url = "https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=" + companySymbol + "&apikey=" + key
    
    data = requests.get(url)
    return data.json()


def getCashFlow(companySymbol, key):
    
    url = "https://www.alphavantage.co/query?function=CASH_FLOW&symbol=" + companySymbol + "&apikey=" + key
    
    data = requests.get(url)
    return data.json()


def getEarnings(companySymbol, key):
    
    url = "https://www.alphavantage.co/query?function=EARNINGS&symbol=" + companySymbol + "&apikey=" + key
    
    data = requests.get(url)
    return data.json()


def getListingStatusActive(key):
    
    url = "https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=" + key

    with requests.Session() as s:
        
        download = s.get(url)
        decodedContent = download.content.decode('utf-8')
        cr = csv.reader(decodedContent.splitlines(), delimiter=',')
        
        data = list(cr)

    return data


def getListingStatuDelisted(key):
    
    url = "https://www.alphavantage.co/query?function=LISTING_STATUS&state=delisted&apikey=" + key

    with requests.Session() as s:
        
        download = s.get(url)
        decodedContent = download.content.decode('utf-8')
        cr = csv.reader(decodedContent.splitlines(), delimiter=',')
        
        data = list(cr)

    return data
import requests
import json
import pathlib
import csv


# Get Alpha Vantage API key from file
def getAlphaVantageKey(path):
    alphaVantageKeyPath = pathlib.Path(__file__).parent.parent.joinpath(path)

    with open(alphaVantageKeyPath) as keys:
        keyObjects = json.load(keys)

    alphaVantageKey = keyObjects["accounts"][0]["key"]
    
    return alphaVantageKey


# Get listed or active companies
def getListingStatusActive(alphaVantageKeyPath):
    
    key = getAlphaVantageKey(alphaVantageKeyPath)
    
    url = "https://www.alphavantage.co/query?function=LISTING_STATUS&state=active&apikey=" + key

    with requests.Session() as s:
        
        download = s.get(url)
        decodedContent = download.content.decode('utf-8')
        cr = csv.reader(decodedContent.splitlines(), delimiter=',')
        
        data = list(cr)

    return data


# Get delisted or inactive companies
def getListingStatuDelisted(alphaVantageKeyPath):
    
    key = getAlphaVantageKey(alphaVantageKeyPath)
    
    url = "https://www.alphavantage.co/query?function=LISTING_STATUS&state=delisted&apikey=" + key

    with requests.Session() as s:
        
        download = s.get(url)
        decodedContent = download.content.decode('utf-8')
        cr = csv.reader(decodedContent.splitlines(), delimiter=',')
        
        data = list(cr)

    return data


# Get Core Stock TIME_SERIES_INTRADAY
def getCoreStockIntraday(alphaVantageKeyPath, companyCode, yearMonth):
    
    key = getAlphaVantageKey(alphaVantageKeyPath)

    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + companyCode + "&interval=5min&month=" + yearMonth + "&outputsize=full&apikey=" + key
    
    with requests.Session() as s:
        
        download = s.get(url)
        response = download.json()
        
        metaData = response["Meta Data"]
        timeSeries = response["Time Series (5min)"]
        
        
        decodedContent = response("Time Series (5min)").content.decode('json')
        cr = csv.reader(decodedContent.splitlines(), delimiter=',')
        
        data = list(cr)   

    return data


# Checker, remove after
alphaVantageKeyPath = "keys/alphavantage.json"
storageAccountKeyPath = "keys/azurestorageaccount.json"

outputPath = "/Users/yessetzhaken/Library/CloudStorage/OneDrive-Personal/AlphaVantage/output/listings/"
companyCode = "IBM"
yearMonth = "2024-01"
dt = getCoreStockIntraday(alphaVantageKeyPath, companyCode, yearMonth)
print(dt)



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
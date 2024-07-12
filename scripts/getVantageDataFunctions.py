import requests
import json

def getStatement(company, key):
    
    url = "https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=" + company + "&apikey=" + key
    
    data = requests.get(url)
    return data.json()


import pathlib

companySymbol = "IBM"

path = pathlib.Path(__file__).parent.parent.joinpath("keys/data.json")
print(path) 

with open(path) as keys:
    keys = json.load(keys)

key = keys["accounts"][0]["key"]

df = getStatement(companySymbol, key)

outputPath = pathlib.Path(__file__).parent.parent.joinpath("output/income_statement/incomeStatement.json")

with open(outputPath, "w", encoding="utf-8") as f:
    json.dump(df, f)


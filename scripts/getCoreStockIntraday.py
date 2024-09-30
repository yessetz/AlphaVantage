import pandas as pd
import pathlib
import json
from getFundamentalDataFunctions import getCoreStockIntraday
from azureFunctions import storeFilesInAzureStorageAccount

alphaVantageKeyPath = "keys/alphavantage.json"
storageAccountKeyPath = "keys/azurestorageaccount.json"

outputPath = "/Users/yessetzhaken/Library/CloudStorage/OneDrive-Personal/AlphaVantage/output/listings/"
companyCode = "IBM"
yearMonth = "2024-01"
getCoreStockIntraday(alphaVantageKeyPath, companyCode, yearMonth)
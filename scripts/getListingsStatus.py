import pandas as pd
import pathlib
import json
from getFundamentalDataFunctions import getListingStatusActive, getListingStatuDelisted
from azureFunctions import storeFilesInAzureStorageAccount

# Request listing status and store in Data Lake
def getListingStatusActive(alphaVantageKeyPath, storageAccountKeyPath, outputPath):

    dataActive = getListingStatusActive(alphaVantageKeyPath)
    dataDelisted = getListingStatuDelisted(alphaVantageKeyPath)

    dfActive = pd.DataFrame(dataActive)
    dfDelisted = pd.DataFrame(dataDelisted)

    df = pd.concat([dfActive, dfDelisted]) 

    fileName = "listingStatus.csv"
    outputPath = pathlib.Path(__file__).parent.parent.joinpath(outputPath + fileName)

    df.to_csv(outputPath, index=False, header=False) 
    storeFilesInAzureStorageAccount(storageAccountKeyPath, "alphavantage/listingStatus", fileName, outputPath + fileName)


alphaVantageKeyPath = "keys/alphavantage.json"
storageAccountKeyPath = "keys/azurestorageaccount.json"

outputPath = "/Users/yessetzhaken/Library/CloudStorage/OneDrive-Personal/AlphaVantage/output/listings/"

getListingStatusActive(alphaVantageKeyPath, storageAccountKeyPath, outputPath)

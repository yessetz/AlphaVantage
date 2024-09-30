import pathlib
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


# Get Azure Storage Account API key by path 
def getAzureStorageAccountKey(path):
    
    azureStorageAccountKeyPath = pathlib.Path(__file__).parent.parent.joinpath(path)
    
    with open(azureStorageAccountKeyPath) as keys:
        keyObjects = json.load(keys)
    
    azureStorageAccountKey = keyObjects["accounts"][0]["key"]
    
    return azureStorageAccountKey


# Get Azure Storage Account Connection String key by path
def getAzureStorageAccountConnectionString(path):
    
    azureStorageAccountKeyPath = pathlib.Path(__file__).parent.parent.joinpath(path)
    
    with open(azureStorageAccountKeyPath) as keys:
        keyObjects = json.load(keys)
    
    azureStorageAccountConnectionString = keyObjects["accounts"][0]["connectionstring"]
    
    return azureStorageAccountConnectionString


# Get Azure Storage Account Connection String key by path
def getAzureStorageAccountName(path):
    
    azureStorageAccountKeyPath = pathlib.Path(__file__).parent.parent.joinpath(path)
    
    with open(azureStorageAccountKeyPath) as keys:
        keyObjects = json.load(keys)
    
    storageaccountname = keyObjects["accounts"][0]["storageaccountname"]
    
    return storageaccountname


def storeFilesInAzureStorageAccount(storageAccountKeyPath, containerName, fileName, filePath):
    
    connectionString = getAzureStorageAccountConnectionString(storageAccountKeyPath)

    # Initialize the BlobServiceClient
    blobServiceClient = BlobServiceClient.from_connection_string(connectionString)

    # Create a container client
    containerClient = blobServiceClient.get_container_client(containerName)

    # If the container doesn't exist, create it
    try:
        containerClient.create_container()
    except Exception as e:
        print(f"Container already exists or couldn't be created: {e}")

    # Create a blob client
    blobClient = blobServiceClient.get_blob_client(container=containerName, blob=fileName)

    # Upload the file
    with open(filePath, "rb") as data:
        blobClient.upload_blob(data, overwrite=True)

    print(f"File {filePath} uploaded to {fileName} in container {containerName}.")
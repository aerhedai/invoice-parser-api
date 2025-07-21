import json
from google.oauth2 import service_account
from google.cloud import documentai_v1 as documentai
from google.cloud import storage

def get_credentials_from_info(service_account_info: dict):
    return service_account.Credentials.from_service_account_info(service_account_info)

def get_documentai_client(credentials):
    return documentai.DocumentProcessorServiceClient(credentials=credentials)

def get_storage_client(credentials):
    return storage.Client(credentials=credentials)

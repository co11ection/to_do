from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
import requests
import os
from decouple import config

class GoogleSheets:
    SCOPES = [config('SCOPES')]
    SPREADSHEET_ID = config("SPREADSHEET_ID")
    service = None
    
    def __init__(self) -> None:
        creds = None
        
        if os.path.exists("token.json"):
            with open("token.json", "r") as file:
                creds_data = json.load(file)
            creds = Credentials.from_authorized_user_info(creds_data)
            
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as file:
                file.write(creds.to_json())
                
        self.service = build("sheets", "v4", credentials=creds)
        
    def readGoogleSheets(self, range):
        result = self.service.spreadsheets().values().get(spreadsheetId=self.SPREADSHEET_ID, range=range)
        values = result.get("values", [])
        return result
    
gs = GoogleSheets()
print(gs.readGoogleSheets('to_do!'))
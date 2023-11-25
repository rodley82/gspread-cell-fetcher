#! /usr/local/bin/python

import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

spreadsheet_name = os.getenv('SPREADSHEET_NAME')
cell_reference = os.getenv('CELL_REFERENCE')
worksheet_name = os.getenv('WORKSHEET_NAME')

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
if os.getenv('CREDENTIALS_JSON_FILE_PATH'):
  # Use the credentials file you downloaded when setting up the Google Sheets API
  credentials_json_file_path = os.getenv('CREDENTIALS_JSON_FILE_PATH')
  creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_json_file_path, scope)
else:
  # Build the credentials from individual env variables
  credentials_dict = {
    "type":                         "service_account",
    "project_id":                   os.getenv('SERVICE_ACCOUNT_PROJECT_ID'),
    "private_key_id":               os.getenv('SERVICE_ACCOUNT_PRIVATE_KEY_ID'),
    "private_key":                  os.getenv('SERVICE_ACCOUNT_PRIVATE_KEY'),
    "client_email":                 os.getenv('SERVICE_ACCOUNT_CLIENT_EMAIL'),
    "client_id":                    os.getenv('SERVICE_ACCOUNT_CLIENT_ID'),
    "auth_uri":                     os.getenv('SERVICE_ACCOUNT_AUTH_URI'),
    "token_uri":                    os.getenv('SERVICE_ACCOUNT_TOKEN_URI'),
    "auth_provider_x509_cert_url":  os.getenv('SERVICE_ACCOUNT_AUTH_PROVIDER_X509_CERT_URL'),
    "client_x509_cert_url":         os.getenv('SERVICE_ACCOUNT_CLIENT_X509_CERT_URL'),
    "universe_domain":              os.getenv('SERVICE_ACCOUNT_UNIVERSE_DOMAIN'),
  }
  creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)

client = gspread.authorize(creds)

# Replace 'Your spreadsheet name' with the name of your spreadsheet
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)

# Replace 'A1' with the cell you want to access
cell_value = sheet.acell(cell_reference).value

print(cell_value)

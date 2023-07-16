#! /usr/local/bin/python

import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

credentials_json_file_path = os.getenv('CREDENTIALS_JSON_FILE_PATH')
spreadsheet_name = os.getenv('SPREADSHEET_NAME')
cell_reference = os.getenv('CELL_REFERENCE')
worksheet_name = os.getenv('WORKSHEET_NAME')

# Use the credentials file you downloaded when setting up the Google Sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_json_file_path, scope)
client = gspread.authorize(creds)

# Replace 'Your spreadsheet name' with the name of your spreadsheet
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)

# Replace 'A1' with the cell you want to access
cell_value = sheet.acell(cell_reference).value

print(cell_value)

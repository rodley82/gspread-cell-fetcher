#! /usr/local/bin/python

import os
import sys
import getopt
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def printHelp():
  text = """  Fetchs the value of a single google spreadsheet cell and outputs to stdout
    usage: python cell-fetcher.py [options]
    options:
      -C, --credfile FILE_PATH                Path of the service account JSON credentials file
      -s, --spreadsheet "Spreadsheet name"    Name of the spreadsheet. Ex: "My spreadsheet"
      -c, --cell  "Cell reference"            Cell refernce. Ex: A1
      -w, --worksheet "Worksheet name"        Worksheet name. Ex: "work1"
      -h --help                               Prints this help

    The values of the above arguments can be defined in env variables:
    - CREDENTIALS_JSON_FILE_PATH
    - SPREADSHEET_NAME
    - CELL_REFERENCE
    - WORKSHEET_NAME
  """
  print(text)

def setArgs():
  spreadsheet_name = os.getenv('SPREADSHEET_NAME')
  cell_reference = os.getenv('CELL_REFERENCE')
  worksheet_name = os.getenv('WORKSHEET_NAME')
  cred_file = os.getenv('CREDENTIALS_JSON_FILE_PATH')
  opts, _args = getopt.getopt(sys.argv[1:], "s:c:C:w:h", ["spreadsheet=", "cell=", "credfile=" "worksheet=","help"])
  for opt, arg in opts:
    if opt in ("-s", "--spreadsheet"):
      spreadsheet_name = arg
    elif opt in ("-c", "--cell"):
      cell_reference = arg
    elif opt in ("-C", "--credfile"):
      cred_file = arg
    elif opt in ("-w", "--worksheet"):
      worksheet_name = arg
    elif opt in ("-h", "--help"):
      printHelp()
      exit(0)
  if spreadsheet_name == None:
    print("Spreadsheet name was not provided")
    exit(1)
  if cell_reference == None:
    print("cell reference was not provided")
    exit(1)
  if worksheet_name == None:
    print("worksheet name was not provided")
    exit(1)
  return spreadsheet_name, cell_reference, worksheet_name, cred_file

def fetchCell(spreadsheet_name, cell_reference, worksheet_name, cred_file=None):
  scope = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
  if cred_file!=None:
    # Use the credentials file you downloaded when setting up the Google Sheets API
    credentials_json_file_path = cred_file
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

def main():
  spreadsheet_name, cell_reference, worksheet_name, cred_file = setArgs()
  fetchCell(spreadsheet_name=spreadsheet_name, cell_reference=cell_reference, worksheet_name=worksheet_name, cred_file=cred_file)

if __name__ == "__main__":
  main()

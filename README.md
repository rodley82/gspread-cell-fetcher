# Cell Fetcher


## Execution

```
export CREDENTIALS_JSON_FILE_PATH="./service-account-creds.json"
export SPREADSHEET_NAME="File name on GDrive"
export CELL_REFERENCE="A1"
export WORKSHEET_NAME="JSON"
```

## Setting up

### Create project

- Create a new project on https://console.cloud.google.com/
- Click on "Enable API and Services"
- Search for "Google Sheets API"
- Click on ENABLE

### Create a service account

TODO

Download the credentials JSON file

### Grant access to service account from google spreadsheet

- Get the email from the json creds, example: kids-savings-service@kids-savings-XXXX.iam.gserviceaccount.com
- From inside the google sheets, add the email as reader


## TODO Ver oauth?

- Click on "Create credentials"
  - On Credential Type select "User data"
  - On Oauth Consent Screen fill required
  - On Scope, no need to select anything

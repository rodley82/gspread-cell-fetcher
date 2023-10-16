# Cell Fetcher


## Execution

Given a service account json file extract the values and set the proper environment variables

```
export SPREADSHEET_NAME="Kids Savings - Juana"
export CELL_REFERENCE="A1"
export WORKSHEET_NAME="JSON"

export SERVICE_ACCOUNT_PROJECT_ID="SERVICE_ACCOUNT_PROJECT_ID"
export SERVICE_ACCOUNT_PRIVATE_KEY_ID="SERVICE_ACCOUNT_PRIVATE_KEY_ID"
export SERVICE_ACCOUNT_PRIVATE_KEY="SERVICE_ACCOUNT_PRIVATE_KEY"
export SERVICE_ACCOUNT_CLIENT_EMAIL="SERVICE_ACCOUNT_CLIENT_EMAIL"
export SERVICE_ACCOUNT_CLIENT_ID="SERVICE_ACCOUNT_CLIENT_ID"
export SERVICE_ACCOUNT_AUTH_URI="SERVICE_ACCOUNT_AUTH_URI"
export SERVICE_ACCOUNT_TOKEN_URI="SERVICE_ACCOUNT_TOKEN_URI"
export SERVICE_ACCOUNT_AUTH_PROVIDER_X509_CERT_URL="SERVICE_ACCOUNT_AUTH_PROVIDER_X509_CERT_URL"
export SERVICE_ACCOUNT_CLIENT_X509_CERT_URL="SERVICE_ACCOUNT_CLIENT_X509_CERT_URL"
export SERVICE_ACCOUNT_UNIVERSE_DOMAIN="SERVICE_ACCOUNT_UNIVERSE_DOMAIN"
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

# Librerias de google sheet
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account



SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
# Escribe aquí el ID de tu documento:
SPREADSHEET_ID = '12g5ecg1J4PMFbRrlgNAZtFE3cxIkYf6DX5iJkAMmAC8'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

# Objeto
service = build('sheets', 'v4', credentials=creds)
#Objeto que controla y manipula la hoja desde Python
sheet = service.spreadsheets()

# Llamada a la api con los métodos values() y get()
# get() permite traer los datos
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Hoja 1!A1:C100').execute()



# Extraemos values del resultado
values = result.get('values',[])
print(values)
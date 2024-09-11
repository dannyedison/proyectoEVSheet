from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID = '12g5ecg1J4PMFbRrlgNAZtFE3cxIkYf6DX5iJkAMmAC8'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
fecha = input("Ingrese la fecha (DD-MM-AAAA): ")
hora = input("Ingrese la hora de entrada (HH:MM): ")

# Debe ser una matriz por eso el doble [[]]
values = [[nombre,fecha,hora]]
# Llamamos a la api
# append() permite insertar los datos al final de la tabla
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range='A1',
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")
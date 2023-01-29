import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope =["https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"]

credenciales = ServiceAccountCredentials.from_json_keyfile_name("client_secrets.json", scope)

cliente = gspread.authorize(credenciales)

sheet = cliente.open("PrimeraBase")

sheet.share("jonathanandres080@gmail.com", perm_type="user", role="writer")
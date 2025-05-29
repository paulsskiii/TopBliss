import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("pancake-data-marketing-b43adb3ca4e4.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet and get the value
sheet = client.open("Promotions for Automation").worksheet("Promotions")  # or use .worksheet("Sheet1")
reply_promotion1 = sheet.acell('A2').value

print("Promotion code:", reply_promotion1)

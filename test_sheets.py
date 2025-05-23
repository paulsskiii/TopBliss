import gspread
from oauth2client.service_account import ServiceAccountCredentials

# pip install gspread oauth2client datetime

# === Define the scope and load credentials ===
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("pancake-data-marketing-68273b87d10d.json", scope)
client = gspread.authorize(creds)

# === Open the Google Sheet ===
sheet = client.open("Pancake Bot logs").sheet1  # or use .worksheet("Sheet1") if needed

# === Test: Append a row ===
row = ["Dan Olarte", "2025-05-19", "Test message sent"]
# sheet.append_row(row)

print("✅ Successfully added test row to Google Sheet!")
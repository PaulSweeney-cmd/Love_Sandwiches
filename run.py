import gspread
from google.oauth2.service_account import Credentials

# API list
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Variables
CREDS = Credentials.from_service_account_file('creds.json')

# Parsing in the SCOPE api list variable
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Parsing in scoped credentials to the gspread authorize method
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Accessing the google spreadsheet
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# Accessing data in our worksheet
sales = SHEET.worksheet('sales')

# Using gspread method to get all values from the sales worksheet
data = sales.get_all_values()
print(data)


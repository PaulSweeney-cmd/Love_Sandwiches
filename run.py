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


def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please enter your sales data from the last market")
    print("Data should be six numbers, seperated by commas")
    print("For example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

    
get_sales_data()


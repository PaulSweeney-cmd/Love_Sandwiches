import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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



# Creating function to get data string from user
def get_sales_data():
    """
    Get sales figures input from the user
    """
    # Using a while loop to state that while the code is of true value
    while True:
        print("Please enter your sales data from the last market")
        print("Data should be six numbers, seperated by commas")
        print("For example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")

        # Using the .split() method splits the strings up at the commas, turning it in to a list value
        sales_data = data_str.split(",")

        # By using an if statement we are telling the code that if the values given are true then the code breaks from the loop
        if validate_data(sales_data):
            print("Data is valid!")
            break
    return sales_data




# Creating a function to validate the user data
def validate_data(values): 
    """
    Inside the try statement, convert all string values to integers, 
    Raises ValueError if strings cannot be converted to integers,
    or if there are more or less than six values
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True



# Function that inserts sales data as a new entry in to the sales worksheet
def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales_worksheet updated successfully!\n")





def update_surplus_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("surplus worksheet updated successfully!\n")







# Function to calculate the surplus data
def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
        - Positive surplus indicates waste
        - Negative surplus indicates extra made when stock sold out.
    """
    print("Calculating surplus data....\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    
# Creating a for loop with a zip method to iterate through two sets of data & produce the result needed
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data












def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num)for num in data]
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_surplus_worksheet(new_surplus_data)



print("Welcome To Love Sandwiches Data Automation!\n")
main()

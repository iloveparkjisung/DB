# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'kpop.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_option = ''
while menu_option != 'DONE':
    menu_option = input('Welcome to the Songs database \n\n'
                        'Where would you like to go? (please type in the letter)\n'
                        'B: All Nct and WayV members\n'
                        'C: Ateez\n'
                        'D: Enhypen\n'
                        'E: NCT\n'
                        'F: Seventeen\n'
                        'G: Straykids\n'
                        'H: Wayv\n'
                        'H: Wayv\n'
                        'done : Exit\n\nWhere would you like to go?: ')
    menu_option = menu_option.upper()
    if menu_option == 'A':
        print_query('All information')
    elif menu_option == 'B':
        print_query('Kpop')
    elif menu_option == 'C':
        print_query('RNB and pop')
    elif menu_option == 'D':
        print_query('Other Than Kpop and RNB')
    elif menu_option == 'E':
        print_query('Top 5 Kpop')
    elif menu_option == 'F':
        print_query('Music Length')
    elif menu_option == 'DONE':
        print('Thanks for using me')

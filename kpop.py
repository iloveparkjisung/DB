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
    menu_option = input('Welcome to the Kpop database \n\n'
                        'This menu contains information about Kpop:\n'
                        '   - Groups\n'
                        '   - Idols\n'
                        "   - Idol's stage name\n"
                        "   - Idol's real name\n"
                        "   - Idol's ages\n"
                        "   - Idol's Birthdays\n"
                        "   - Idol's Ethnicity\n"
                        "   - Idol's height\n"
                        "   - Idol's instagram\n\n"
                        'Please enter a letter that is from A - O to navigate throught the menu.\n'
                        'Please type "DONE" to exit the database\n'
                        'A: All Information\n'
                        'B: Ateez Members Names\n'
                        'C: Enhypen Members Names\n'
                        'D: NCT Members Names\n'
                        'E: Seventeen Members Names\n'
                        'F: Straykids Members Names\n'
                        'G: Wayv Members Names\n'
                        'H: Idols over 180cm\n'
                        'I: Not from Korea\n'
                        'J: Idols that were born in 2000 and after\n'
                        'K: Top 10 oldest\n'
                        'L: Top 10 tallest\n'
                        'M: Top 10 Youngest\n'
                        "N: All the lee's in kpop\n"
                        'O: Idols that are the age 25 and below\n'
                        'DONE: Exit\n\n'
                        'Where would you like to go? ')
    menu_option = menu_option.upper()
    if menu_option == 'A':
        print_query('All information')
    elif menu_option == 'B':
        print_query('Ateez Members Names')
    elif menu_option == 'C':
        print_query('Enhypen Members Names')
    elif menu_option == 'D':
        print_query('NCT Members Names')
    elif menu_option == 'E':
        print_query('Seventeen Members Names')
    elif menu_option == 'F':
        print_query('Straykids Members Names')
    elif menu_option == 'G':
        print_query('Wayv Members Names')
    elif menu_option == 'H':
        print_query('Idols over 180cm')
    elif menu_option == 'I':
        print_query('Not from Korea')
    elif menu_option == 'J':
        print_query('Idols that were born in 2000 and after')
    elif menu_option == 'K':
        print_query('Top 10 oldest')
    elif menu_option == 'L':
        print_query("Top 10 tallest")
    elif menu_option == 'M':
        print_query('Top 10 Youngest')
    elif menu_option == 'N':
        print_query("All the lee's in kpop")
    elif menu_option == 'O':
        print_query('Idols that are the age 25 and below')
    elif menu_option == 'DONE':
        print('Thanks for using me! \nPlease come again!!!')

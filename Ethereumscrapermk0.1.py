#! python3

# An Ethereum webscraper with email alert function
# Author: Tom Moore

import requests
import datetime
import time
import sys
import sqlite3
from pathlib import Path

# something to look at while running
print("Retrieving data from the interwebs...")
#get the currency price from Coinbase API
res = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=ETH')
res.raise_for_status()
#Convert the json file to a readable format
resjson = res.json()
#Go to nested dictionary of currency prices
currency_dict = resjson['data']['rates']
eth_price = currency_dict.get("GBP")

#Create an SQL lite database

eth_sql_db = "/var/eth_sql_dbv2.sqlite"
eth_price_table = 'eth_prices'	# name of the table to be created
date_field = 'date_column' # name of the column
price_field = 'price_column'
first_col_fieldtype = 'TEXT' # column data type
field_type = 'INTEGER'  # column data type



# Connecting to the database file
db_path = Path(eth_sql_db)
if db_path.is_file():
    print("File already exists, proceeding to update database")
else:
    conn = sqlite3.connect(eth_sql_db)
    c_cursor = conn.cursor()
    # Creating a new SQLite table with 2 columns
    c_cursor.execute('CREATE TABLE {tn} ({fc} {ftc}, {sc} {ft})'\
        .format(tn=eth_price_table, fc=date_field, ftc=first_col_fieldtype, sc=price_field, ft=field_type))
    # Committing changes and closing the connection to the database file
    conn.commit()
    conn.close()

#Update the database with daily ethereum price
def eth_price_update(today_date, eth_today):
    # Open the SQL database
    conn = sqlite3.connect(eth_sql_db)
    c_cursor = conn.cursor()
    # Insert the current ethereum price into the database
    c_cursor.execute("INSERT INTO eth_prices (date_column, price_column) VALUES (?, ?)", (today_date,eth_today))
    conn.commit()
    conn.close()

# Variables to store current time and the ethereum price
t_time = datetime.datetime.now()
eth_price_update(t_time,eth_price)

# check if Ethereum price has moved more than a certain percentage in the last day
def price_movement_func():
    # Open the SQL database
    conn = sqlite3.connect(eth_sql_db)
    c_cursor = conn.cursor()
    #select the current row and previous row
    yesterday_price = c_cursor.execute('SELECT price_column FROM eth_prices WHERE date_column < (?)', (datetime('now'))
    print(yesterday_price)
    current_price = print('this should be the current price')
    print(current_price)

price_movement_func()








#THIS IS TEST TEXT 

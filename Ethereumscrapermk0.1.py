#! python3

# An Ethereum webscraper with email alert function
# Author: Tom Moore

import requests
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
first_col_fieldtype = 'DATETIME'
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
    c_cursor.execute("INSERT INTO {tn} ({fc},{sc}) VALUES ({td}, {tp})".\
                    format(tn=eth_price_table, fc=date_field, sc=price_field, td=today_date, tp=eth_today))
    conn.commit()
    conn.close()
t_time =
eth_price_update(t_time,eth_price)


#THIS IS TEST TEXT 

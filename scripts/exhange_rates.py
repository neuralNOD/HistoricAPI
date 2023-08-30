# -*- encoding: utf-8 -*-

"""
Get Historical Exchange Rates Prices using Exhange Rates API

Exchange Rates API (https://exchangeratesapi.io/) has a free and a
paid plan of fetching historical exchange rates. The python code uses
the private API key to fetch historical rates for a list of required
currencies and store the same in a SQLite3 Database.

@author:  Debmalya Pramanik
@version: v0.0.1
"""

import requests
import pandas as pd

access_key = input("Enter Private API Key: ")

url = f"http://api.exchangeratesapi.io/v1/symbols?access_key={access_key}"
response = requests.get(url).json()

symbols = pd.DataFrame(data = {
    "CurrencyCode" : response["symbols"].keys(),
    "CountryName" : response["symbols"].values()
}).set_index("CurrencyCode")

symbols.to_excel("symbols.xlsx")

# historical time series
# Set API Endpoint and API key
endpoint = 'timeseries'


start_date = "2023-01-01"
end_date = "2023-06-30"
base = "USD"

# Construct the URL
url = f'http://api.exchangeratesapi.io/v1/{endpoint}?access_key={access_key}&start_date={start_date}&end_date={end_date}&base={base}' # base does not work

# Send a GET request using the requests library
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON response
    exchange_rates = response.json()

    # Access the exchange rate values, e.g. GBP
    print(exchange_rates['rates']['GBP'])
else:
    print('Error:', response.status_code)

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

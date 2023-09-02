# -*- encoding: utf-8 -*-

"""
Code Script to Process WorldGeographyDB

Geographical information (like country, states, city names, currency)
etc. is obtained from GitHub (check reference submodule). While the
data is pretty clean and descent, however some database optimization
is considered while storing the data. In addition, since the primary
keys are generated from within the data itself, thus the database can
be very easily replicated.

@author:  Debmalya Pramanik
@version: v0.0.1
"""

import os
import uuid
import pandas as pd

if __name__ == "__main__":
    ROOT = ".." # project source directory
    DATA = os.path.join(ROOT, "sources", "WorldGeographyDB", "csv")

    # ? Countries Master Table
    countries = pd.read_csv(os.path.join(DATA, "countries.csv"))
    countries = countries[["iso3", "name", "iso2", "region", "subregion", "capital", "currency", "tld", "latitude", "longitude"]]
    countries.columns = ["CountryID", "CountryName", "ISO2", "RegionName", "SubRegionName", "CapitalName", "CurrencyCode", "TLD", "CountryLatitude", "CountryLongitude"]

    # ? States Master Table
    states = pd.read_csv("../sources/WorldGeographyDB/csv/states.csv")
    states = states.merge(countries[["CountryID", "ISO2"]], left_on = "country_code", right_on = "ISO2")
    states["StateID"] = [str(uuid.uuid4()).upper() for _ in range(states.shape[0])]
    states = states[["StateID", "name", "CountryID", "state_code", "type", "latitude", "longitude"]]
    states.columns = ["StateID", "StateName", "CountryID", "StateCode", "StateType", "StateLatitude", "StateLongitude"]

    # ? Cities Master Table

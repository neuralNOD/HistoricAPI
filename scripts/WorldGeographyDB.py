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

import pandas as pd

if __name__ == "__main__":
    ROOT = ".." # project source directory
    DATA = os.path.join(ROOT, "sources", "WorldGeographyDB", "csv")

    countries = pd.read_csv(os.path.join(DATA, "countries.csv"))
    countries["CountryID"] = countries[["iso2", "iso3", "numeric_code"]].apply(
        lambda x : f"{x[0]}-{x[1]}-{str(x[2]).zfill(3)}", axis = 1
    )

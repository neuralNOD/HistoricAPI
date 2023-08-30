# -*- encoding: utf-8 -*-

"""
Fetch Currency Information from Wikipedia Table

Wikipedia lists out all the circulating, as well as, old currency
symbols in the standard ISO-4217 format. A list of cryptocurrencies
(non-standard) is also available.
"""

import wikipedia # pyright: ignore[reportMissingImports]
import pandas as pd

wikipedia.wikitable("https://en.wikipedia.org/wiki/ISO_4217")[0].to_excel("active.xlsx", index = False)

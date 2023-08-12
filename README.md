<h1 align = "center">Historic API</h1>

---

<div align = "justify">

The database and API consolidates various *open-source* and *proprietary* data sources to provide a 360° view about the world macroeconomics factors -
like conversion rates, commodity historical price, import-export price of various raw materials etc. Open-source data is available under [`./sources`](./sources)
directory (check [README.md](./sources/README.md) or check the 'submodules' referenced), while detailed information about proprietary data (including pricing, URL)
are mentioned in [PROPRIETARY_SOURCES.md](./sources/PROPRIETARY_SOURCES.md).

The database is designed such that all macro-economics factors for different country, states and cities are available globally, however many informations is related
to the Indian subcontinent. Global indicators may be integrated, but is currently not defined in the project scope. In addition,
[**`SQLite3`**](https://www.sqlite.org/index.html) is considered as the database, however given the [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/20/orm/) used
for models, views definations can be used to initialize different database.

</div>

# -*- encoding: utf-8 -*-

"""
An Interface Base Class

In a REST API, the table interface can be defined using the following standard HTTP methods mapped to CRUD operations, which are:

  1. GET: This method is used to retrieve data from the table. It can be used to fetch a single record or a collection of records. The GET method is typically associated with the SELECT operation in SQL.
  2. POST: This method is used to create new records in the table. It is used when you want to add a new entry to the table. The POST method is typically associated with the INSERT operation in SQL.
  3. PUT/PATCH: These methods are used to update existing records in the table. They are used when you want to modify the existing data in the table. The PUT method is typically associated with the UPDATE operation in SQL, while PATCH is used for partial updates.
  4. DELETE: This method is used to delete records from the table. It is used when you want to remove data from the table. The DELETE method is typically associated with the DELETE operation in SQL.

These HTTP methods can be mapped to specific endpoints in your API to represent the table interface. The base interface class is defined such that some operations like `get_all()` can be defined and controlled from one single place.

? `get_all()` : Typically, this function returns everything.
"""

from app.main import db
from app.main.models import * # noqa: F401, F403

class BaseInterface(object):
    """
    Base Interface Class Defination

    The base class is dynamically defined, and is thus can be
    inherited by any child class to return some certain values.
    """

    def __init__(self, table : object) -> None:
        self.table = table
    

    # * lambda function to fetch all records from a table
    get_all = lambda self : [row.__to_dict__() for row in self.table.query.all()]

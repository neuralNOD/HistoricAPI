# -*- encoding: utf-8 -*-

# define base model schema for all basic models

import decimal
import datetime as dt

class ModelClass(object):
    """Base Model Schema

    The base model class is defined under api-model class, 
    as this provides some functions helpful for development,
    representation and fetching records from `repository`.

    More information on Flask 2.x Customizing is available
    https://flask-sqlalchemy.palletsprojects.com/en/2.x/customizing/

    ```python
      class NewTableView(db.Model, ModelSchema):
        '''docstring'''

        __tablename__ = 'my_table'

        # define table attributes here

      class Repository(object):
        '''docstring'''

        def get(self) -> list:
            # since ModelClass has the following functionalities is also available

            return [record.__to_dict__() for record in NewTableView.query.all()]
    ```

    The base class exposes two dunder methods: `repr` and `str` for any
    class, that can be used by developers and any members of the class
    respectively for debugging purposes. In addition, the method `__to_dict__`
    can be used to replace schema design with a function call. However,
    this will always return all the columns for any particular table,
    and proper care has to be maintained if anything else is required.
    """


    def __repr__(self):
        # can be used by developers - for debugging
        # recomended to update the `repr(NewTableView)` as required
        return f"{self.__name__} | Columns: {self.__table__.columns}"


    def __str__(self):
        # can be used by anyone to understand the class
        # recomended to update the `str(NewTableView)` as required
        return f"Model Class: {self.__name__}"


    def __to_dict__(self):
        """
        Converts a Table View and Returns Parsed Results

        The views table only allows GET operations on a given table
        views. The table views are defined under `app/main/models/views`
        and each specific table is imported for further analysis. The
        method automatically parses data into `key: value` object.

        :type  records: array-like
        :param records: A set of records obtained using `query.all()`
                        functionality. This is a `row` type object, which
                        is JSON serialized in this function.

        :type  columns: array-like
        :param columns: List of column names, available as `.columns`
                        arguments on a table object.
        """
        
        di = dict()
        for c in self.__table__.columns:
            value_ = getattr(self, c.key)

            if isinstance(value_, decimal.Decimal):
                value_ = float(value_)
            elif isinstance(value_, dt.datetime):
                value_ = str(value_)
            else:
                pass

            di[c.key] = value_
        return di


    def __get_dtypes__(self):
        # returns { column-nane : data-type }
        return { c.key : str(c.type) for c in self.__table__.columns }


    def __get_column_names__(self):
        # returns list of all column names
        return [c.key for c in self.__table__.columns]

# -*- encoding: utf-8 -*-

from flask_restful import reqparse, Resource

from app.utils import ResponseFormatter

class BaseResource(Resource):
    """
    Base Resource Class for any API/Controller Objects

    The api/controller defines a set of crud operations on database,
    and often requires a set of same codes. The base method exposes
    such methods/attributes which is always required.
    """

    def __init__(self):
        # default constructor
        self.formatter  = ResponseFormatter() # format response

        # !! somehow `.add_argument(location = ('json', 'values'))`
        # is not accepting arguments from `from-data` or `params` unless
        # specifically said so using.
        # https://stackoverflow.com/a/72113212/6623589
        # https://flask-restful.readthedocs.io/en/latest/reqparse.html#argument-locations
        # https://flask-restful.readthedocs.io/en/latest/reqparse.html#parser-inheritance
        self.req_parser = reqparse.RequestParser() # parse incoming params


    @property
    def args(self):
        """Return all Request Parser Arguments"""

        return self.req_parser.parse_args()

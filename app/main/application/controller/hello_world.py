# -*- encoding: utf-8 -*-

# will be using flask_restful design
from flask_restful import Resource

from .._base_resource import BaseResource

class HelloWorld(BaseResource):
    """Hello-World Controller"""

    def __init__(self):
        super().__init__()

    def get(self):
        # dummy get using formatter
        return self.formatter.get("Hello-World")

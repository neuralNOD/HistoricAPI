# -*- encoding: utf-8 -*-

"""Base Case File for unittest Model"""

from unittest import TestCase

from .. import app

class BaseCase(TestCase):
    """Base Case Model for Testing"""

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        # define tearDown for database initialization
        # https://docs.python.org/3/library/unittest.html#setupclass-and-teardownclass
        pass

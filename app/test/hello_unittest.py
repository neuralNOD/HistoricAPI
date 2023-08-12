# -*- encoding: utf-8 -*-

from ._base_case import BaseCase

class HelloWorldTest(BaseCase):
    # check if the api is accesible

    @property
    def response(self):
        return self.app.get("/testing/")

    def test_hello_world_is_reachable(self):
        
        self.assertEqual(self.response.status_code, 200)


    def test_hello_world_has_correct_response(self):

        self.assertEqual(self.response.json["data"], "Hello-World")

from application import app
from flask import url_for
from flask_testing import TestCase
import application.routes
from unittest.mock import patch 


class TestBase(TestCase):
    def create_app(self):
        return app

class testa1_t3(TestBase):
    def test_get_a1(self):
        response = self.client.get(url_for('a1'))
        self.assert200(response) 
        self.assertNotIn(b'magic',response.data)

class testa1(TestBase):
    @patch('application.routes.choice', return_value='strength, intelligence')
    def test_get_a1(self, patched):
        response = self.client.get(url_for('a1'))
        self.assert200(response) 
        self.assertIn(b'intelligence',response.data)

class testa1_t2(TestBase):
    @patch('application.routes.choice', return_value='strength, intelligence')
    def test_get_a1(self, patched):
        response = self.client.get(url_for('a1'))
        self.assert200(response) 
        self.assertIn(b'strength',response.data)


        



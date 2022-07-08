from application import app
from flask import url_for
from flask_testing import TestCase
import requests_mock

# import application.routes
# from unittest.mock import patch 

class TestBase(TestCase):
    def create_app(self):
        return app

class testa1_t3(TestBase):
    def test_get_front(self):

        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/get_a1', text = "strength")
            m.get('http://service_3:5000/get_a2', text = "DC")
            m.post('http://service_4:5000/character', text = "SUPERMAN")
            response = self.client.get(url_for('index'))
            self.assert200(response) 
            self.assertIn(b'<b>superhero: </b> SUPERMAN',response.data)
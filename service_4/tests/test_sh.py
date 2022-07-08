from application import app
from flask import url_for
from flask_testing import TestCase
import application.routes
from unittest.mock import patch 

class TestBase(TestCase):
    def create_app(self):
        return app

class testsh_t1(TestBase):
    @patch('application.routes.choice', return_value ='BATMAN')
    def test_get_sh(self, patched):
        response = self.client.post(
            url_for('character'), 
            json = {'power':"intelligence", 'publisher':"DC"}
        )
        self.assert200(response) 
        self.assertIn(b'BATMAN',response.data)

class testsh_t2(TestBase):
    def test_get_sh2(self):
        response = self.client.post(
            url_for('character'), 
            json = {'power':"strength", 'publisher':"DC"}
        )
        self.assert200(response) 
        self.assertIn(b'green lantern',response.data)

class testsh_t3(TestBase):
    def test_get_sh3(self):
        response = self.client.post(
            url_for('character'), 
            json = {'power':"magic", 'publisher':"DC"}
        )
        self.assert200(response) 
        self.assertIn(b'nothing',response.data)

class testsh_t4(TestBase):
    @patch('application.routes.choice', return_value ='spider-man')
    def test_get_sh4(self, patched):
        response = self.client.post(
            url_for('character'), 
            json = {'power':"strength", 'publisher':"Marvel"}
        )
        self.assert200(response) 
        self.assertIn(b'spider-man',response.data)

class testsh_t5(TestBase):
    @patch('application.routes.choice', return_value ='IRONMAN')
    def test_get_sh5(self, patched):
        response = self.client.post(
            url_for('character'), 
            json = {'power':"intelligence", 'publisher':"Marvel"}
        )
        self.assert200(response) 
        self.assertIn(b'IRONMAN',response.data)
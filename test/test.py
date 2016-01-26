# -*- coding: utf-8 -*-

import unittest
from urllib.request import urlopen
from app import app
from flask.ext.testing import TestCase

class FunctionalTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8494
        return app
        
    def tearDown(self):
        app.teardown_request
        
    def test_server_is_up_and_running(self):
        response = urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)
        
        
    def test_something(self):
        rv = self.client.post("/post", data=dict(
            n='david',
            m='The first message',
        ), follow_redirects=True)
        self.assertIn(b'david', rv.data)
        self.assertIn(b'<p>The first message</p>', rv.data)
        
        re = self.client.post("/post", data=dict(
            n='我',
            m='大家好',
        ), follow_redirects=True)
        self.assertIn(b'hello'.encode(encoding='utf8'), re.data)
        self.assertIn(b'<p>Hello, \xcf\x89!</p>'.encode(encoding='utf8'), re.data)

             
if __name__ == '__main__':
    unittest.main()
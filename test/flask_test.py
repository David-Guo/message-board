# -*- coding: utf-8 -*-

import unittest
from urllib.request import urlopen
from app import app
from flask_testing import LiveServerTestCase

class FunctionalTest(LiveServerTestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8494
        return app
        
    def test_server_is_up_and_running(self):
        response = urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)
        
#    def test_add_message(self):
#        response = self.client.get("/")
        
    def test_something(self):
        rv = self.client.post("/post", data=dict(
            n='david',
            m='The first message',
        ), follow_redirects=True)
        self.assertIn(b'david', rv.data)
        self.assertIn(b'<p>The first message</p>', rv.data)
        
        
if __name__ == '__main__':
    unittest.main()
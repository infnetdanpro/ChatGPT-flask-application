import unittest
from flask import Flask
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.app.post('/login', data={'username': 'admin', 'password': 'secret'})
        self.assertEqual(response.status_code, 302)

    def test_welcome_page(self):
        response = self.app.get('/welcome')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Welcome, user!')

if __name__ == '__main__':
    unittest.main()

from flask_testing import TestCase
from flask import current_app, url_for
from app import app
import unittest


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_app_in_debug_mode(self):
        self.assertFalse(current_app.config['DEBUG'])


if __name__ == '__main__':
    unittest.main()

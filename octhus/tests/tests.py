import unittest
import sys
import os
sys.path.append(os.getcwd() + '/..')
from app import create_app


class TestHome(unittest.TestCase):

    def test_get(self):
    	app = create_app()
    	apptest = app.test_client()
    	response = apptest.get('/')
    	self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
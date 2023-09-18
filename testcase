import unittest
import json
from app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_version1_login_with_sentence(self):
        data = {'sentence': 'This is a test sentence for version 1'}
        response = self.app.post('/v1/login', json=data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertTrue('access_token' in result)
        self.assertTrue('random_array' in result)
        self.assertEqual(len(result['random_array']), 500)

    def test_version2_login_with_sentence(self):
        data = {'sentence': 'This is a test sentence for version 2'}
        response = self.app.post('/v2/login', json=data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertTrue('access_token' in result)
        self.assertTrue('random_array' in result)
        self.assertEqual(len(result['random_array']), 500)

    def test_missing_sentence(self):
        data = {}  # Missing 'sentence' key in the JSON data
        response = self.app.post('/v1/login', json=data)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['error'], 'Input sentence is required')

if __name__ == '__main__':
    unittest.main()



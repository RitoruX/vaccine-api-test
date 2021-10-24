import unittest
import requests
import json

API_URL = "https://wcg-apis.herokuapp.com/registration"

class TestRegistrationApi(unittest.TestCase):

    def sample_body(self, address = "Bangkok", birth_date = "2000-02-02", citizen_id = "1234567666666", name = "SuphanburiPrajantakham", occupation = "student", surname = "Wang"):
        body = {
        "address": f"{address}",
        "birth_date": f"{birth_date}",
        "citizen_id": f"{citizen_id}",
        "name": f"{name}",
        "occupation": f"{occupation}",
        "surname": f"{surname}"
        }
        return body

    def setUp(self):
        requests.delete("https://wcg-apis.herokuapp.com/citizen", data = self.sample_body())
        self.INVALID_ID = {'feedback': 'registration failed: invalid citizen ID'}
        self.SUCCESS = {"feedback": "registration success!"}
        self.MISSING_ATTRIBUTE = {'feedback': 'registration failed: missing some attribute'}

    def test_request_response(self):
        self.response = requests.get(API_URL)
        self.assertEqual(self.response.status_code, 200)

    def test_post_registration(self):
        self.response = requests.post(API_URL, self.sample_body())
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json(), self.SUCCESS)

    def test_post_registration_with_letter_id(self):
        self.response = requests.post(API_URL, self.sample_body(citizen_id = "RitoruX"))
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json(), self.INVALID_ID)
    
    def test_post_registration_with_not_complete_id(self):
        self.response = requests.post(API_URL, self.sample_body(citizen_id = "1234567890"))
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json(), self.INVALID_ID)

    def test_post_registration_with_empty_id(self):
        self.response = requests.post(API_URL, self.sample_body(citizen_id = ""))
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json(), self.MISSING_ATTRIBUTE)

    def test_post_registration_with_empty_address(self):
        self.response = requests.post(API_URL, self.sample_body(address = ""))
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json(), self.MISSING_ATTRIBUTE)

    def test_post_registration_with_empty_birth_date(self):
        self.response = requests.post(API_URL, self.sample_body(birth_date = ""))
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json(), self.MISSING_ATTRIBUTE)

    def test_post_registration_with_empty_name(self):
        self.response = requests.post(API_URL, self.sample_body(name = ""))
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json(), self.MISSING_ATTRIBUTE)

    def test_post_registration_with_empty_occupation(self):
        self.response = requests.post(API_URL, self.sample_body(occupation = ""))
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json(), self.MISSING_ATTRIBUTE)

    def test_post_registration_with_empty_surname(self):
        self.response = requests.post(API_URL, self.sample_body(surname = ""))
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json(), self.MISSING_ATTRIBUTE)

    def test_post_registration_with_numeric_name(self):
        self.response = requests.post(API_URL, self.sample_body(name = 1101))
        self.assertEqual(self.response.status_code, 200)
        self.assertNotEqual(self.response.json(), self.SUCCESS)

    def test_post_registration_with_numeric_surname(self):
        self.response = requests.post(API_URL, self.sample_body(surname = 1101))
        self.assertEqual(self.response.status_code, 200)
        self.assertNotEqual(self.response.json(), self.SUCCESS)

    def test_post_registration_with_numeric_occupation(self):
        self.response = requests.post(API_URL, self.sample_body(occupation = 1101))
        self.assertEqual(self.response.status_code, 200)
        self.assertNotEqual(self.response.json(), self.SUCCESS)

if __name__ == '__main__':
    unittest.main()
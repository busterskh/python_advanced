"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""


import unittest

import requests
from flask_wtf import FlaskForm
from hw1_registration import app, RegistrationForm



class FlaskrTestCase(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()


    def test_get_post(self):
        data = requests.get_data(as_text=True)
        call_func = '/registration'
        responce = self.app.post(call_func, data)
        self.assertRaises(responce)


if __name__ == '__main__':
    unittest.main()


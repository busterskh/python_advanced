"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.response = self._login(name='Petrov V.V.', email='testgmail.com', phone=9999999999, address='acsdc', index=123, comment='test')

    def _login(self, name, email, phone, address, index, comment):
        return self.app.post('/registration', data=dict(
                                              name=name,
                                              email=email,
                                              phone=phone,
                                              address=address,
                                              index=index,
                                              comment=comment
            ))

    def test_register(self):
        self.assertEqual(self.response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

import unittest
from module_02_linux.homework.hw_3_2 import app, storage


class TestFinancialAccounting(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_get_correct_add_spending(self):
        dict_len = len(storage.keys())
        date_and_money = '20220708/1000'
        responce = self.app.get(f'/add/{date_and_money}')
        self.assertTrue(len(storage) > dict_len)

    def test_get_correct_add_data(self):
        date_and_money = '220708/1000'
        responce = self.app.get(f'/add/{date_and_money}')
        self.assertIsNot('Запись внесена!', responce)

    def test_get_correct_calculate(self):
        responce = self.app.get('/calculate/2022')
        responce_text = responce.data.decode()
        self.assertTrue(str(sum(storage.values())) in responce_text)

    def test_get_correct_calculate_month(self):
        responce = self.app.get('/calculate/2022/01')
        responce_text = responce.data.decode()
        self.assertTrue(str(storage[('2022', '01', '31')]) in responce_text)

import unittest
from module_02_linux.homework.hw_3_3 import decrypt


class TestDectypt(unittest.TestCase):
    cipher_var = ['абрау...-кадабра', 'абра---------................кадабра',
                  'абраа..-.кадабра', 'абраа..-кадабра', 'абра-кадабра.']

    def test_get_correct_decrypt(self):
        flag = True
        for cipher_text in self.cipher_var:
            result = decrypt(cipher_text)
            if result != 'абра-кадабра':
                flag = False
        self.assertTrue(flag)

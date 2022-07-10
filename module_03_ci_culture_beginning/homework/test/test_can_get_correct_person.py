import unittest
from module_03_ci_culture_beginning.homework.person import Person


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.name = 'Bob'
        self.year_of_birth = 1987
        self.address = '221b, Baker street'
        self.bob = Person(name=self.name, year_of_birth=self.year_of_birth, address=self.address)

    def test_can_get_age(self):
        self.assertEqual(self.bob.get_age(), (2022 - 1987))

    def test_can_get_name(self):
        self.assertEqual(self.bob.get_name(), self.name)

    def test_can_get_address(self):
        self.assertEqual(self.bob.get_address(), self.address)

    def test_can_get_year_of_birth(self):
        self.assertEqual(self.bob.get_year_of_birth(), self.year_of_birth)

    def test_can_set_name(self):
        new_name = 'Not Bob'
        self.bob.set_name(name=new_name)
        self.assertEqual(self.bob.get_name(), new_name)

    def test_can_set_address(self):
        new_address = '1123, North avenue'
        self.bob.set_address(address=new_address)
        self.assertEqual(self.bob.get_address(), new_address)

    def test_can_set_year_of_birth(self):
        new_yob = 1999
        self.bob.set_yob(year_of_birth=new_yob)
        self.assertEqual(self.bob.get_year_of_birth(), new_yob)

    def test_can_get_correct_is_homeless(self):
        need_list = [False, True]
        result_list = [self.bob.is_homeless()]
        self.bob.set_address(address='')
        result_list.append(self.bob.is_homeless())
        self.assertListEqual(need_list, result_list)

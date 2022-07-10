import datetime


class Person:
    def __init__(self, name, year_of_birth, address=''):
        self.__name = name
        self.__yob = year_of_birth
        self.__address = address

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.get_year_of_birth()

    def get_year_of_birth(self):
        return self.__yob

    def set_yob(self, year_of_birth):
        self.__yob = year_of_birth

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def is_homeless(self):
        '''
        returns True if address is not set, false in other case
        '''
        return True if self.get_address() == '' else False

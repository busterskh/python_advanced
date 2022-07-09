import datetime
import unittest

from module_02_linux.homework.hw_2_4_hello_world_with_day import app


class TestHelloWorldWithDay(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_username(self):
        username = 'username'
        responce = self.app.get(self.base_url + username)
        responce_text = responce.data.decode()
        self.assertTrue(username in responce_text)

    def test_can_get_correct_weekdate(self):
        username = 'username'
        day_week = ['понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья']
        weekdate = day_week[datetime.datetime.today().weekday()]
        responce = self.app.get(self.base_url + username)
        responce_text = responce.data.decode()
        self.assertTrue(weekdate in responce_text)

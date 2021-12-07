import unittest

from faker import Faker

from .model_test import ModelTest


class TestPlay(ModelTest):

    faker = Faker()

    @classmethod
    def setUpClass(cls):
        super(TestPlay, cls).setUpClass()

        from mib.models import lottery
        cls.user = lottery

    @staticmethod
    def assertPlayEquals(value, expected):
        t = unittest.FunctionTestCase(TestPlay)
        t.assertEqual(value.lottery_number, expected.lottery_number)

    @staticmethod
    def generate_random_play():
        number = TestPlay.faker.random_int(1,100)

        from mib.models import Lottery

        play = Lottery(
            lottery_number=number
        )

        return play
    
    def test_set_number(self):
        play = TestPlay.generate_random_play()
        number = self.faker.random_int(1,100)
        play.set_number(number)
        self.assertEqual(number, play.lottery_number)

from faker import Faker

from .dao_test import DaoTest


class TestLotteryManager(DaoTest):
    faker = Faker()

    @classmethod
    def setUpClass(cls):
        super(TestLotteryManager, cls).setUpClass()
        from tests.models.test_play import TestPlay
        cls.test_play = TestPlay
        from mib.dao import lottery_manager
        cls.lottery_manager = lottery_manager.LotteryManager

    def test_crud(self):
        for _ in range(0, 10):
            play = self.test_play.generate_random_play()
            self.lottery_manager.create_lottery_play(lottery=play)
            play1 = self.lottery_manager.retrieve_by_id(play.id)
            self.test_play.assertPlayEquals(play1, play)
            play.set_number(self.faker.random_int(1,100))
            self.lottery_manager.update_lottery_play(lottery=play)
            play1 = self.lottery_manager.retrieve_by_id(play.id)
            self.test_play.assertPlayEquals(play1, play)
            self.lottery_manager.delete_lottery_play(lottery=play)

    def test_retried_by_number(self):
        base_play = self.test_play.generate_random_play()
        self.lottery_manager.create_lottery_play(lottery=base_play)
        retrieved_play = self.lottery_manager.retrieve_by_number(lottery_number=base_play.lottery_number)
        self.test_play.assertPlayEquals(base_play, retrieved_play)

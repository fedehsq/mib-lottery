from .view_test import ViewTest
from faker import Faker

class TestLottery(ViewTest):
    faker = Faker('it_IT')

    @classmethod
    def setUpClass(cls):
        super(TestLottery, cls).setUpClass()

    ''' def test_delete_user(self):
        user = self.login_test_user()
        rv = self.client.delete('/user/%d' % user.id)
        assert rv.status_code == 202
    '''
    @staticmethod
    def generate_random_play():
        number = TestLottery.faker.random_int(1,100)

        from mib.models import Lottery
        
        play = Lottery(
            lottery_number=number
        )
        
        return play

    def test_check_play(self):
        # get a non-existent play
        rv = self.client.get('/lottery/exist/0')
        assert rv.status_code == 404
        # create a play and check that exist
        from mib.dao.lottery_manager import LotteryManager

        play = self.generate_random_play()
        LotteryManager.create_lottery_play(play)
        rv = self.client.get('/lottery/exist/%s' % play.id)
        assert rv.status_code == 200

    def test_create_lottery_play(self):
        data = {
            'id' : TestLottery.faker.random_int(),
            'lottery_number': TestLottery.faker.random_int(1,100)
        }
        rv = self.client.post('/lottery', json = data)
        assert rv.status_code == 201
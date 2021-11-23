from mib.dao.manager import Manager
from mib.models.lottery import Lottery


class LotteryManager(Manager):

    @staticmethod
    def create_lottery_play(lottery: Lottery):
        Manager.create(lottery=lottery)

    @staticmethod
    def retrieve_by_id(id_):
        Manager.check_none(id=id_)
        return Lottery.query.get(id_)

    @staticmethod
    def retrieve_by_number(lottery_number):
        Manager.check_none(lottery_number=lottery_number)
        return Lottery.query.filter(Lottery.lottery_number == lottery_number).first()

    @staticmethod
    def update_lottery_play(lottery: Lottery):
        Manager.update(lottery=lottery)

    @staticmethod
    def delete_lottery_play(lottery: Lottery):
        Manager.delete(lottery=lottery)

    @staticmethod
    def delete_lottery_play_by_id(id_: int):
        lottery_play = LotteryManager.retrieve_by_id(id_)
        LotteryManager.delete_lottery_play(lottery_play)

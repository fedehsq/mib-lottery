import unittest


class ViewTest(unittest.TestCase):
    """
    This class should be implemented by
    all classes that tests resources
    """
    client = None

    @classmethod
    def setUpClass(cls):
        from mib import create_app
        app = create_app()
        cls.client = app.test_client()

        from tests.models.test_play import TestPlay
        cls.test_play = TestPlay

        from mib.dao.lottery_manager import LotteryManager
        cls.lottery_manager = LotteryManager()

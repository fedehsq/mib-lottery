from mib import db, create_app, create_celery
from random import seed, randint
from celery import Celery
from celery.schedules import crontab
from mib.models.lottery import Lottery
from datetime import timedelta
import requests
from mib.dao.lottery_manager import LotteryManager


BACKEND = BROKER = 'redis://localhost:6379'
celery = Celery(__name__, backend=BACKEND, broker=BROKER)

flask_app = create_app()
app = create_celery(flask_app)

try:
    import mib.tasks
except ImportError:
    raise RuntimeError('Cannot import celery tasks')

celery.conf.beat_schedule = {
    "lottery-game":{
        "task": "lottery_task",
        "schedule": timedelta(days = 30)     #day_of_month="1" for a monthly lottery, 60 seconds to do tests 
    }
}

@celery.task(name = 'lottery_task')
def lottery():
    with app.app_context():
        #generate random number between 1-100
        seed()
        number_extract = randint(1,100)
        #number_extract = 10
        plays = db.session.query(Lottery)
        for play in plays:
            if play.lottery_number == number_extract:
                url = "http://localhost:5001/user/updatepoints/%s" % str(play.id)
                requests.post(url, timeout=15)
                print("vinto")
            #delete the user's lottery play for the next extraction
            LotteryManager.delete_lottery_play(play)
        db.session.commit()
        return "lottery extraction done!"
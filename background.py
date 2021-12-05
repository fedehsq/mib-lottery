from mib import create_app
from random import seed, randint
from celery import Celery
from celery.signals import worker_ready
from datetime import timedelta
import requests


APP = None

BACKEND = BROKER = 'redis://lottery_ms_redis-server:6379'
celery = Celery(__name__, backend=BACKEND, broker=BROKER)
#flask_app = create_app()
#app= db.init_app(flask_app)
#app=flask_app
#app = create_celery(flask_app)

'''
try:
    import mib.tasks
except ImportError:
    raise RuntimeError('Cannot import celery tasks')
'''

celery.conf.beat_schedule = {
    "lottery-game":{
        "task": "lottery_task",
        "schedule": timedelta(seconds = 30)     #day_of_month="1" for a monthly lottery, 60 seconds to do tests 
    }
}

@celery.task(name = 'lottery_task')
def lottery():
    global APP
    if not APP:
        return "not app"
    with APP.app_context():
        from mib.models.lottery import Lottery, db
        from mib.dao.lottery_manager import LotteryManager
        #generate random number between 1-100
        seed()
        number_extract = randint(1,100)
        #print(number_extract)
        #number_extract = 10
        plays = db.session.query(Lottery)
        """url = "http://users_ms_worker:5000/user/updatepoints/%s" % str(1)
        requests.put(url, json = {'user/updatepoints' : 'increase'},
                timeout=15)"""
        if plays is None:
            return "no play found"
        for play in plays:
            if play.lottery_number == number_extract:
                url = "http://users_ms_worker:5000/user/updatepoints/%s" % str(play.id)
                requests.put(url, json = {'user/updatepoints' : 'increase'},
                timeout=15)
                print("vinto")
            #delete the user's lottery play for the next extraction
            LotteryManager.delete_lottery_play(play)
        db.session.commit()
        return {"lottery extraction done!": number_extract}


@worker_ready.connect
def start(sender, **k):
    with sender.app.connection() as conn:
        sender.app.send_task('background.initialize',
            connection = conn)

@celery.task
def initialize():
    global APP
    # lazy init
    if APP is None:
        app = create_app()
        APP = app
    else:
        app = APP
    return []
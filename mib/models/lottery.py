from mib import db


class Lottery(db.Model):
    """Representation of Lottery model."""

    # The name of the table that we explicitly set
    __tablename__ = 'Lottery'

    # A list of fields to be serialized
    SERIALIZE_LIST = ['id', 'lottery_number']

    # All fields of lottery
    id = db.Column(db.Integer, primary_key = True)
    lottery_number = db.Column(db.Integer, default = 0)

    def __init__(self, *args, **kw):
        super(Lottery, self).__init__(*args, **kw)
        self.lottery_number = 0

    def set_number(self, lottery_number):
        self.lottery_number = lottery_number

    def serialize(self):
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])

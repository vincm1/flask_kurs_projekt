from sportmeetup import db, bcrypt
from datetime import datetime

class Meetup(db.Model):

    __tablename__ = "meetups"

    id = db.Column(db.Integer, primary_key=True)
    ersteller = db.Column(db.Integer, db.ForeignKey('users.id'))

    creation_date = db.Column(db.DateTime, default=datetime.now)
    event_date = db.Column(db.DateTime, nullable=False)
    sport = db.Column(db.String(100), nullable=False)
    place = db.Column(db.String(400), nullable=False)
    adress = db.Column(db.String(400), nullable=False)
    description = db.Column(db.Text())

    def __init__(self, ersteller, event_date, sport, place, adress, description):
        self.ersteller = ersteller,
        self.event_date = event_date,
        self.sport = sport,
        self.place = place,
        self.adress = adress,
        self.description = description,
    
    def __repr__(self):
        f"The meetup {self.place} in {self.place} {self.adress} wurde erstellt"

from sportmeetup import db, bcrypt
from flask_login import UserMixin
from sportmeetup import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), unique=True, nullable=False)
    # profile_picture = db.Column(db.String(100), nullable=True, default='default_profile_pic.png')
    user_email = db.Column(db.String(100), unique=True, nullable=False)
    user_passwort = db.Column(db.String(80), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.now)

    def check_passwort(self, passwort):
        return bcrypt.check_password_hash(self.user_passwort, passwort)

    # classmethods gehören zu einer Klasse, aber sind nicht verbunden mit Class Instanzen
    @classmethod
    def create_user(cls, username, email, passwort):
        user = cls(user_name=username,
                    user_email=email,
                    user_passwort=bcrypt.generate_password_hash(passwort).decode('utf-8'))
        
        db.session.add(user)
        db.session.commit()
        return user

    def __repr__(self):
        return f"Username: {self.username}"


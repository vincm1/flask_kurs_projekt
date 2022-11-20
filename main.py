from sportmeetup import create_app, db
from sportmeetup.users.models import User
from sportmeetup.meetups.models import Meetup

if __name__ == '__main__':
    flask_app = create_app('dev')
    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name="MaxMuster").first():
            User.create_user(username="MaxMuster", email="MaxMuster@gmail.com", passwort='secret')
    flask_app.run()
    flask_app.run(debug=True)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from flask_login import current_user
from sportmeetup.users.models import User

class MeetupForm(FlaskForm):
    event_date = DateField('Datum', validators=[DataRequired()])
    sport = StringField('Sportart', validators=[DataRequired()])
    place = StringField('Sportplatz', validators=[DataRequired()] )
    adress = StringField('Adresse', validators=[DataRequired()])
    description = TextAreaField('Beschreibung', validators=[DataRequired()])
    submit = SubmitField('Meetup hinzufügen')

    
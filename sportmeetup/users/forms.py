from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from sportmeetup.users.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(3,10, message="Zwischen 3 & 10 Zeichen")])
    email = StringField('Email', validators=[DataRequired(),Email()])
    passwort = PasswordField('Passwort', validators=[DataRequired(), Length(8), EqualTo('confirm_pw', message="Passwörter stimmen nicht überein!")] )
    confirm_pw = PasswordField('Passwort bestätigen', validators=[DataRequired()])
    submit = SubmitField('Anmelden')

    def check_name(form, field):
        name = User.query.filter_by(username=field.data).first()
        if name:
            raise ValidationError('Nutzername bereits vorhanden!')

    def check_email(form, field):
        email = User.query.filter_by(user_email=field.data).first()
        if email:
            raise ValidationError('Email bereits vorhanden!')

class LoginForm(FlaskForm):
    email = StringField('Nutzer-Email', validators=[DataRequired(), Email()])
    passwort = PasswordField('Passwort', validators=[DataRequired()])
    submit = SubmitField('Anmelden')

class EditProfileForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    user = StringField('Username', validators=[DataRequired()])
    picture = FileField('Profilbild', validators=[FileAllowed(['jpg','png','svg'])])
    submit = SubmitField('Profil aktualisieren')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has already been registered!")

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Your username has already been registered!")
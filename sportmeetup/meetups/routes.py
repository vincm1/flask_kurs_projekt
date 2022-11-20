from flask import render_template ,flash, request, redirect, url_for
from flask import Blueprint
from sportmeetup import login_manager, db
from flask_login import login_user, logout_user, login_required, current_user
from sportmeetup.meetups.forms import MeetupForm
from sportmeetup.users.models import User
from sportmeetup.meetups.models import Meetup

meetups = Blueprint('meetups', __name__)

@meetups.route('/meetups', methods=["GET"])
def all_meetups():
    
    meetups = Meetup.query.all()

    return render_template('meetups.html', meetups=meetups)

@meetups.route('/meetup_hinzufügen', methods=["GET","POST"])
def add_meetup():
    
    form = MeetupForm()

    if form.validate_on_submit():
        meetup = Meetup(ersteller=current_user.id, event_date=form.event_date.data, sport=form.sport.data,
                    place=form.place.data, adress=form.adress.data, description=form.description.data)
        db.session.add(meetup)
        db.session.commit()
        flash("Meetup hinzugefügt")
        return redirect(url_for('meetups.all_meetups'))

    return render_template('add_meetup.html', form=form)



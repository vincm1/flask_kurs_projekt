from flask import render_template ,flash, request, redirect, url_for
from flask import Blueprint
from sportmeetup import login_manager, db
from flask_login import login_user, logout_user, login_required, current_user
from sportmeetup.users.forms import RegistrationForm, LoginForm, EditProfileForm
from sportmeetup.users.models import User

users = Blueprint('users', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@users.route('/login', methods=["GET", "POST"])
def do_login_user():

    form = LoginForm()
    
    if form.validate_on_submit():
        
        user=User.query.filter_by(user_email=form.email.data).first()
        
        if not user or not user.check_passwort(form.passwort.data):
            flash('Falsche Anmeldedaten!')
            redirect(url_for('users.do_login_user'))
        
        login_user(user)
        return redirect(url_for('core.landing'))

    return render_template('login.html', form=form)

@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))

@users.route('/anmeldung', methods=["GET", "POST"])
def register_user():

    form = RegistrationForm()

    if form.validate_on_submit():
        User.create_user(
            username = form.username.data,
            email = form.email.data,
            passwort = form.passwort.data)
        flash('Anmeldung erfolgreich!')
        #return redirect(url_for('users.do_login_user'))
    
    return render_template('anmeldung.html', form=form)

@users.route('/account', methods=["GET","POST"])
@login_required
def edit_profile():

    form = EditProfileForm()

    if form.validate_on_submit():
        print(form)
        #if form.picture.data:
        username = current_user.username
        print(username)
        print(form.picture.data)
        pic = add_profile_pic(form.picture.data,username)
        current_user.profile_picture = pic
        print(current_user.profile_picture)
        
        current_user.username = form.user.data
        current_user.email = form.email.data

        db.session.commit()

        flash('Profil erfolgreich bearbeitet!')

    elif request.method == 'GET':
        form.user.data = current_user.username
        form.email.data = current_user.user_email
    
    profile_picture = url_for('static', filename='profile_pics/'+ str(current_user.profile_picture))
    return render_template('profile.html', form=form, profile_picture=profile_picture)



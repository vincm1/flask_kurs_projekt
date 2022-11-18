from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
@core.route('/home')
def landing():
    return render_template('landing.html')

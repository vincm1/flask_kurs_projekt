import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap= Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_login_user'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()

def create_app(config_type): #dev, test, prod
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(),'config',config_type + '.py')
    app.config.from_pyfile(configuration)

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from sportmeetup.core.routes import core
    app.register_blueprint(core)

    from sportmeetup.users.routes import users
    app.register_blueprint(users)

    return app
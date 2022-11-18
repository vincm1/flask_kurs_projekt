import os
from flask import Flask

app = Flask(__name__)

from sportmeetup.core.routes import core

app.register_blueprint(core)

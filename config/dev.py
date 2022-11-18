import os

DEBUG = True
secret_key_env = os.environ.get('SECRET_KEY')
SECRET_KEY = secret_key_env

db_user_env = os.environ.get('DB_USER')
db_pw_env = os.environ.get('DB_PW')

SQLALCHEMY_DATABASE_URI = f'postgresql://{db_user_env}:{db_pw_env}@localhost/sportmeetup_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
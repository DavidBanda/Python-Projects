from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e7e4b44cfa377d362eae765337be7361872b62bb7fc0bf2fea25f4d88222291f'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASS")}' \
    f'@localhost/proyecto_visitas'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes


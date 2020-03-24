from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_visitas.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Por favor ingrese a su cuenta para acceder a este recurso'

from flask_visitas.users.routes import users
from flask_visitas.solicitudes.routes import solicitudes
from flask_visitas.main.routes import main

app.register_blueprint(users)
app.register_blueprint(solicitudes)
app.register_blueprint(main)

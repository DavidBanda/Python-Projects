from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_visitas.config import Config
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
login_manager = LoginManager(app)

login_manager.login_view = 'usuarios.login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Por favor ingrese a su cuenta para acceder a este recurso'

from flask_visitas.usuarios.routes import usuarios
from flask_visitas.solicitudes.routes import solicitudes
from flask_visitas.principal.routes import principal

app.register_blueprint(usuarios)
app.register_blueprint(solicitudes)
app.register_blueprint(principal)

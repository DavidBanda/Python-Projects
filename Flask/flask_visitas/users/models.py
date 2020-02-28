from flask_visitas import db, login_manager
from flask_login import UserMixin

ACCESS = {
    0: 'Profesor',
    1: 'Jefe de Departamento',
    2: 'Subdirector',
    3: 'Gestion Tecnologica',
    4: 'Admin'
}


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    access = db.Column(db.Integer, nullable=False, default=0)
    image_file = db.Column(db.String(30), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def type_of_user(self):
        return ACCESS[self.access]

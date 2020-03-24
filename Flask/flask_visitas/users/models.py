from flask_visitas import db, login_manager
from flask_login import UserMixin
from flask_visitas.users.dict_choices import ACCESS


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    access = db.Column(db.Integer, nullable=False, default=0)
    image_file = db.Column(db.String(30), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    visitas = db.relationship('Visitas', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def type_of_user(self):
        return ACCESS[self.access]

    def get_username(self):
        all_name = self.name.split()
        if len(all_name) == 3:
            return f'{all_name[0]} {all_name[1]}'
        return f'{all_name[0]} {all_name[2]}'







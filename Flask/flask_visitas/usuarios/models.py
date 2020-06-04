from itsdangerous import TimedJSONWebSignatureSerializer as TimeSerializer
from flask_visitas import db, login_manager, app
from flask_login import UserMixin
from flask_visitas.usuarios.dict_choices import access, department


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.Integer, nullable=False, default=0)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    access = db.Column(db.Integer, nullable=False, default=0)
    image_file = db.Column(db.String(30), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    visitas = db.relationship('Visitas', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

    @staticmethod
    def getJefeDepartamento():
        jefes = User.query.filter_by(access=1).all()
        storeJefesChoices = []
        for i, jefe in enumerate(jefes):
            storeJefesChoices.append((f'{jefe.name}', f'{jefe.name}'))
        return storeJefesChoices if len(storeJefesChoices) > 0 else [(f'{0}', 'Inexistente')]

    @staticmethod
    def getSubdirector():
        subs = User.query.filter_by(access=2).all()
        storeSubdirectores = []
        for i, sub in enumerate(subs):
            storeSubdirectores.append((f'{i}', f'{sub.name}'))
        return storeSubdirectores if len(storeSubdirectores) > 0 else [(f'{0}', 'Inexistente')]

    def type_of_user(self):
        return access[self.access]

    def get_department(self):
        return department[self.department]

    def get_username(self):
        all_name = self.name.split()
        if len(all_name) <= 3:
            return f'{all_name[0]} {all_name[1]}'
        return f'{all_name[0]} {all_name[2]}'

    def get_reset_token(self, expires_seconds=300):
        s = TimeSerializer(app.config['SECRET_KEY'], expires_seconds)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = TimeSerializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']

        except:
            return None

        return User.query.get(user_id)







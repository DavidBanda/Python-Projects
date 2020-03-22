from flask_visitas import db
from datetime import datetime

status = {
    0: 'Espera',
    1: 'Aceptado',
    2: 'Rechazado',
}


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status_departamento = db.Column(db.Integer, nullable=False, default=0)
    status_subdirector = db.Column(db.Integer, nullable=False, default=0)
    status_gestion = db.Column(db.Integer, nullable=False, default=0)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"

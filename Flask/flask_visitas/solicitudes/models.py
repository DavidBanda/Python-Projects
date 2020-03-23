from flask_visitas import db
from datetime import datetime

status = {
    0: 'Espera',
    1: 'Aceptado',
    2: 'Rechazado',
}

periodo = {
    0: 'enero - junio',
    1: 'agosto - diciembre',
}


class Visitas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_tec = db.Column(db.String(100), nullable=False, default='Instituto Tecnológico de Chihuahua')
    name_sub = db.Column(db.String(100), nullable=False, default='Subdirección Académica')
    fecha_elaboracion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    periodo_escolar = db.Column(db.String(50), nullable=False)
    nombre_docente = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    status_jefe_departamento = db.Column(db.Integer, nullable=False, default=0)
    status_subdirector = db.Column(db.Integer, nullable=False, default=0)
    status_gestion_tecnologica = db.Column(db.Integer, nullable=False, default=0)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.fecha_elaboracion}')"

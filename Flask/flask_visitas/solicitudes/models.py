from flask_visitas import db
from datetime import datetime
from flask_visitas.solicitudes.dict_choices import status, periodo, \
    carrera, turno


class Visitas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_tec = db.Column(db.String(50), nullable=False)
    name_sub = db.Column(db.String(50), nullable=False)
    fecha_elaboracion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    periodo_escolar = db.Column(db.Integer, nullable=False)
    no_visitas = db.Column(db.Integer, nullable=False)
    nombre_empresa = db.Column(db.String(30), nullable=False)
    ciudad = db.Column(db.String(30), nullable=False)
    objetivo = db.Column(db.Text, nullable=False)
    area_visita = db.Column(db.String(30), nullable=False)
    fecha_visita = db.Column(db.DateTime, nullable=False)
    turno = db.Column(db.Integer, nullable=False)
    carrera = db.Column(db.Integer, nullable=False)
    semestre = db.Column(db.Integer, nullable=False)
    total_estudiantes = db.Column(db.Integer, nullable=False)
    nombre_asignatura = db.Column(db.String(30), nullable=False)
    unidad_asignatura = db.Column(db.Integer, nullable=False)
    nombre_jefe_departamento = db.Column(db.String(30), nullable=False)
    nombre_subdirector = db.Column(db.String(30), nullable=False)
    status_jefe_departamento = db.Column(db.Integer, nullable=False, default=0)
    status_subdirector = db.Column(db.Integer, nullable=False, default=0)
    status_gestion_tecnologica = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.fecha_elaboracion}')"

    def get_carrera(self):
        return carrera[self.carrera]

    def get_turno(self):
        return turno[self.turno]

    def get_periodo(self):
        return periodo[self.periodo]

    def get_status(self):
        if self.status_jefe_departamento == 2 or self.status_subdirector == 2 \
                or self.status_gestion_tecnologica == 2:
            return 2
        elif self.status_jefe_departamento == 1 and self.status_subdirector == 1 \
                and self.status_gestion_tecnologica == 1:
            return 1
        else:
            return 0


from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, TextAreaField, SelectField,
                        IntegerField, DateField)
from wtforms.validators import DataRequired, Length
from flask_visitas.solicitudes.choices import periodo, carrera, turno


class VisitaForm(FlaskForm):
    name_tec = StringField('Nombre del Tecnológico', validators=[DataRequired(), Length(min=5, max=50)])
    name_sub = StringField('Nombre de Subdirección', validators=[DataRequired(), Length(min=5, max=50)])
    periodo_escolar = SelectField('Periodo Escolar', validators=[DataRequired()], choices=periodo)
    no_visitas = IntegerField('Numero consecutivo de visitas', validators=[DataRequired()])
    nombre_empresa = StringField('Nombre de la Empresa', validators=[DataRequired(), Length(min=5, max=30)])
    ciudad = StringField('Ciudad', validators=[DataRequired(), Length(min=5, max=30)])
    objetivo = TextAreaField('Objetivo de la visita', validators=[DataRequired()])
    area_visita = StringField('Area a visitar en la empresa', validators=[DataRequired(), Length(min=5, max=30)])
    fecha_visita = DateField('Fecha de visita', format='%d/%m/%Y',
                                validators=[DataRequired('Ingrese un formato valido')])
    turno = SelectField('Turno', validators=[DataRequired()], choices=turno)
    carrera = SelectField('Carrera', validators=[DataRequired()], choices=carrera)
    semestre = IntegerField('Semestre', validators=[DataRequired()])
    total_estudiantes = IntegerField('Total de estudiantes', validators=[DataRequired()])
    nombre_asignatura = StringField('Nombre asignatura', validators=[DataRequired(), Length(min=5, max=30)])
    unidad_asignatura = IntegerField('Unidad', validators=[DataRequired()])
    nombre_jefe_departamento = SelectField('Nombre Jefe de Departamento', validators=[DataRequired()],
                                            choices=[])
    nombre_subdirector = SelectField('Nombre de Subdirector', validators=[DataRequired()],
                                        choices=[])
    submit = SubmitField('Solicitar')




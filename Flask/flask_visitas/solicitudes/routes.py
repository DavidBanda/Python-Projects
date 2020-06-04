from flask import (render_template, url_for, flash,
                    redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flask_visitas import db
from flask_visitas.solicitudes.models import Visitas
from flask_visitas.solicitudes.forms import VisitaForm
from flask_visitas.usuarios.models import User

solicitudes = Blueprint('solicitudes', __name__)


@solicitudes.route('/visita/nueva', methods=['GET', 'POST'])
@login_required
def nueva_visita():
    if current_user.access == 0:
        form = VisitaForm()
        form.nombre_jefe_departamento.choices = User.getJefeDepartamento()
        form.nombre_subdirector.choices = User.getSubdirector()
        if form.validate_on_submit():
            visita = Visitas()
            visita.name_tec = form.name_tec.data
            visita.name_sub = form.name_sub.data
            visita.periodo_escolar = int(form.periodo_escolar.data)
            visita.no_visitas = form.no_visitas.data
            visita.nombre_empresa = form.nombre_empresa.data
            visita.ciudad = form.ciudad.data
            visita.objetivo = form.objetivo.data
            visita.area_visita = form.area_visita.data
            visita.fecha_visita = form.fecha_visita.data
            visita.turno = int(form.turno.data)
            visita.carrera = int(form.carrera.data)
            visita.semestre = form.semestre.data
            visita.total_estudiantes = form.total_estudiantes.data
            visita.nombre_asignatura = form.nombre_asignatura.data
            visita.unidad_asignatura = form.unidad_asignatura.data
            visita.nombre_jefe_departamento = form.nombre_jefe_departamento.data
            visita.nombre_subdirector = form.nombre_subdirector.data
            visita.author = current_user
            db.session.add(visita)
            db.session.commit()
            flash('Tu visita ha sido creada!', 'success')
            return redirect(url_for('principal.visitas'))
        return render_template('create_visita.html', title='Nueva Visita',
                                legend='Nueva Visita', form=form)
    page = request.args.get('page', 1, type=int)
    visitas = Visitas.query.order_by(Visitas.fecha_visita.asc()).paginate(page=page, per_page=5)
    last_visita = Visitas.query.order_by(Visitas.fecha_visita.asc()).last()
    return render_template('visitas.html', visitas=visitas, title="Visitas", last_visita=last_visita)


@solicitudes.route('/visita/<int:visita_id>/actualizar', methods=['GET', 'POST'])
@login_required
def actualizar_visita(visita_id):
    visita = Visitas.query.get_or_404(visita_id)
    legend = 'Actualizar Visita'
    if visita.author != current_user and current_user.access != 4:
        legend = 'Visita'
    form = VisitaForm()
    form.nombre_jefe_departamento.choices = User.getJefeDepartamento()
    form.nombre_subdirector.choices = User.getSubdirector()
    if form.validate_on_submit():
        visita.name_tec = form.name_tec.data
        visita.name_sub = form.name_sub.data
        visita.periodo_escolar = int(form.periodo_escolar.data)
        visita.no_visitas = form.no_visitas.data
        visita.nombre_empresa = form.nombre_empresa.data
        visita.ciudad = form.ciudad.data
        visita.objetivo = form.objetivo.data
        visita.area_visita = form.area_visita.data
        visita.fecha_visita = form.fecha_visita.data
        visita.turno = int(form.turno.data)
        visita.carrera = int(form.carrera.data)
        visita.semestre = form.semestre.data
        visita.total_estudiantes = form.total_estudiantes.data
        visita.nombre_asignatura = form.nombre_asignatura.data
        visita.unidad_asignatura = form.unidad_asignatura.data
        visita.nombre_jefe_departamento = form.nombre_jefe_departamento.data
        visita.nombre_subdirector = form.nombre_subdirector.data
        visita.status_jefe_departamento = 0
        visita.status_subdirector = 0
        visita.status_gestion_tecnologica = 0
        db.session.commit()
        flash('La visita ha sido actualizada!', 'success')
        return redirect(url_for('principal.visitas', visita_id=visita.id))

    if request.method == 'GET':
        form.name_tec.data = visita.name_tec
        form.name_sub.data = visita.name_sub
        form.periodo_escolar.data = visita.periodo_escolar
        form.no_visitas.data = visita.no_visitas
        form.nombre_empresa.data = visita.nombre_empresa
        form.ciudad.data = visita.ciudad
        form.objetivo.data = visita.objetivo
        form.area_visita.data = visita.area_visita
        form.fecha_visita.data = visita.fecha_visita
        form.turno.data = visita.turno
        form.carrera.data = visita.carrera
        form.semestre.data = visita.semestre
        form.total_estudiantes.data = visita.total_estudiantes
        form.nombre_asignatura.data = visita.nombre_asignatura
        form.unidad_asignatura.data = visita.unidad_asignatura
        form.nombre_jefe_departamento.data = visita.nombre_jefe_departamento
        form.nombre_subdirector.data = visita.nombre_subdirector
    form.nombre_jefe_departamento.choices = User.getJefeDepartamento()
    form.nombre_subdirector.choices = User.getSubdirector()
    return render_template('create_visita.html', title='Actualizar Visita',
                            form=form, legend=legend)

@solicitudes.route('/visita/<int:visita_id>/actualizar-status', methods=['POST'])
@login_required
def actualizar_status(visita_id):
    visita = Visitas.query.get_or_404(visita_id)
    userAccess = current_user.access
    state = request.args.get('state', type=int)
    if current_user.access not in [1, 2, 3]:
        abort(403)
    if userAccess == 1:
        visita.status_jefe_departamento = state
    elif userAccess == 2:
        visita.status_subdirector = state
    elif userAccess == 3:
        visita.status_gestion_tecnologica = state
    db.session.commit()
    if state == 1:
        flash('La visita ha sido aceptada!', 'success')
    elif state == 2:
        flash('La visita ha sido rechazada!', 'warning')
    return redirect(url_for('principal.visitas'))

@solicitudes.route('/visita/<int:visita_id>/borrar', methods=['POST'])
@login_required
def borrar_visita(visita_id):
    visita = Visitas.query.get_or_404(visita_id)
    if visita.author != current_user and current_user.access != 4:
        abort(403)
    db.session.delete(visita)
    db.session.commit()
    flash('La visita ha sido eliminada!', 'success')
    return redirect(url_for('principal.visitas'))








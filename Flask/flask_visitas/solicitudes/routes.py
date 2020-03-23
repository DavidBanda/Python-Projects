from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flask_visitas import db
from flask_visitas.solicitudes.models import Visitas
from flask_visitas.solicitudes.forms import VisitaForm

solicitudes = Blueprint('solicitudes', __name__)


@solicitudes.route('/visita/nueva', methods=['GET', 'POST'])
@login_required
def nueva_visita():
    if current_user.access == 0:
        form = VisitaForm()
        if form.validate_on_submit():
            visita = Visitas(title=form.title.data, content=form.content.data, author=current_user)
            db.session.add(visita)
            db.session.commit()
            flash('Tu visita ha sido creada!', 'success')
            return redirect(url_for('main.visitas'))
        return render_template('create_visita.html', title='Nueva Visita',
                               legend='Nueva Visita', form=form)
    page = request.args.get('page', 1, type=int)
    visitas = Visitas.query.order_by(Visitas.fecha_elaboracion.desc()).paginate(page=page, per_page=5)
    last_visita = Visitas.query.order_by(Visitas.fecha_elaboracion.desc()).first()
    return render_template('visitas.html', visitas=visitas, title="Visitas", last_visita=last_visita)


@solicitudes.route('/visita/<int:visita_id>')
@login_required
def visita(visita_id):
    visita = Visitas.query.get_or_404(visita_id)
    return render_template('visita.html', title='Visita', visita=visita)


@solicitudes.route('/visita/<int:visita_id>/actualizar', methods=['GET', 'POST'])
@login_required
def actualizar_visita(visita_id):
    visita = Visitas.query.get_or_404(visita_id)
    if visita.author != current_user and current_user.access != 4:
        abort(403)
    form = VisitaForm()
    if form.validate_on_submit():
        visita.title = form.title.data
        visita.content = form.content.data
        db.session.commit()
        flash('Tu visita ha sido actualizada!', 'success')
        return redirect(url_for('solicitudes.visita', visita_id=visita.id))
    if request.method == 'GET':
        form.title.data = visita.title
        form.content.data = visita.content
    return render_template('create_visita.html', title='Actualizar Visita',
                           form=form, legend='Actualizar Visita')


@solicitudes.route('/visita/<int:visita_id>/borrar', methods=['POST'])
@login_required
def borrar_visita(visita_id):
    visita = Visitas.query.get_or_404(visita_id)
    if visita.author != current_user and current_user.access != 4:
        abort(403)
    db.session.delete(visita)
    db.session.commit()
    flash('Tu visita ha sido eliminada!', 'success')
    return redirect(url_for('main.visitas'))








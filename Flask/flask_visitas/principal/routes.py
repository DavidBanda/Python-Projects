from flask import render_template, request, Blueprint, redirect, url_for
from flask_visitas.solicitudes.models import Visitas
from flask_login import login_required, current_user

principal = Blueprint('principal', __name__)


@principal.route('/')
@principal.route('/visitas')
@login_required
def visitas():
    if current_user.access == 0:
        return redirect(url_for('usuarios.visitas_usuario', id=current_user.id))
    page = request.args.get('page', 1, type=int)
    visitas = Visitas.query.order_by(Visitas.fecha_visita.asc()).paginate(page=page, per_page=5)
    last_visita = Visitas.query.order_by(Visitas.fecha_visita.asc()).first()
    return render_template('visitas.html', visitas=visitas, title="Visitas", last_visita=last_visita)


@principal.route('/grupos')
@login_required
def grupos():
    return render_template('grupos.html', title="Grupos")







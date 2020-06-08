from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import login_user, current_user, logout_user, login_required
from flask_visitas import db, bcrypt, mail
from flask_visitas.solicitudes.models import Visitas
from flask_visitas.usuarios.models import User
from flask_visitas.usuarios.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                            RequestResetForm, ResetPasswordForm)
from flask_visitas.usuarios.utils import save_picture, delete_picture
from flask_mail import Message

usuarios = Blueprint('usuarios', __name__)


@usuarios.route('/registrar', methods=['GET', 'POST'])
@login_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, department=int(form.department.data),
                    access=int(form.access.data), password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Tu cuenta ha sido creada! Ahora puedes iniciar sesión', 'success')
        return redirect(url_for('usuarios.login'))
    return render_template('register.html', title='Registro', form=form)


@usuarios.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('principal.visitas'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('principal.visitas'))
        else:
            flash('Inicio de sesión fallido. Favor de verificar correo y contraseña', 'danger')
    return render_template('login.html', title='Login', form=form)


@usuarios.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('usuarios.login'))


@usuarios.route('/cuenta', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    form.data_user_prev = current_user
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            delete_picture(current_user.image_file)
            current_user.image_file = picture_file
        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.department = int(form.department.data)
        current_user.access = int(form.access.data)
        db.session.commit()
        flash('Tu cuenta ha sido actualizada!', 'success')
        # return redirect(url_for('usuarios.account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
        form.department.data = f'{current_user.department}'
        form.access.data = f'{current_user.access}'
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Cuenta',
                           image_file=image_file, form=form)


@usuarios.route('/usuario/<int:id>/')
@login_required
def visitas_usuario(id):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(id=id).first_or_404()
    visitas = Visitas.query.filter_by(author=user) \
        .order_by(Visitas.fecha_elaboracion.desc()) \
        .paginate(page=page, per_page=5)
    last_visita = Visitas.query.filter_by(author=user).order_by(Visitas.fecha_visita.asc()).first()
    return render_template('visitas_usuario.html', visitas=visitas, title="Visitas Usuario", user=user,
                           last_visita=last_visita)


@usuarios.route('/usuarios')
@login_required
def all_users():
    if current_user.access == 4:
        page = request.args.get('page', 1, type=int)
        users = User.query.order_by(User.name.desc()).paginate(page=page, per_page=7)
        return render_template('usuarios_admin.html', users=users, title="Usuarios")

    abort(401)


@usuarios.route('/cuenta/<int:id>/', methods=['GET', 'POST'])
@login_required
def account_admin(id):
    user = User.query.filter_by(id=id).first_or_404()
    form = UpdateAccountForm()
    form.data_user_prev = user
    if current_user.access == 4:
        if form.validate_on_submit():
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                delete_picture(user.image_file)
                user.image_file = picture_file
            user.name = form.name.data
            user.email = form.email.data
            user.department = int(form.department.data)
            user.access = int(form.access.data)
            db.session.commit()
            flash('Tu cuenta ha sido actualizada!', 'success')
            return redirect(url_for('usuarios.account_admin', id=user.id))
        elif request.method == 'GET':
            form.name.data = user.name
            form.email.data = user.email
            form.access.data = f'{user.access}'
            form.department.data = f'{user.department}'
        image_file = url_for('static', filename='profile_pics/' + user.image_file)
        return render_template('account.html', title='Cuenta',
                            image_file=image_file, form=form, user=user)
    elif current_user.access in [1, 2, 3]:
        form.name.data = user.name
        form.email.data = user.email
        form.access.data = f'{user.access}'
        form.department.data = f'{user.department}'
        image_file = url_for('static', filename='profile_pics/' + user.image_file)
        return render_template('account.html', title='Cuenta',
                                image_file=image_file, form=form, user=user)

    abort(403)


@usuarios.route('/usuario/<int:usuario_id>/borrar', methods=['POST'])
@login_required
def borrar_usuario(usuario_id):
    usuario = User.query.get_or_404(usuario_id)
    if current_user.access != 4:
        abort(403)
    db.session.delete(usuario)
    db.session.commit()
    flash('El usuario ha sido eliminado!', 'success')
    return redirect(url_for('usuarios.all_users'))


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Restablecer Contraseña',
                    sender='noreply@demo.com',
                    recipients=[user.email])
    # msg.body = \
    #     f''' Para restablecer tu contraseña, da click en el siguiente 
    #     link: {url_for('usuarios.reset_token', token=token, _external=True)} 
    
    #     Si no hiciste esta solicitud, por favor ignora este email. 
    #     '''

    image_file = url_for('static', filename='images/mail-itch2.jpeg') 
    msg.html = render_template('mail_body.html', token=token, image_file=image_file)

    mail.send(msg)


@usuarios.route('/restablecer-contraseña', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('principal.visitas'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Ah sido enviado un email con instrucciones para restablecer la contraseña.', 'info')
        return redirect(url_for('usuarios.login'))
    return render_template('restablecer_contraseña.html',
                            title="Restablecer Contraseña", form=form)


@usuarios.route('/restablecer-contraseña/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('principal.visitas'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('El token es invalido o ha expirado', 'warning')
        return redirect(url_for('usuarios.reset_request'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Tu contraseña ha sido actualizada! Ahora puedes iniciar sesión', 'success')
        return redirect(url_for('usuarios.login'))
    return render_template('restablecer_token.html',
                           title="Restablecer Contraseña", form=form)



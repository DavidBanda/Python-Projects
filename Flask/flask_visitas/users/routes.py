from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import login_user, current_user, logout_user, login_required
from flask_visitas import db, bcrypt
from flask_visitas.solicitudes.models import Visitas
from flask_visitas.users.models import User
from flask_visitas.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm)
from flask_visitas.users.utils import save_picture, delete_picture

users = Blueprint('users', __name__)


@users.route('/registrar', methods=['GET', 'POST'])
@login_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data,
                    access=int(form.access.data), password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Tu cuenta ha sido creada! Ahora puedes iniciar sesion', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Registro', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.visitas'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.visitas'))
        else:
            flash('Inicio de sesión fallido. Favor de verificar correo y contraseña', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@users.route('/cuenta', methods=['GET', 'POST'])
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
        current_user.access = int(form.access.data)
        db.session.commit()
        flash('Tu cuanta ha sido actualizada!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
        form.access.data = f'{current_user.access}'
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Cuenta',
                           image_file=image_file, form=form)


@users.route('/usuario/<int:id>/')
@login_required
def visitas_usuario(id):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(id=id).first_or_404()
    visitas = Visitas.query.filter_by(author=user)\
        .order_by(Visitas.fecha_elaboracion.desc())\
        .paginate(page=page, per_page=5)
    return render_template('visitas_usuario.html', visitas=visitas, title="Visitas Usuario", user=user)


@users.route('/usuarios')
@login_required
def all_users():
    if current_user.access == 4:
        page = request.args.get('page', 1, type=int)
        users = User.query.order_by(User.name.desc()).paginate(page=page, per_page=7)
        return render_template('usuarios_admin.html', users=users, title="Usuarios")

    abort(403)


@users.route('/cuenta/<int:id>/', methods=['GET', 'POST'])
@login_required
def account_admin(id):
    if current_user.access == 4:
        user = User.query.filter_by(id=id).first_or_404()
        form = UpdateAccountForm()
        form.data_user_prev = user
        if form.validate_on_submit():
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                delete_picture(user.image_file)
                user.image_file = picture_file
            user.name = form.name.data
            user.email = form.email.data
            user.access = int(form.access.data)
            db.session.commit()
            flash('Tu cuanta ha sido actualizada!', 'success')
            return redirect(url_for('users.account_admin', id=user.id))
        elif request.method == 'GET':
            form.name.data = user.name
            form.email.data = user.email
            form.access.data = f'{user.access}'
        image_file = url_for('static', filename='profile_pics/' + user.image_file)
        return render_template('account.html', title='Cuenta',
                               image_file=image_file, form=form, user=user)

    abort(403)





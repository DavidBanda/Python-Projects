from flask import render_template, request, Blueprint, redirect, url_for
from flaskblog.solicitudes.models import Post
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

"""
solicitudes = [
    {
        'author': 'Ruben Alonso',
        'title': 'Visita 1',
        'content': 'Contenido de visita',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Angelica Garcia',
        'title': 'Visita 2',
        'content': 'Contenido de visita',
        'date_posted': 'April 21, 2018'
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('visitas.html', solicitudes=solicitudes, title="Home")
"""


@main.route('/')
@main.route('/visitas')
@login_required
def visitas():
    # return render_template('visitas.html', posts=posts, title="Visitas", last_post=last_post)
    return redirect(url_for('users.user_posts', username=current_user.username))


@main.route('/grupos')
def grupos():
    return render_template('grupos.html', title="Grupos")



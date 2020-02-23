from flask import render_template, request, Blueprint
from flaskblog.solicitudes.models import Post
from flask_login import login_required

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
    return render_template('home.html', solicitudes=solicitudes, title="Home")
"""


@main.route('/')
@main.route('/home')
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    last_post = Post.query.order_by(Post.date_posted.desc()).first()
    return render_template('home.html', posts=posts, title="Home", last_post=last_post)


@main.route('/about')
def about():
    return render_template('about.html', title="About")



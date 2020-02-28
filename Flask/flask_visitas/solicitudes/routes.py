from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flask_visitas import db
from flask_visitas.solicitudes.models import Post
from flask_visitas.solicitudes.forms import PostForm

solicitudes = Blueprint('solicitudes', __name__)


@solicitudes.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if current_user.access == 0:
        form = PostForm()
        if form.validate_on_submit():
            post = Post(title=form.title.data, content=form.content.data, author=current_user)
            db.session.add(post)
            db.session.commit()
            flash('Your post has been created!', 'success')
            return redirect(url_for('main.visitas'))
        return render_template('create_post.html', title='Nueva Visita',
                               legend='Nueva Visita', form=form)
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    last_post = Post.query.order_by(Post.date_posted.desc()).first()
    return render_template('visitas.html', posts=posts, title="Visitas", last_post=last_post)


@solicitudes.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title='Post', post=post)


@solicitudes.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('solicitudes.post', post_id=post.id))
    if request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Actualizar Visita',
                           form=form, legend='Actualizar Visita')


@solicitudes.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.visitas'))








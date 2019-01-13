from flask import render_template, redirect, url_for, request, \
    current_app, make_response
from flask_login import current_user, login_required
from . import post
from .forms import PostForm
from ..models import Post, Permission
from .. import db


@post.route('/', methods=['GET', 'POST'])
def show_posts():
    form = PostForm()
    if current_user.can(Permission.WRITE) and form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.show_posts'))

    page = request.args.get('page', 1, type=int)
    show_followed = False

    if current_user.is_authenticated:
        show_followed = bool(request.cookies.get('show_followed', ''))
    if show_followed:
        query = current_user.followed_posts
    else:
        query = Post.query
    pagination = query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('post/show_posts.html', form=form, posts=posts,
                           pagination=pagination, show_followed=show_followed)


@post.route('/<int:id>')
def show_post(id):
    post = Post.query.get_or_404(id)
    return render_template('post/single_post.html', posts=[post])


@post.route('/all')
@login_required
def show_all():
    resp = make_response(redirect(url_for('post.show_posts')))
    resp.set_cookie('show_followed', '', max_age=30*24*60*60)  # 30 days
    return resp


@post.route('/followed')
@login_required
def show_followed():
    resp = make_response(redirect(url_for('post.show_posts')))
    resp.set_cookie('show_followed', '1', max_age=30*24*60*60)  # 30 days
    return resp

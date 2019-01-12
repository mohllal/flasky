from flask import render_template, redirect, url_for, request, \
    current_app
from flask_login import current_user
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
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('post/show_posts.html', form=form, posts=posts,
                           pagination=pagination)

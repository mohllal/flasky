from flask import render_template
from . import profile
from ..models import User


@profile.route('/profile/<username>')
def show_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile/show_profile.html', user=user)






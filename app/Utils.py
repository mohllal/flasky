from .models import User, Role
from . import db
from flask import current_app


class Utils:

    @staticmethod
    def update_users_with_role():
        admin_role = Role.query.filter_by(name='Administrator').first()
        default_role = Role.query.filter_by(default=True).first()
        for u in User.query.all():
            if u.role is None:
                if u.email == current_app.config['FLASKY_ADMIN']:
                    u.role = admin_role
            else:
                u.role = default_role

            db.session.add(u)
        db.session.commit()

    @staticmethod
    def create_dummy_user(username, email, password, role_name):
        role = Role.query.filter_by(name=role_name).first()
        user = User(username=username, email=email, password=password, role=role, confirmed=True)

        db.session.add(user)
        db.session.commit()

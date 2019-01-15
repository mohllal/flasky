from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment
from config import config
from flask_pagedown import PageDown

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
moment = Moment()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    moment.init_app(app)
    pagedown.init_app(app)
    login_manager.init_app(app)

    # attaching routes and custom errors pages here
    # this will replaced with registering blueprint
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .profile import profile as profile_blueprint
    from .post import post as post_blueprint
    from .api_v1 import api_v1 as api_v1_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(profile_blueprint, url_prefix='/profile')
    app.register_blueprint(post_blueprint, url_prefix='/post')
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

    return app

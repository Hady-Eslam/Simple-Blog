from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from App.configs import Config
from App.errors import errors
from App.errors import handlers     #### Leave It Like This
import importlib


db = SQLAlchemy()

bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'authentication.login'
login_manager.login_message_category = 'info'

mail = Mail()


def init_app(module_name=__name__, configs=Config):
    app = Flask(module_name, template_folder='App/templates', static_folder='App/static')

    app.config.from_object(configs())

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    app.register_blueprint(errors)

    for blueprint in app.config.get('INSTALLED_BLUEPRINTS'):
        mymodule = importlib.import_module('App.Blueprints.' + blueprint)
        importlib.import_module('App.Blueprints.' + blueprint + '.routes')
        importlib.import_module('App.Blueprints.' + blueprint + '.handlers')
        app.register_blueprint(mymodule.__dict__[blueprint.lower()])

    return app

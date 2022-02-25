from dotenv import load_dotenv
load_dotenv('App/.env')


import importlib
from App import init_app
from App import db
app = init_app(__name__)


for blueprint in app.config.get('INSTALLED_BLUEPRINTS'):
    importlib.import_module('App.Blueprints.' + blueprint + '.models')


with app.app_context():
    db.create_all()

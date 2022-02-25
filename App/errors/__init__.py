from flask import Blueprint

errors = Blueprint('errors', __name__, template_folder='templates/errors', static_folder='static/errors')

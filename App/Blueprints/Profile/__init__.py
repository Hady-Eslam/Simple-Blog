from flask import Blueprint


profile = Blueprint('profile', __name__, template_folder='templates/Profile', static_folder='static/Profile')

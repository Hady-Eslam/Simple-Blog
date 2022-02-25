from flask import Blueprint


posts = Blueprint('posts', __name__, template_folder='templates/Posts', static_folder='static/Posts')

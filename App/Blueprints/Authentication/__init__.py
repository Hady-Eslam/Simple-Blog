from flask import Blueprint

authentication = Blueprint(
    'authentication', __name__,
    template_folder='templates/Authentication',
    static_folder='static/Authentication'
)

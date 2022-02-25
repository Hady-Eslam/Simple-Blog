from flask import render_template
from App.Blueprints.Authentication import authentication




@authentication.errorhandler(404)
def error_404(error):
    return render_template('Authentication_errors/error_404.html', error=error), 404



@authentication.errorhandler(403)
def error_403(error):
    return render_template('Authentication_errors/error_403.html', error=error), 403



@authentication.errorhandler(500)
def error_500(error):
    return render_template('Authentication_errors/error_500.html', error=error), 500

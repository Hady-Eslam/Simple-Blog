from flask import render_template
from App.Blueprints.Profile import profile




@profile.errorhandler(404)
def error_404(error):
    return render_template('Profile_errors.html', error=error), 404



@profile.errorhandler(403)
def error_403(error):
    return render_template('Profile_errors.html', error=error), 403



@profile.errorhandler(500)
def error_500(error):
    return render_template('Profile_errors.html', error=error), 500

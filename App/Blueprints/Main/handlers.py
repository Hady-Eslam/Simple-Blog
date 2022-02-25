from flask import render_template
from App.Blueprints.Main import main




@main.errorhandler(404)
def error_404(error):
    return render_template('Main_errors/errors.html', error=error), 404



@main.errorhandler(403)
def error_403(error):
    return render_template('Main_errors/errors.html', error=error), 403



@main.errorhandler(500)
def error_500(error):
    return render_template('Main_errors/errors.html', error=error), 500

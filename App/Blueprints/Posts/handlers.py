from flask import render_template
from App.Blueprints.Posts import posts




@posts.errorhandler(404)
def error_404(error):
    return render_template('Posts_errors/error_404.html', error=error), 404



@posts.errorhandler(403)
def error_403(error):
    return render_template('Posts_errors/error_403.html', error=error), 403



@posts.errorhandler(500)
def error_500(error):
    return render_template('Posts_errors/error_500.html', error=error), 500

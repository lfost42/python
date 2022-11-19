from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    """
    returns 404.html error
    """
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    """
    returns 403.html error
    """
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    """
    returns 500.html error
    """
    return render_template('errors/500.html'), 500
from flask import render_template
from ..app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('erreurs/404.html'), 404

@app.errorhandler(502)
def internal_error(error):
    return render_template('erreurs/500.html'), 500
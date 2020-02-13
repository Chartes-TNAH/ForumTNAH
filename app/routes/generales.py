from ..app import app
from flask import render_template

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """
	Route permettant l'affichage de la page d'accueil
	:return: template de la page d'accueil
	"""
    return render_template("pages/home.html", nom="Accueil")
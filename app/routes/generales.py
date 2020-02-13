from ..app import app, db, login
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_user, current_user, logout_user
from ..modeles.utilisateurs import User
from ..modeles.donnees import Post


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """
	Route permettant l'affichage de la page d'accueil
	:return: template de la page d'accueil
	"""
    return render_template("pages/home.html", nom="Accueil")


@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    """
    Route permettant d'afficher le formulaire d'inscription
    :return: template de la page d'inscription' avec le formulaire
    """
    # en cas de réussite d'envoi du formulaire
    if request.method == 'POST':
        statut, donnees = User.creer(
            user_name=request.form.get("user_name", None),
            user_mail=request.form.get("user_mail", None),
            user_firstname=request.form.get("user_firstname", None),
            user_surname=request.form.get("user_surname", None),
            user_password=request.form.get("user_password", None)
        )
        if statut is True:
            flash("Vous êtes désormais inscrit. Connectez-vous.", "success")
            return redirect(url_for('home'))
        else:
            flash("Plusieurs erreurs sont survenues: " + ",".join(donnees), "error")
            return render_template("pages/inscription.html", nom="Inscription")
    else:
        return render_template('pages/inscription.html', nom="Inscription")

@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    """ Route gérant les connexions
    """
    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté", "info")
        return redirect("/")
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        utilisateur = User.identification(
            user_name=request.form.get("user_name", None),
            password=request.form.get("user_password", None)
        )
        if utilisateur:
            flash("Connexion effectuée", "success")
            login_user(utilisateur)
            return redirect("/")
        else:
            flash("Les identifiants n'ont pas été reconnus", "error")

    return render_template("pages/connexion.html")
login.login_view = 'connexion'

@app.route("/deconnexion", methods=["POST", "GET"])
def deconnexion():
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté", "info")
    return redirect(url_for('home'))
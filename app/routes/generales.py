from ..app import app, db, login
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from werkzeug.urls import url_parse
from ..modeles.utilisateurs import LoginForm, RegistrationForm, EditProfileForm, PostForm
from ..modeles.donnees import Post, User


# mettre à jour la date de visite dans la base de données
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.user_last_seen = datetime.utcnow()
        db.session.commit()


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
    Route permettant l'inscription d'un nouvel utilisateur
    :return: template de la page d'inscription avec le formulaire
    """
    if current_user.is_authenticated:
        return redirect('home')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(user_name = form.username.data,
                    user_mail = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Inscription enregistrée')
        return redirect(url_for('connexion'))
    return render_template('pages/inscription.html', nom="Inscription", form=form)


@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    """ Route gérant les connexions
    """
    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté", "info")
        return redirect("/")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        if user is None or not user.check_password(form.user_password.data):
            flash('Nom d\'utilisateur ou mot de passe incorrect')
            return redirect(url_for('connexion'))
        login_user(user, remember=form.remember_me.data)
        flash("Vous êtes maintenant connecté.")
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('pages/connexion.html', form=form)


@app.route("/deconnexion", methods=["POST", "GET"])
def deconnexion():
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté", "info")
    return redirect(url_for('home'))


@app.route('/utilisateur/<user_name>')
def utilisateur(user_name):
    utilisateur = User.query.filter_by(user_name=user_name).first_or_404()
    posts = utilisateur.posts.order_by(Post.post_date.desc()).all()
    return render_template("pages/utilisateur.html", nom=user_name, user=utilisateur, posts=posts)


@app.route('/editer_profil', methods=['GET', 'POST'])
@login_required
def editer_profil():
    """
    Route permettant de modifier ses données personnelles
    :return: template de la page d'édition du profil avec le formulaire
    """
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.user_name = form.user_name.data
        current_user.user_firstname = form.user_firstname.data
        current_user.user_surname = form.user_surname.data
        current_user.user_mail = form.user_mail.data
        current_user.user_promotion_date = form.user_promotion_date.data
        current_user.user_birthyear = form.user_birthyear.data
        current_user.user_description = form.user_description.data
        db.session.commit()
        flash("Modifications enregistrées")
        return redirect(url_for('utilisateur', user_name=current_user.user_name))
    elif request.method == 'GET':
        form.user_name.data = current_user.user_name
        form.user_description.data = current_user.user_description
        form.user_firstname.data = current_user.user_firstname
        form.user_surname.data = current_user.user_surname
        form.user_promotion_date.data = current_user.user_promotion_date
        form.user_mail.data = current_user.user_mail
        form.user_birthyear.data = current_user.user_birthyear
    return render_template('pages/editer.html', nom="Editer le profil", form=form)

@app.route('/fil', methods=['GET', 'POST'])
def poster():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(post_titre=form.titre.data, post_message=form.message.data, auteur=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Votre message est maintenant publié")
        return redirect(url_for('poster'))
    posts = Post.query.order_by(Post.post_date.desc()).all()
    return render_template('pages/publier.html', nom="Publier", form=form, posts=posts)
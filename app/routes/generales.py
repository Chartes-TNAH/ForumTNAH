from ..app import app, db, login
from flask import render_template, flash, redirect, request, url_for, abort
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from werkzeug.urls import url_parse
from ..modeles.utilisateurs import LoginForm, RegistrationForm, EditProfileForm, PostForm, CommentForm, CVForm
from ..modeles.donnees import Post, User, Comment, CV
from ..constantes import POSTS_PAR_PAGE, COMMENTS_PAR_PAGE, POSTS_PAR_PAGE_DISCUSSION


# mettre à jour la date de visite dans la base de données
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.user_last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/')
@app.route('/home')
def home():
    """
	Route permettant l'affichage de la page d'accueil
	:return: template de la page d'accueil
	"""
    return render_template("pages/home.html",
                           nom="Accueil")

@app.route('/discussions')
def discussions():
    """
    Route permettant l'affichage de tous les posts du forum du plus récent au plus ancien.
    """
    # gestion de la pagination des posts
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.post_date.desc()).paginate(page=int(page), per_page=int(POSTS_PAR_PAGE_DISCUSSION))

    # pour afficher la date du dernier commentaire
    dernier_commentaire = {}
    liste_posts = Post.query.all()
    for post in liste_posts:
        last_comment = post.comments.order_by(Comment.comment_date.desc()).first()
        dernier_commentaire[post.post_id] = last_comment

    return render_template('pages/discussions.html',
                           nom="Discussions",
                           dernier_commentaire=dernier_commentaire,
                           posts=posts.items,
                           pagination=posts)

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
        user = User(user_name=form.username.data,
                    user_mail=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Inscription enregistrée')
        return redirect(url_for('connexion'))
    return render_template('pages/inscription.html',
                           nom="Inscription",
                           form=form)


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
    return render_template('pages/connexion.html',
                           nom='Connexion',
                           form=form)


@app.route("/deconnexion", methods=["POST", "GET"])
def deconnexion():
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté", "info")
    return redirect(url_for('home'))


@app.route('/explorer')
@login_required
def utilisateurs():
    utilisateurs = User.query.all()

    # création d'un dictionnaire avec le nom de l'utilisateur en clé et la dernière date de post en valeur
    dictionnaire_dates_posts = {}
    for utilisateur in utilisateurs:
        derniere_date = utilisateur.posts.order_by(Post.post_date.desc()).first()
        dictionnaire_dates_posts[utilisateur.user_name] = str(derniere_date.post_date)

    # pour afficher la date du dernier commentaire de l'utilisateur
    dernier_commentaire = {}
    for utilisateur in utilisateurs:
        derniere_date = utilisateur.comments.order_by(Comment.comment_date.desc()).first()
        dernier_commentaire[utilisateur.user_name] = str(derniere_date.comment_date)

    return render_template('pages/explorer.html',
                           nom='Explorer',
                           utilisateurs=utilisateurs,
                           dates_posts=dictionnaire_dates_posts,
                           dates_comments=dernier_commentaire)


@app.route('/suivre/<user_name>')
@login_required
def suivre(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    if user is None:
        flash('L\'utilisateur {} n\'a pas été trouvé'.format(user_name))
        return redirect(url_for('home'))
    if user == current_user:
        flash('Vous ne pouvez pas vous suivre vous-même')
        return redirect(url_for('utilisateur', user_name=user_name))
    current_user.follow(user)
    db.session.commit()
    flash('Vous suivez désormais {}!'.format(user_name))
    return redirect(url_for('utilisateur', user_name=user_name))

@app.route('/ne_plus_suivre/<user_name>')
@login_required
def ne_plus_suivre(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    if user is None:
        flash('L\'utilisateur {} n\'a pas été trouvé'.format(user_name))
        return redirect(url_for('home'))
    if user == current_user:
        flash('Vous ne pouvez pas ne plus vous suivre')
        return redirect(url_for('utilisateur', user_name=user_name))
    current_user.unfollow(user)
    db.session.commit()
    flash('Vous ne suivez plus {} désormais.'.format(user_name))
    return redirect(url_for('utilisateur', user_name=user_name))
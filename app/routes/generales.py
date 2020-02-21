from ..app import app, db, login
from flask import render_template, flash, redirect, request, url_for, abort
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from werkzeug.urls import url_parse
from ..modeles.utilisateurs import LoginForm, RegistrationForm, EditProfileForm, PostForm, CommentForm
from ..modeles.donnees import Post, User, Comment
from ..constantes import POSTS_PAR_PAGE, COMMENTS_PAR_PAGE


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
    return render_template("pages/home.html",
                           nom="Accueil")


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


@app.route('/utilisateur/<user_name>')
def utilisateur(user_name):
    page = request.args.get("page", 1)
    utilisateur = User.query.filter_by(user_name=user_name).first_or_404()
    posts = utilisateur.posts.order_by(Post.post_date.desc()).paginate(page=int(page), per_page=int(POSTS_PAR_PAGE))

    # pour afficher la date du dernier commentaire
    liste_posts = utilisateur.posts.order_by(Post.post_date.desc()).all()
    for post in liste_posts:
        dernier_commentaire = post.comments.order_by(Comment.comment_date.desc()).first()

    return render_template("pages/utilisateur.html",
                           nom=user_name,
                           user=utilisateur,
                           dernier_commentaire=dernier_commentaire,
                           posts=posts.items,
                           pagination=posts)


@app.route('/explorer')
@login_required
def utilisateurs():
    utilisateurs = User.query.all()

    # création d'un dictionnaire avec le nom de l'utilisateur en clé et la dernière date de post en valeur
    dictionnaire_dates_posts = {}
    for utilisateur in utilisateurs:
        derniere_date = utilisateur.posts.order_by(Post.post_date.desc()).first()
        dictionnaire_dates_posts[utilisateur.user_name] = str(derniere_date.post_date)

    # création d'un dictionnaire avec le nom de l'utilisateur en clé et la dernière date de commentaire en valeur
    dictionnaire_dates_comments = {}
    for utilisateur in utilisateurs:
        derniere_date = utilisateur.comments.order_by(Comment.comment_date.desc()).first()
        dictionnaire_dates_comments[utilisateur.user_name] = str(derniere_date.comment_date)

    return render_template('pages/explorer.html',
                           nom='Explorer',
                           utilisateurs=utilisateurs,
                           dates_posts=dictionnaire_dates_posts,
                           dates_comments=dictionnaire_dates_comments)

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
    return render_template('pages/editer.html',
                           nom="Editer le profil",
                           form=form)

@app.route('/editer_post/<int:id>', methods=['GET', 'POST'])
@login_required
def editer_post(id):
    """
    Route permettant de modifier ses propres posts
    """
    post = Post.query.get_or_404(id)
    if current_user != post.auteur:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.post_titre = form.titre.data
        post.post_message = form.message.data
        db.session.add(post)
        db.session.commit()
        flash("Le post a bien été mis à jour")
        return redirect(url_for('post', id=post.post_id))
    form.titre.data = post.post_titre
    form.message.data = post.post_message
    return render_template('pages/editer_post.html', form=form)

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

    # pour afficher la date du dernier commentaire
    utilisateur = User.query.filter_by(user_name=current_user.user_name).first_or_404()
    liste_posts = utilisateur.posts.order_by(Post.post_date.desc()).all()
    dernier_commentaire = "Pas encore de commentaires"
    for post in liste_posts:
            dernier_commentaire = post.comments.order_by(Comment.comment_date.desc()).first()

    return render_template('pages/publier.html',
                           nom="Publier",
                           dernier_commentaire=dernier_commentaire,
                           form=form,
                           posts=posts)


@app.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    """
    Fonction renvoyant le template Post avec un seul post désigné par l'id: permet de créer des liens permanents pour partager
    """
    post = Post.query.get_or_404(id)
    utilisateur = User.query.filter_by(user_name=current_user.user_name).first_or_404()
    dernier_commentaire = post.comments.order_by(Comment.comment_date.desc()).first()

    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment_message=form.message.data,
                          comment_post=post.post_id,
                          comment_auteur=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash("Votre commentaire a été publié")
        return redirect(url_for('post', id=post.post_id))

    page = request.args.get('page', 1, type=int)
    comments = utilisateur.comments.order_by(Comment.comment_date.desc()).paginate(page=int(page), per_page=int(COMMENTS_PAR_PAGE))

    return render_template('pages/post.html',
                           nom='Post',
                           posts=[post],
                           post=str(post.post_id),
                           dernier_commentaire=dernier_commentaire,
                           form=form,
                           comments=comments.items,
                           pagination=comments)

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
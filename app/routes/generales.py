from ..app import app, db
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from werkzeug.urls import url_parse
from ..modeles.utilisateurs import LoginForm, RegistrationForm
from ..modeles.donnees import Post, User, Comment, Competences, CV
from ..modeles.utilitaires import get_first_image
from ..constantes import POSTS_PAR_PAGE_DISCUSSION, POSTS_HASARD, RESULTATS_PAR_PAGE
import random

# dans l'ordre:
# /
# /home
# /discussions
# /thematiques
# /thematiques/<thematique>
# /competences
# /competences/<competence>
# /lieux
# /lieux/<lieu>
# /inscription
# /connexion
# /deconnexion
# /explorer
# /suivre
# /ne_plus_suivre
# /recherche


# mise à jour de la date de visite dans la base de données dès que l'utilisateur fait une action
@app.before_request
def before_request():
    """
    Permet de mettre à jour la date de dernière activité dans la base de données dès que l'utilisateur se connecte
    :return: None
    :rtype: None
    """
    if current_user.is_authenticated:
        current_user.user_last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/')
def racine():
    """
    Route sur laquelle l'utilisateur arrive en ouvrant le site, il doit se connecter pour accéder au ForumTNAH
    :return: template racine.html
    :rtype: template
    """
    return render_template('pages/racine.html')


@app.route('/home')
@login_required
def home():
    """
    Route permettant l'affichage de la page d'accueil
    :return: template home.html de la page d'accueil
    :rtype: template
    """
    # comptage du nombre d'utilisateurs du forum
    compteur_utilisateur = User.query.count()
    # comptage du nombre de posts
    compteur_posts = Post.query.count()
    # comptage du nombre de commentaires
    compteur_comments = Comment.query.count()

    # choix de posts au hasard
    posts = Post.query.all()
    hasard = random.sample(posts, POSTS_HASARD)

    return render_template("pages/home.html",
                           compteur_utilisateur=compteur_utilisateur,
                           compteur_posts=compteur_posts,
                           compteur_comments=compteur_comments,
                           posts=hasard,
                           nb_posts=POSTS_HASARD,
                           nom="Accueil")


@app.route('/discussions')
@login_required
def discussions():
    """
    Route permettant l'affichage de tous les posts du forum du plus récent au plus ancien.
    :return: template discussions;html
    :rtype: template
    """
    # comptage du nombre de posts
    compteur_posts = Post.query.count()
    # comptage du nombre de commentaires
    compteur_comments = Comment.query.count()

    # récupération de tous les posts
    tous_posts = Post.query.all()
    # création d'une liste vide qui prendra tous les mots clés des posts, sans doublons
    liste_distincte = []
    for post in tous_posts:
        # si le mot clé du post n'est pas présent dans la liste, alors il est jouté; s'il y est, alors il n'y est pas ajouté
        if post.post_indexation not in liste_distincte:
            liste_distincte.append(post.post_indexation)

    # gestion de la pagination des posts
    page = request.args.get('page', 1, type=int)
    # récupération des posts du forum, classés par date de création
    posts = Post.query.order_by(Post.post_date.desc()).paginate(page=int(page), per_page=int(POSTS_PAR_PAGE_DISCUSSION))

    # pour afficher la date du dernier commentaire
    # création d'un dictionnaire vide dans lequel seront insérés les id des posts en clé, et les id des commentaires en valeur
    dernier_commentaire = {}
    liste_posts = Post.query.all()
    for post in liste_posts:
        last_comment = post.comments.order_by(Comment.comment_date.desc()).first()
        dernier_commentaire[post.post_id] = last_comment

    return render_template('pages/discussions.html',
                           nom="Discussions",
                           dernier_commentaire=dernier_commentaire,
                           posts=posts.items,
                           pagination=posts,
                           compteur_posts=compteur_posts,
                           compteur_comments=compteur_comments,
                           mots_cles=liste_distincte)


@app.route('/thematiques')
@login_required
def thematiques():
    """
    Route permettant l'affichage des thématiques des posts
    :return: template thematiques.html
    :rtype: template
    """
    # récupération de tous les posts
    posts = Post.query.all()
    # création d'un dictionnaire vide qui aura comme clé le mot clé et comme valeur l'url de l'image
    dictionnaire_distinct = {}

    for post in posts:
        # si le mot clé du post n'est pas présent dans la liste, alors il est jouté; s'il y est, alors il n'y est pas ajouté
        if post.post_indexation not in dictionnaire_distinct:
            try:
                # récupération de l'image
                image = get_first_image(post.post_indexation)
                # remplissage du dictionnaire
                dictionnaire_distinct[post.post_indexation] = image
            except:
                dictionnaire_distinct[post.post_indexation] = "http://commons.wikimedia.org/wiki/File:High-contrast-emblem-photos.svg"

    # comptage du nombre de nombre de mots-clés
    compteur_tags = len(dictionnaire_distinct)

    return render_template('pages/thematiques/thematiques.html',
                           nom="Thématiques",
                           sujets=dictionnaire_distinct,
                           compteur_tags=compteur_tags)


@app.route('/thematiques/<thematique>')
@login_required
def thematique(thematique):
    """
    Route permettant l'affichage des posts en fonction du mot-clé demandé
    :param thematique: châine de caractère correspondant au mot-clé
    :type thematique: str
    :return: template thematique.html
    :rtype: template
    """
    # récupération des posts correspondant à la thématique choisie
    posts = Post.query.filter(Post.post_indexation == thematique).all()

    # récupération de tous les posts du forum
    post_liste = Post.query.all()

    # création d'une liste vide qui prendra tous les mots clés des posts, sans doublons
    liste_distincte = []
    for post in post_liste:
        # si le mot clé du post n'est pas présent dans la liste, alors il est jouté; s'il y est, alors il n'y est pas ajouté
        if post.post_indexation not in liste_distincte:
            liste_distincte.append(post.post_indexation)

    return render_template('pages/thematiques/thematique.html',
                           nom=thematique,
                           posts=posts,
                           sujet=thematique,
                           sujets=liste_distincte)


@app.route('/competences')
@login_required
def competences():
    """
        Route permettant l'affichage des competences
        :return: template competences.html
        :rtype: template
    """
    # récupération de toutes les compétences
    competences = Competences.query.all()

    # création d'un dictionnaire vide qui aura comme clé la compétence et comme valeur l'url de l'image
    dictionnaire_distinct = {}

    for competence in competences:
        try:
            # récupération de l'image
            image = get_first_image(competence.competence_label)
            # remplissage du dictionnaire
            dictionnaire_distinct[competence.competence_label] = image
        except:
            dictionnaire_distinct[competence.competence_label] = "https://thenounproject.com/term/skills/369287/"

    # comptage du nombre de nombre de mots-clés
    compteur_competences = len(dictionnaire_distinct)

    return render_template('pages/competences/competences.html',
                           nom="Compétences",
                           competences=dictionnaire_distinct,
                           compteur_competences=compteur_competences)


@app.route('/competences/<competence>')
@login_required
def competence(competence):
    """
    Route permettant l'affichage des utilisateurs en fonction de la compétence demandée
    :param competence: châine de caractère correspondant au mot-clé
    :type competence: str
    :return: template competence.html
    :rtype: template
    """
    # récupération de la classe de la compétence
    competence_donnee = Competences.query.filter(Competences.competence_label == competence).all()

    # récupération des utilisateurs correspondant à la compétence choisie
    utilisateurs = User.query.filter(User.competences.contains(competence_donnee[0])).all()

    # création d'une liste vide qui prendra toutes les compétences des utilisateurs, sans doublons
    competences = Competences.query.all()

    # création d'un dictionnaire avec le nom de l'utilisateur en clé et la dernière date de post en valeur
    derniers_posts = {}
    for utilisateur in utilisateurs:
        derniere_date = utilisateur.posts.order_by(Post.post_date.desc()).first()
        derniers_posts[utilisateur.user_name] = derniere_date

    # pour afficher la date du dernier commentaire de l'utilisateur
    derniers_commentaires = {}
    for utilisateur in utilisateurs:
        derniere_date = utilisateur.comments.order_by(Comment.comment_date.desc()).first()
        derniers_commentaires[utilisateur.user_name] = derniere_date

    return render_template('pages/competences/competence.html',
                           nom=competence,
                           utilisateurs=utilisateurs,
                           competence=competence,
                           competences=competences,
                           dates_posts=derniers_posts,
                           dates_comments=derniers_commentaires,
                           )


@app.route('/lieux')
@login_required
def lieux():
    """
        Route permettant l'affichage des lieux
        :return: template lieux.html
        :rtype: template
    """
    # récupération de toutes les lieux
    experiences = CV.query.all()

    # création d'un dictionnaire vide qui aura comme clé la compétence et comme valeur l'url de l'image
    dictionnaire_distinct = {}

    for experience in experiences:
        try:
            # récupération de l'image
            image = get_first_image(experience.cv_ville)
            # remplissage du dictionnaire
            dictionnaire_distinct[experience.cv_ville] = image
        except:
            dictionnaire_distinct[experience.cv_ville] = "http://www.istockphoto.com/vector/city-icons-set-signs-and-symbols-gm497023616-78886163"

    # comptage du nombre de nombre de mots-clés
    compteur_lieux = len(dictionnaire_distinct)

    return render_template('pages/lieux/lieux.html',
                           nom="Lieux",
                           lieux=dictionnaire_distinct,
                           compteur_lieux=compteur_lieux)


@app.route('/lieux/<lieu>')
@login_required
def lieu(lieu):
    """
    Route permettant l'affichage des utilisateurs en fonction du lieu de travail
    :param lieu: châine de caractère correspondant au lieu
    :type lieu: str
    :return: template lieu.html
    :rtype: template
    """
    # récupération de la classe du lieu
    lieu_donne = CV.query.filter(CV.cv_ville == lieu).all()
    print(lieu_donne)

    # récupération des utilisateurs correspondant au lieu choisi
    utilisateurs =[]
    for lieu in lieu_donne:
        utilisateurs += User.query.filter(User.cvs.contains(lieu)).all()

    # récupération de tous les cvs
    cvs = CV.query.all()
    # création d'une liste vide qui prendra tous les lieux , sans doublons
    liste_distincte = []
    for cv in cvs:
        if cv.cv_ville not in liste_distincte:
            liste_distincte.append(cv.cv_ville)

    # création d'un dictionnaire avec le nom de l'utilisateur en clé et la dernière date de post en valeur
    derniers_posts = {}
    for utilisateur in utilisateurs:
        derniere_date = utilisateur.posts.order_by(Post.post_date.desc()).first()
        derniers_posts[utilisateur.user_name] = derniere_date

    # pour afficher la date du dernier commentaire de l'utilisateur
    derniers_commentaires = {}
    for utilisateur in utilisateurs:
        derniere_date = utilisateur.comments.order_by(Comment.comment_date.desc()).first()
        derniers_commentaires[utilisateur.user_name] = derniere_date

    return render_template('pages/lieux/lieu.html',
                           nom=lieu.cv_ville,
                           utilisateurs=utilisateurs,
                           lieu=lieu,
                           lieux=liste_distincte,
                           dates_posts=derniers_posts,
                           dates_comments=derniers_commentaires,
                           )


@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    """
    Route permettant l'inscription d'un nouvel utilisateur
    :return: template inscription.html de la page d'inscription avec le formulaire
    :rtype: template
    """
    # vérification que l'utilisateur n'est pas déjà connecté
    if current_user.is_authenticated:
        return redirect('home')

    # utilisation du formulaire de classe RegistrationForm
    form = RegistrationForm()
    # validate_on_submit fonctionne avec la méthode POST
    if form.validate_on_submit():
        # la variable user stcoke provisoirement les données du formulaire réconciliées avec les champs de la base de données
        user = User(user_name=form.username.data,
                    user_mail=form.email.data,
                    user_inscription_date=datetime.utcnow())
        user.set_password(form.password.data)
        # ajout et commit des données de user dans la base de données
        db.session.add(user)
        db.session.commit()
        flash('Inscription enregistrée')
        return redirect(url_for('connexion'))

    return render_template('pages/inscription.html',
                           nom="Inscription",
                           form=form)


@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    """ Route gérant la connexion de l'utilisateur
    :return: template connexion.html
    :rtype: template
    """
    # vérification si l'utilisateur est déjà connecté: si c'est le cas, il est redirigé vers la page d'accueil
    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté", "info")
        return redirect("/home")

    # utilisation du formulaire de classe LoginForm
    form = LoginForm()
    # validate_on_submit fonctionne avec la méthode POST
    if form.validate_on_submit():
        # récupération des données de l'utilisateur en fonction du pseudo qu'il a rentré dans le formulaire
        user = User.query.filter_by(user_name=form.user_name.data).first()
        # vérification des nom d'utilisateur et mot de passe
        if user is None or not user.check_password(form.user_password.data):
            flash('Nom d\'utilisateur ou mot de passe incorrect')
            return redirect(url_for('connexion'))
        # connection de l'utilisateur si tout est correct
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

    """
    Route permettant la déconnexion de l'utilisateur
    :return: redirection vers la page d'accueil
    :rtype: template
    """
    # vérification si l'utilisateur est bien connecté
    if current_user.is_authenticated is True:
        # de manière à pouvoir le déconnecter
        logout_user()
    flash("Vous êtes déconnecté", "info")

    return redirect(url_for('home'))


@app.route('/explorer')
@login_required
def utilisateurs():
    """
    Route permettant de voir tous les utilisateurs du forum
    :return: template explorer.html
    :rtype: template
    """
    # récupération de l'ensemble des utilisateurs
    utilisateurs = User.query.all()

    # comptage du nombre d'utilisateurs
    compteur_utilisateurs = User.query.count()

    # création d'un dictionnaire avec le nom de l'utilisateur en clé et la dernière date de post en valeur
    derniers_posts = {}
    for utilisateur in utilisateurs:
        derniere_date = utilisateur.posts.order_by(Post.post_date.desc()).first()
        derniers_posts[utilisateur.user_name] = derniere_date

    # pour afficher la date du dernier commentaire de l'utilisateur
    derniers_commentaires = {}
    for utilisateur in utilisateurs:
        derniere_date = utilisateur.comments.order_by(Comment.comment_date.desc()).first()
        derniers_commentaires[utilisateur.user_name] = derniere_date

    return render_template('pages/explorer.html',
                           nom='Explorer',
                           utilisateurs=utilisateurs,
                           dates_posts=derniers_posts,
                           dates_comments=derniers_commentaires,
                           compteur_utilisateurs=compteur_utilisateurs)


@app.route('/suivre/<user_name>')
@login_required
def suivre(user_name):
    """
    Permet le suivi d'un utilisateur du forum
    :param user_name: pseudo de l'utilisateur
    :type user_name: str
    :return: template utilisateur.html
    :rtype: template
    """
    # récupération de l'utilisateur dont le pseudo a été donné en paramètre
    user = User.query.filter_by(user_name=user_name).first()

    # si l'utilisateur demandé n'existe pas, alors il y a redirection vers la page d'accueil
    if user is None:
        flash('L\'utilisateur {} n\'a pas été trouvé'.format(user_name))
        return redirect(url_for('home'))

    # si l'utilisateur demandé est celui connecté, alors il y a redirection vers son profil
    if user == current_user:
        flash('Vous ne pouvez pas vous suivre vous-même')
        return redirect(url_for('utilisateur', user_name=user_name))

    # si l'utilisateur demandé est correct, alors il est ajouté dans la base de données
    current_user.follow(user)
    db.session.commit()
    flash('Vous suivez désormais {}!'.format(user_name))

    return redirect(url_for('utilisateur', user_name=user_name))


@app.route('/ne_plus_suivre/<user_name>')
@login_required
def ne_plus_suivre(user_name):
    """
    Permet l'arrêt du suivi d'un utilisateur du forum
    :param user_name: pseudo de l'utilisateur
    :type user_name: str
    :return: template utilisateur.html
    :rtype: template
    """
    # récupération de l'utilisateur dont le pseudo a été donné en paramètre
    user = User.query.filter_by(user_name=user_name).first()

    # si l'utilisateur demandé n'existe pas, alors il y a redirection vers la page d'accueil
    if user is None:
        flash('L\'utilisateur {} n\'a pas été trouvé'.format(user_name))
        return redirect(url_for('home'))

    # si l'utilisateur demandé est celui connecté, alors il y a redirection vers son profil
    if user == current_user:
        flash('Vous ne pouvez pas ne plus vous suivre')
        return redirect(url_for('utilisateur', user_name=user_name))

    # si l'utilisateur demandé est correct, alors la modification est enregistrée dans la base de données
    current_user.unfollow(user)
    db.session.commit()
    flash('Vous ne suivez plus {} désormais.'.format(user_name))

    return redirect(url_for('utilisateur', user_name=user_name))


@app.route("/recherche/posts")
@login_required
def recherche_posts():
    """ Route permettant la recherche plein-texte dans le corps des messages publics
    """
    # On préfèrera l'utilisation de .get() ici
    #   qui nous permet d'éviter un if long (if "clef" in dictionnaire and dictonnaire["clef"])
    motclef = request.args.get("keyword", None)
    page = request.args.get("page", 1)

    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    # On crée une liste vide de résultat (qui restera vide par défaut
    #   si on n'a pas de mot clé)
    resultats = []

    # On fait de même pour le titre de la page
    titre = "Recherche"
    if motclef:
        resultats = Post.query.filter(
            Post.post_message.like("%{}%".format(motclef))
        ).paginate(page=page, per_page=RESULTATS_PAR_PAGE)
        titre = "Résultat pour la recherche `" + motclef + "`"

    return render_template(
        "pages/recherche/recherche_posts.html",
        resultats=resultats,
        titre=titre,
        keyword=motclef,
        nom="Recherche"
    )


@app.route("/recherche/utilisateurs")
@login_required
def recherche_utilisateurs():
    """ Route permettant la recherche d'utilisateurs
    """
    # On préfèrera l'utilisation de .get() ici
    #   qui nous permet d'éviter un if long (if "clef" in dictionnaire and dictonnaire["clef"])
    motclef = request.args.get("keyword", None)
    page = request.args.get("page", 1)

    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    # On crée une liste vide de résultat (qui restera vide par défaut
    #   si on n'a pas de mot clé)
    resultats = []

    # On fait de même pour le titre de la page
    titre = "Recherche"
    if motclef:
        resultats = User.query.filter(
            User.user_name.like("%{}%".format(motclef))
        ).paginate(page=page, per_page=RESULTATS_PAR_PAGE)
        titre = "Résultat pour la recherche `" + motclef + "`"

    return render_template(
        "pages/recherche/recherche_utilisateurs.html",
        utilisateurs=resultats,
        titre=titre,
        keyword=motclef,
        nom="Recherche"
    )


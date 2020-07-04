from ..app import app, db
from flask import render_template, flash, redirect, request, url_for, abort
from flask_login import current_user, login_required
from ..modeles.utilisateurs import EditProfileForm, CVForm, CompetencesForm
from ..modeles.donnees import Post, User, Comment, CV, Competences
from ..modeles.utilitaires import get_first_image
from ..constantes import POSTS_PAR_PAGE

"""
par ordre d'apparition:
/utilisateur/<user_name>
/editer_profil/<user_name>
/editer_profil/<user_name>/competences
/editer_profil/<user_name>/CV
/editer_profil/<user_name>/CV/<int:id>
"""

@app.route('/utilisateur/<user_name>')
def utilisateur(user_name):
    """
    Permet d'afficher le profil de l'utilisateur
    :param user_name: nom de l'utilisateur
    :type user_name: str
    :return: template utilisateur.html
    :rtype: template
    """
    # gestion de la pagination
    page = request.args.get("page", 1)
    # récupération de l'utilisateur à partir du paramètre fourni
    utilisateur = User.query.filter_by(user_name=user_name).first_or_404()
    # récupération des posts de l'utilisateur
    posts = utilisateur.posts.order_by(Post.post_date.desc()).paginate(page=int(page), per_page=int(POSTS_PAR_PAGE))

    # pour afficher la date du dernier commentaire
    # création d'un dictionnaire vide dans lequel seront mis l'id du post en clé, et l'id du commentaire en valeur
    dernier_commentaire = {}
    liste_posts = Post.query.all()
    for post in liste_posts:
        last_comment = post.comments.order_by(Comment.comment_date.desc()).first()
        dernier_commentaire[post.post_id] = last_comment

    # classement des expériences par ordre chronologique dans cvs_classes
    cvs_classes = utilisateur.cvs.order_by(CV.cv_annee_debut.desc()).all()

    # comptage du nombre d'expériences
    compteur_experiences = utilisateur.cvs.count()

    # comptage du nombre de posts de l'utilisateur
    compteur_posts = utilisateur.posts.count()

    # récupération des compétences de l'utilisateur
    competences = utilisateur.competences.all()
    # création d'un dictionnaire vide qui aura comme clé la compétence et comme valeur l'url de l'image
    dictionnaire_distinct = {}

    for competence in competences:
        # si la compétence de l'utilisateur n'est pas présente dans la liste, alors il est ajouté; s'il y est, alors il n'y est pas ajouté
        if competence.competence_label not in dictionnaire_distinct:
            # récupération de l'image
            image = get_first_image(competence.competence_label)
            # remplissage du dictionnaire
            dictionnaire_distinct[competence.competence_label] = image

    # récupération des lieux de travail de l'utilisateur dans un dictionnaire avec la ville en clé et l'url de l'image en valeur
    lieux_travail = {}
    for cv in cvs_classes:
        if cv.cv_ville not in lieux_travail:
            # récupération de l'image
            image = get_first_image(cv.cv_ville)
            # remplissage du dictionnaire
            lieux_travail[cv.cv_ville] = image

    return render_template("pages/profil_utilisateur/utilisateur.html",
                           nom=user_name,
                           user=utilisateur,
                           dernier_commentaire=dernier_commentaire,
                           posts=posts.items,
                           pagination=posts,
                           cvs_classes=cvs_classes,
                           compteur_experiences=compteur_experiences,
                           compteur_posts=compteur_posts,
                           dictionnaire_competences=dictionnaire_distinct,
                           images_lieux=lieux_travail)


@app.route('/editer_profil/<user_name>', methods=['GET', 'POST'])
@login_required
def editer_profil(user_name):
    """
    Route permettant de modifier ses données personnelles de son profil
    :return: template editer.html de la page d'édition du profil avec le formulaire
    :rtype: template
    """
    # récupération de l'utilisateur à partir du paramètre fourni
    utilisateur = User.query.filter_by(user_name=user_name).first_or_404()
    # utilisation du formulaire de la classe EditProfileForm
    form = EditProfileForm()
    # validate_on_submit fonctionne avec la méthode POST
    if form.validate_on_submit():
        # ajout des données dans la base de données
        current_user.user_name = form.user_name.data
        current_user.user_firstname = form.user_firstname.data
        current_user.user_surname = form.user_surname.data
        current_user.user_mail = form.user_mail.data
        current_user.user_promotion_date = form.user_promotion_date.data
        current_user.user_birthyear = form.user_birthyear.data
        current_user.user_description = form.user_description.data
        # ces deux lignes permettent d'éviter à l'utilisateur de rentrer l'url de ses profils, seul l'identifiant/pseudo des comptes suffit
        current_user.user_linkedin = "https://www.linkedin.com/in/" + form.user_linkedin.data
        current_user.user_github = "https://www.github.com/" + form.user_github.data
        # commit des données
        db.session.commit()
        flash("Modifications enregistrées")
        return redirect(url_for('utilisateur', user_name=current_user.user_name))
    # permet l'affichage des données pré-existantes dans le formulaire
    elif request.method == 'GET':
        form.user_name.data = current_user.user_name
        form.user_description.data = current_user.user_description
        form.user_firstname.data = current_user.user_firstname
        form.user_surname.data = current_user.user_surname
        form.user_promotion_date.data = current_user.user_promotion_date
        form.user_mail.data = current_user.user_mail
        form.user_birthyear.data = current_user.user_birthyear
        form.user_linkedin.data = current_user.user_linkedin
        form.user_github.data = current_user.user_github

    return render_template('pages/profil_utilisateur/editer.html',
                           nom="Editer le profil",
                           form=form,
                           user=utilisateur)

@app.route('/editer_profil/<user_name>/competences', methods=['GET', 'POST'])
@login_required
def editer_competences(user_name):
    """
        Route permettant de modifier ses données personnelles de son profil
        :return: template editer.html de la page d'édition du profil avec le formulaire
        :rtype: template
        """
    # récupération de l'utilisateur à partir du paramètre fourni
    utilisateur = User.query.filter_by(user_name=user_name).first_or_404()
    # gestion du formulaire de premier message privé avec un utilisateur
    competences_disponibles = Competences.query.all()
    # création de la liste de tuples pour le RadioField du formulaire
    competences_liste = [(c.competence_id, c.competence_label) for c in competences_disponibles]
    # utilisation du formulaire de la classe EditProfileForm
    form = CompetencesForm()
    # passage de la liste dans le formulaire
    form.competences.choices = competences_liste
    # validate_on_submit fonctionne avec la méthode POST
    if form.validate_on_submit():
        competence = form.competences.data
        requete = 'INSERT INTO skills VALUES (' + str(current_user.id) + ',' + str(competence) + ')'
        db.engine.execute(requete)
        flash("Modifications enregistrées")
        return redirect(url_for('utilisateur', user_name=current_user.user_name))
    # permet l'affichage des données pré-existantes dans le formulaire
    #elif request.method == 'GET':
        #form.user_name.data = current_user.user_name
    return render_template('pages/profil_utilisateur/editer_competences.html',
                           nom="Editer les compétences",
                           form=form,
                           user=utilisateur)


@app.route('/editer_profil/<user_name>/CV', methods=['GET', 'POST'])
@login_required
def editer_profil_cv(user_name):
    """
    Permet d'ajouter une expérience professionnelle sur son profil
    :return: template editer_cv.html
    :rtype: template
    """
    # récupération de l'utilisateur à partir du paramètre fourni
    utilisateur = User.query.filter_by(user_name=user_name).first_or_404()
    # utilisation du formulaire de classe CVForm
    form = CVForm()
    # validate_on_submit fonctionne avec la méthode POST
    if form.validate_on_submit():
        # la variable cv permet de stocker les données ajoutées en attendant d'être entrées dans la base de données
        cv = CV(cv_nom_poste=form.cv_nom_poste.data,
                cv_nom_employeur=form.cv_nom_employeur.data,
                cv_ville=form.cv_ville.data,
                cv_annee_debut=int(form.cv_annee_debut.data),
                cv_annee_fin=int(form.cv_annee_fin.data),
                cv_description_poste=form.cv_description_poste.data,
                utilisateur=utilisateur)
        # ajout et commit des données dans la base de données
        db.session.add(cv)
        db.session.commit()
        flash("Cette expérience a bien été ajoutée")
        return redirect(url_for('utilisateur', user_name=current_user.user_name))

    # classement des expériences par ordre chronologique dans cvs_classes
    cvs_classes = utilisateur.cvs.order_by(CV.cv_annee_debut.desc()).all()

    return render_template('pages/profil_utilisateur/editer_cv.html',
                           nom="Editer mes expériences",
                           cvs_classes=cvs_classes,
                           form=form,
                           user=utilisateur)


@app.route('/editer_profil/<user_name>/CV/<int:id>', methods=['GET', 'POST'])
@login_required
def editer_cv(user_name, id):
    """
    Route permettant de modifier une expérience professionnelle, seulement si l'on est connecté et l'auteur de l'expérience
    :param id: id de l'expérience professionnelle
    :type id: int
    :return: template editer_cv.html
    :rtype: template
    """
    # récupération de l'utilisateur à partir du paramètre fourni
    utilisateur = User.query.filter_by(user_name=user_name).first_or_404()
    # récupération de l'expérience grâce à son id
    cv = CV.query.get_or_404(id)
    # vérification que l'utilisateur actuel est bien l'auteur de l'expérience
    if current_user != cv.utilisateur:
        abort(403)

    # utilisation du formulaire de classe CVForm
    form = CVForm()
    # validate_on_submit fonctionne avec la méthode POST
    if form.validate_on_submit():
        # récupération des données du formulaire pour les faire correspondre aux champs de la base de données
        cv.cv_nom_poste=form.cv_nom_poste.data
        cv.cv_nom_employeur=form.cv_nom_employeur.data
        cv.cv_ville=form.cv_ville.data
        cv.cv_annee_debut=int(form.cv_annee_debut.data)
        cv.cv_annee_fin=int(form.cv_annee_fin.data)
        cv.cv_description_poste=form.cv_description_poste.data
        cv.utilisateur=current_user
        # ajout et commit des modifications
        db.session.add(cv)
        db.session.commit()
        flash("Cette expérience a bien été modifiée")
        return redirect(url_for('utilisateur', user_name=current_user.user_name))
    # permet le remplissage des champs du formulaire avec les données pré-existantes
    form.cv_nom_poste.data = cv.cv_nom_poste
    form.cv_nom_employeur.data = cv.cv_nom_employeur
    form.cv_ville.data = cv.cv_ville
    form.cv_annee_debut.data = cv.cv_annee_debut
    form.cv_annee_fin.data = cv.cv_annee_fin
    form.cv_description_poste.data = cv.cv_description_poste

    # classement des expériences par ordre chronologique dans cvs_classes
    cvs_classes = current_user.cvs.order_by(CV.cv_annee_debut.desc()).all()

    return render_template('pages/profil_utilisateur/editer_cv.html',
                           nom="Editer mes expériences",
                           cvs_classes=cvs_classes,
                           form=form,
                           user=utilisateur)
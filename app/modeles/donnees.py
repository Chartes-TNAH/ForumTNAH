from ..app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from markdown import markdown
import bleach


# création de la table d'association des followers
followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
                     )

# création de la table d'association des compétences des utilisateurs
skills = db.Table('skills',
                  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                  db.Column('competence_id', db.Integer, db.ForeignKey('competences.competence_id'))
                  )


# création de la table user pour les informations sur l'utilisateur
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # pseudo de l'utilisateur
    user_name = db.Column(db.String(64), index=True, unique=True)
    # identité réelle de l'utilisateur
    user_firstname = db.Column(db.String(64), index=True)
    user_surname = db.Column(db.String(64), index=True)

    user_mail = db.Column(db.String(120), index=True, unique=True)
    user_password_hash = db.Column(db.String(128))

    user_birthyear = db.Column(db.Integer)
    user_promotion_date = db.Column(db.String(9))
    user_description = db.Column(db.String(140))
    user_last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    user_linkedin = db.Column(db.String(120))
    user_github = db.Column(db.String(120))

    # jointures avec les autres tables
    posts = db.relationship("Post", backref='auteur', lazy='dynamic')

    comments = db.relationship('Comment', backref='auteur', lazy='dynamic')

    cvs = db.relationship("CV", backref='utilisateur', lazy='dynamic')

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic'
    )

    competences = db.relationship('Competences', secondary=skills, backref=db.backref('utilisateur', lazy='dynamic'), lazy='dynamic')

    def get_id(self):
        """
        Retourne l'id de l'objet utilisé
        :return: ID de l'utilisateur
        :rtype: int
        """
        return self.id

    def avatar(self, size):
        """
        Fonction permettant de récupérer le lien vers la photo Gravatar de l'utilisateur à partir de son adresse mail;
        une icone neutre apparaît si l'utilisateur n'a pas de profil Gravatar
        :param size: taille en pixels de l'icône que l'on souhaite
        :type size: int
        :return: lien vers l'icône Gravatar
        :rtype: str
        """
        # hashage de l'adresse email conformément à Gravatar
        digest = md5(self.user_mail.lower().encode('utf-8')).hexdigest()
        # création du lien
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    #gestion des mots de passe
    def set_password(self, password):
        """
        Permet de générer un mot de passe hashé
        :param password: mot de passe rentré dans les formulaires
        :type password: str
        :return: None
        :rtype: None
        """
        self.user_password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Permet de vérifier l'exactitude du mot de passe avec le hash stocké en base de données
        :param password: mot de passe rentré dans le formulaire
        :type password: str
        :return: true si le mot de passe est correct, false s'il ne l'est pas
        :rtype: bool
        """
        return check_password_hash(self.user_password_hash, password)

    # met à jour la date de dernière visite dès lors qu'une action est effectuée sur le profil
    def ping(self):
        """
        Permet de mettre à jour la date de dernière visite quand on modifie le profil
        :return: None
        :rtype: None
        """
        self.user_last_seen = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    # gestion des fonctions de suivi des utilisateurs entre eux
    def follow(self, user):
        """
        Fonction de suivi d'un utilisateur
        :param user: nom de l'utilisateur à suivre
        :type user: str
        :return: None
        :rtype: None
        """
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        """
        Fonction d'arrêt de suivi d'un utilisateur
        :param user: nom de l'utilisateur à ne plus suivre
        :type user: str
        :return: None
        :rtype: None
        """
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        """
        Permet de chercher les utilisateurs qui suivent
        :param user: nom de l'utilisateur
        :type user: str
        :return: True si la relation existe
        :rtype: bool
        """
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        """
        Fonction permettant de récupérer les posts des personnes suivies
        """
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.post_auteur)).filter(
                followers.c.follower_id == self.id)
        miens = Post.query.filter_by(post_auteur=self.id)
        return followed.union(miens).order_by(Post.post_date.desc())

# création de la table des posts
class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_titre = db.Column(db.String(70))
    post_message = db.Column(db.Text)
    post_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    html = db.Column(db.Text)

    # jointures avec les autres tables
    post_auteur = db.Column(db.Integer, db.ForeignKey('user.id'))

    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    # gestion de la saisie MarkDown
    @staticmethod
    def au_changement(target, value, oldvalue, initiator):
        """
        Permet de convertir le MarkDown en HTML à chaque fois qu'un changement est effectué dans le champ html de la table
        """
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i',
                        'li', 'ol', 'ul', 'pre', 'strong', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        # la fonction markdown fait une conversion en html; la fonction clean permet de nettoyer le code des balises qui ne sont pas dans
        # allowed_tags; linkify fait la conversion des URL en balises <a>
        target.html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True
        ))

db.event.listen(Post.post_message, 'set', Post.au_changement)


# création de la table des commentaires
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_message = db.Column(db.Text)
    comment_html = db.Column(db.Text)
    comment_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    comment_auteur = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment_post = db.Column(db.Integer, db.ForeignKey('post.post_id'))

    @staticmethod
    def au_changement(target, value, oldvalue, initiator):
        """
        Permet de convertir le MarkDown en HTML à chaque fois qu'un changement est effectué dans le champ html de la table
        """
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i',
                        'li', 'ol', 'ul', 'pre', 'strong', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        # la fonction markdown fait une conversion en html; la fonction clean permet de nettoyer le code des balises qui ne sont pas dans
        # allowed_tags; linkify fait la conversion des URL en balises <a>
        target.comment_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True
        ))

db.event.listen(Comment.comment_message, 'set', Comment.au_changement)


# création de la table des expériences professionnelles
class CV(db.Model):
    cv_id = db.Column(db.Integer, primary_key=True)
    cv_nom_poste = db.Column(db.Text)
    cv_nom_employeur = db.Column(db.Text)
    cv_ville = db.Column(db.String(64))
    cv_annee_debut = db.Column(db.Integer)
    cv_annee_fin = db.Column(db.Integer)
    cv_description_poste = db.Column(db.Text)

    cv_utilisateur = db.Column(db.Integer, db.ForeignKey('user.id'))


# création de la table des compétences
class Competences(db.Model):
    competence_id = db.Column(db.Integer, primary_key=True)
    competence_label = db.Column(db.String(48))


@login.user_loader
def get_user_by_id(id):
        return User.query.get(int(id))
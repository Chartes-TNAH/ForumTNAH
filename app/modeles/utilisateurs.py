from ..app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


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

    posts = db.relationship("Post", backref='author', lazy='dynamic')

    @staticmethod
    def identification(user_name, password):
        """ Identifie un utilisateur. Si cela fonctionne, renvoie les données de l'utilisateur.

        :param user_name: Nom de l'utilisateur
        :param password: Mot de passe envoyé par l'utilisateur
        :returns: Si réussite, données de l'utilisateur. Sinon None
        :rtype: User or None
        """
        user_name = User.query.filter(User.user_name == user_name).first()
        if user_name and check_password_hash(user_name.user_password_hash, password):
            return user_name
        return None

    @staticmethod
    def creer(user_name, user_mail, user_firstname, user_surname, user_password):
        """ Crée un compte utilisateur. Retourne un tuple (booléen, User ou liste).
        Si il y a une erreur, la fonction renvoie False suivi d'une liste d'erreur
        Sinon, elle renvoie True suivi de la donnée enregistrée

        :param user_name: Login de l'utilisateur
        :param user_mail: Email de l'utilisateur
        :param user_firstname: Prénom de l'utilisateur
        :param user_surname: Nom de l'utilisateur
        :param user_password: Mot de passe de l'utilisateur

        """
        erreurs = []
        if not user_name:
            erreurs.append("Le nom d'utilisateur fourni est vide")
        if not user_mail:
            erreurs.append("L'email fourni est vide")
        if not user_firstname:
            erreurs.append("Le prénom fourni est vide")
        if not user_surname:
            erreurs.append('Le nom est vide')
        if not user_password or len(user_password) < 5:
            erreurs.append("Le mot de passe fourni est vide ou trop court")

        # On vérifie que personne n'a utilisé cet email ou ce login
        uniques = User.query.filter(
            db.or_(User.user_mail == user_mail, User.user_name == user_name)
        ).count()
        if uniques > 0:
            erreurs.append("L'email ou le login sont déjà inscrits dans notre base de données")

        # Si on a au moins une erreur
        if len(erreurs) > 0:
            return False, erreurs

        # On crée un utilisateur
        utilisateur = User(
            user_name=user_name,
            user_firstname=user_firstname,
            user_surname=user_surname,
            user_mail=user_mail,
            user_password_hash=generate_password_hash(user_password)
        )

        try:
            # On l'ajoute au transport vers la base de données
            db.session.add(utilisateur)
            # On envoie le paquet
            db.session.commit()

            # On renvoie l'utilisateur
            return True, utilisateur
        except Exception as erreur:
            return False, [str(erreur)]

    def get_id(self):
        """
        Retourne l'id de l'objet utilisé
        :return: ID de l'utilisateur
        :rtype: int
        """
        return self.id

    # met à jour la date de dernière visite dès lors qu'une action est effectuée sur le profil
    def ping(self):
        self.user_last_seen=datetime.utcnow()
        db.session.add(self)
        db.session.commit()

@login.user_loader
def get_user_by_id(id):
        return User.query.get(int(id))
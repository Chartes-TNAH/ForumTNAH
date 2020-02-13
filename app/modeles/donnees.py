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

    def set_password(self, password):
        self.user_password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.user_password_hash, password)

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

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_statuse = db.Column(db.Boolean)
    post_message = db.Column(db.Text)
    post_markdown = db.Column(db.Boolean)
    post_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    creator = db.Column(db.Integer, db.ForeignKey('user.id'))


@login.user_loader
def get_user_by_id(id):
        return User.query.get(int(id))
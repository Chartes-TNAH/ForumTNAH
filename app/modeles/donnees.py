from ..app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from markdown import markdown
import bleach

followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
                     )

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

    posts = db.relationship("Post", backref='auteur', lazy='dynamic')

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic'
    )

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
        une icone neutre si l'utilisateur n'a pas de profil Gravatar
        """
        digest = md5(self.user_mail.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    #gestion des mots de passe
    def set_password(self, password):
        self.user_password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.user_password_hash, password)

    # met à jour la date de dernière visite dès lors qu'une action est effectuée sur le profil
    def ping(self):
        self.user_last_seen=datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    #gestion des fonctions de suivis des utilisateurs entre eux
    def follow(self,user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
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

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_titre = db.Column(db.String(70))
    post_message = db.Column(db.Text)
    post_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    post_auteur = db.Column(db.Integer, db.ForeignKey('user.id'))

    html = db.Column(db.Text)

    @staticmethod
    def au_changement(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i',
                        'li', 'ol', 'ul', 'pre', 'strong', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        target.html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True
        ))

db.event.listen(Post.post_message, 'set', Post.au_changement)


@login.user_loader
def get_user_by_id(id):
        return User.query.get(int(id))
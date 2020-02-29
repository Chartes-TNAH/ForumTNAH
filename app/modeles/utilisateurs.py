from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from app.modeles.donnees import User
from flask_pagedown.fields import PageDownField

class LoginForm(FlaskForm):
    user_name = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    user_password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de moi')
    submit = SubmitField('Connexion')

class RegistrationForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    password2 = PasswordField('Mot de passe', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('S\'inscrire')

    def validate_username(self, username):
        user = User.query.filter_by(user_name=username.data).first()
        if user is not None:
            raise ValidationError('Nom d\'utilisateur déjà enregistré')

    def validate_email(self, email):
        user = User.query.filter_by(user_mail=email.data).first()
        if user is not None:
            raise ValidationError('Adresse email déjà enregistrée')

class EditProfileForm(FlaskForm):
    user_name = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    user_mail = StringField('Email', validators=[DataRequired(), Email()])
    user_surname = StringField('Nom', validators=[DataRequired()])
    user_firstname = StringField('Prénom', validators=[DataRequired()])
    user_linkedin = StringField('URL vers mon profil LinkedIn')
    user_github = StringField('URL vers mon compte Github')
    user_birthyear = StringField('Année de naissance', validators=[DataRequired()])
    user_promotion_date = StringField('Promotion (année du diplôme)')
    user_description = TextAreaField('Description')
    submit = SubmitField('Mettre à jour')

class PostForm(FlaskForm):
    titre = StringField('Titre de la discussion', validators=[DataRequired()])
    message = PageDownField("Ecrivez ici votre message (MarkDown possible)", validators=[DataRequired()])
    submit = SubmitField('Envoyer')

class CommentForm(FlaskForm):
    message = PageDownField("Votre commentaire", validators=[DataRequired()])
    submit = SubmitField('Commenter')

class CVForm(FlaskForm):
    cv_nom_poste = StringField('Dénomination du poste', validators=[DataRequired()])
    cv_nom_employeur = StringField("Nom de l'entreprise ou du service", validators=[DataRequired()])
    cv_ville = StringField('Nom de la ville', validators=[DataRequired()])
    cv_annee_debut = StringField("Année de début d'exercice", validators=[DataRequired()])
    cv_annee_fin = StringField("Année de fin d'exercice", validators=[DataRequired()])
    cv_description_poste = TextAreaField('Description des missions du poste')
    submit = SubmitField('Enregistrer')
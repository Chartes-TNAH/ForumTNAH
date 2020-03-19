from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired
from app.modeles.donnees import User
from flask_pagedown.fields import PageDownField

# création de la classe du formulaire pour la connexion
class LoginForm(FlaskForm):
    user_name = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    user_password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de moi')

    submit = SubmitField('Connexion')


# création de la classe du formulaire pour l'inscription
class RegistrationForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    # vérification que le mot de passe fourni la deuxième fois est le même que celui fourni la première fois
    password2 = PasswordField('Mot de passe', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('S\'inscrire')

    # vérification que le nom d'utilisateur n'existe pas
    def validate_username(self, username):
        """
        Permet de vérifier que le nom d'utilisateur donné n'existe pas déjà
        :param username: nom de l'utilisateur
        :type username: str
        :return: None
        :rtype: None
        """
        # récupération du premier utilisateur dont le nom est le même que celui donné en paramètre
        user = User.query.filter_by(user_name=username.data).first()
        # s'il y a un retour d'un utilisateur, alors une erreur s'affiche
        if user is not None:
            raise ValidationError('Nom d\'utilisateur déjà enregistré')

    def validate_email(self, email):
        """
        Permet de vérifier que le mail fourni n'existe pas déjà
        :param email: adresse email de l'utilisateur
        :type email: str
        :return: None
        :rtype: None
        """
        # récupération du premier mail identique à celui fourni en paramètre
        mail = User.query.filter_by(user_mail=email.data).first()
        # s'il y a un retour d'une adresse mail, alors une erreur s'affiche
        if mail is not None:
            raise ValidationError('Adresse email déjà enregistrée')


# création de la classe du formulaire pour l'édition du profil de l'utilisateur
class EditProfileForm(FlaskForm):
    user_name = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    user_mail = StringField('Email', validators=[DataRequired(), Email()])
    user_surname = StringField('Nom', validators=[DataRequired()])
    user_firstname = StringField('Prénom', validators=[DataRequired()])
    user_linkedin = StringField('Identifiant de mon profil LinkedIn')
    user_github = StringField('Identifiant de mon compte Github')
    user_birthyear = StringField('Année de naissance', validators=[DataRequired()])
    user_promotion_date = StringField('Promotion (année du diplôme)')
    user_description = TextAreaField('Description')

    submit = SubmitField('Mettre à jour')


# création de la classe du formulaire pour publier un post
class PostForm(FlaskForm):
    titre = StringField('Titre de la discussion', validators=[DataRequired()])
    message = PageDownField("Ecrivez ici votre message (MarkDown possible)", validators=[DataRequired()])
    indexation = StringField("Ecrivez ici un mot clé", validators=[DataRequired()])

    submit = SubmitField('Envoyer')


# création de la classe du formulaire pour l'écriture d'un commentaire
class CommentForm(FlaskForm):
    message = PageDownField("Votre commentaire", validators=[DataRequired()])

    submit = SubmitField('Commenter')


# création de la classe du formulaire pour l'édition d'une expérience professionnelle
class CVForm(FlaskForm):
    cv_nom_poste = StringField('Dénomination du poste', validators=[DataRequired()])
    cv_nom_employeur = StringField("Nom de l'entreprise ou du service", validators=[DataRequired()])
    cv_ville = StringField('Nom de la ville', validators=[DataRequired()])
    cv_annee_debut = StringField("Année de début d'exercice", validators=[DataRequired()])
    cv_annee_fin = StringField("Année de fin d'exercice", validators=[DataRequired()])
    cv_description_poste = TextAreaField('Description des missions du poste')

    submit = SubmitField('Enregistrer')

# création de la classe du formulaire pour le choix des compétences principales
class CompetencesForm(FlaskForm):
    competences = RadioField('competences', choices=[
        ('1', 'IIIF'),
        ('2', 'Python'),
        ('3', "SQL")
    ])

    submit = SubmitField('Enregistrer')

# création de la classe du formulaire d'écriture d'un premier message de conversation privée
class AddConversationForm(FlaskForm):
    destinataire_id = SelectField('Destinataire', coerce=int, validators=[InputRequired()])
    message = PageDownField("Ecrivez ici votre message (MarkDown possible)", validators=[DataRequired()])

    submit = SubmitField('Envoyer')
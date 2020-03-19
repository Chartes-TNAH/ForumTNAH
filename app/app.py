from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
from .constantes import SECRET_KEY
from flask_pagedown import PageDown

# définition des chemins
chemin_actuel =os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

app = Flask(
    "Application",
    template_folder=templates,
    static_folder=statics
)

# configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqlite'
# désactivation du tracking des modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initiation de SQLAlchemy
db = SQLAlchemy(app)

# On configure la clé secrète
app.config['SECRET_KEY'] = SECRET_KEY

migrate = Migrate(app, db)

# pour la gestion des utilisateurs
login = LoginManager(app)

#pour la saisie en MarkDown
pagedown = PageDown(app)

from .routes import generales, erreurs, posts, profil_utilisateur, messagerie
from app.app import app, db
from app.constantes import DEBUG
from app.sql_initilisation import users, posts, comments, cvs, competences, skills, messages, followers

if __name__ == "__main__":
    print("Initialisation de la base de données en cours...")
    db.drop_all()
    print("Création des tables de la base de données...")
    db.create_all()
    print("Insertion de données utilisateurs tests...")
    db.engine.execute(users)
    print("Insertion de posts tests...")
    db.engine.execute(posts)
    print("Insertion de commentaires tests...")
    db.engine.execute(comments)
    print("Insertion de expériences utilisateurs tests...")
    db.engine.execute(cvs)
    print("Insertion de compétences tests...")
    db.engine.execute(competences)
    print("Insertion de compétences utilisateurs tests...")
    db.engine.execute(skills)
    print("Insertion de messages personnels tests...")
    db.engine.execute(messages)
    print("Insertion de suivis entre utilisateurs tests...")
    db.engine.execute(followers)
    app.run(debug=DEBUG)
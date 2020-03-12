from app.app import app, db
from app.constantes import DEBUG
from app.sql_initilisation import users, posts, comments, cvs, competences

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    db.engine.execute(users)
    db.engine.execute(posts)
    db.engine.execute(comments)
    db.engine.execute(cvs)
    db.engine.execute(competences)
    app.run(debug=DEBUG)
from app.app import app, db
from app.constantes import DEBUG
from app.sql_initilisation import users, posts, comments, cvs, competences, skills, messages

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    db.engine.execute(users)
    db.engine.execute(posts)
    db.engine.execute(comments)
    db.engine.execute(cvs)
    db.engine.execute(competences)
    db.engine.execute(skills)
    db.engine.execute(messages)
    app.run(debug=DEBUG)
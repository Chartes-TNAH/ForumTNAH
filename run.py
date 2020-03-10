from app.app import app, db
from app.sql_initilisation import users, posts, comments, cvs

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    # db.engine.execute('SQL ici'); hashage du mdp Maxime pbkdf2:sha256:150000$koCdnv2k$8cb86eb992afe0931cb2315daaac22c1a29655d55b1b57d028d17db354bcf23a
    db.engine.execute(users)
    db.engine.execute(posts)
    db.engine.execute(comments)
    db.engine.execute(cvs)
    app.run(debug=True)
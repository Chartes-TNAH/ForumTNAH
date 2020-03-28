from app.app import app, db
from app.constantes import DEBUG, SQL_INIT
from tqdm import tqdm
import os

if __name__ == "__main__":
    print("Initialisation de la base de données en cours")
    db.drop_all()
    print("Création des tables de la base de données")
    db.create_all()
    # insertion des données d'exemple
    for fichier in tqdm(os.listdir(SQL_INIT)):
        with open(SQL_INIT + fichier, 'r') as f:
            print("Insertion de données d'exemple dans la table  " + fichier.replace('.sql', ''))
            for line in tqdm(f):
                db.engine.execute(line)
    app.run(debug=DEBUG)
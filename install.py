from app.app import app, init_db
from app.constantes import DEBUG

if __name__ == "__main__":
    init_db()
    # app.run(debug=DEBUG)
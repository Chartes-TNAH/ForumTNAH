from ..app import db
from datetime import datetime

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_statuse = db.Column(db.Boolean)
    post_message = db.Column(db.Text)
    post_markdown = db.Column(db.Boolean)
    post_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    creator = db.Column(db.Integer, db.ForeignKey('user.id'))
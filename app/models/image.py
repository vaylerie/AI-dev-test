from models.db import db

class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer(), primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    filepath = db.Column(db.String(255), nullable=True)

import imp
from run import db

class Messages(db.Model):
    Id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name=db.Column(db.String(50), nullable=False)
    Email=db.Column(db.String(50), nullable=False)
    Subject=db.Column(db.String(50), nullable=False)
    Message=db.Column(db.String(255), nullable=False)
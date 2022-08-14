from run import db

class Messages(db.Model):
    Id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name=db.Column(db.String(50), nullable=False)
    Email=db.Column(db.String(50), nullable=False)
    Subject=db.Column(db.String(50), nullable=False)
    Message=db.Column(db.String(255), nullable=False)

class NavLinks(db.Model):
    Id=db.Column(db.Integer, primary_key=True)
    Name=db.Column(db.String(25), nullable=False)
    Url=db.Column(db.String(50), nullable=False)
    Order=db.Column(db.Integer, nullable=False)
    IsActive=db.Column(db.Boolean, nullable=False)
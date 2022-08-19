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

class Teams(db.Model):
    Id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name=db.Column(db.String(50))
    Profession=db.Column(db.String(50))
    Image=db.Column(db.String(100))
    TwitterAdress=db.Column(db.String(50))
    FacebookAdress=db.Column(db.String(50))
    InstagramAdress=db.Column(db.String(50))
    LinkedinAdress=db.Column(db.String(50))
    Order=db.Column(db.Integer)
    IsActive=db.Column(db.Boolean)
class PortfolioCategory(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50))
    portfolios=db.relationship('Portfolio', backref='portfolio_category', lazy=True)
class Portfolio(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(25))
    Category_id=db.Column(db.Integer, db.ForeignKey('portfolio_category.Id'))
    img=db.Column(db.String(50))
    info=db.Column(db.String(100))
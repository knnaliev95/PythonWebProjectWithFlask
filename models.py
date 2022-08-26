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
    images=db.relationship('TeamImages', backref='team_images', lazy=True)

class TeamImages(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Teamsid=db.Column(db.Integer, db.ForeignKey('teams.Id'))
    image=db.Column(db.String(50))

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

class FeaturedServices(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    icon=db.Column(db.String(50))
    name=db.Column(db.String(50))
    info=db.Column(db.String(250))

class Clients(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    image=db.Column(db.String(50))

class Features(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50))
    icon=db.Column(db.String(50))
    info=db.Column(db.String(250))
    image=db.Column(db.String(50))
    options=db.relationship('FeatureOptions', backref='feature_options', lazy=True)

class FeatureOptions(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    features_id=db.Column(db.Integer, db.ForeignKey('features.Id'))
    option=db.Column(db.String(150))

class Services(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50))
    info=db.Column(db.String(250))
    icon=db.Column(db.String(50))
    image=db.Column(db.String(50))

class Testimanials(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50))
    profession=db.Column(db.String(50))
    info=db.Column(db.String(150))

class Pricing(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50))
    amount=db.Column(db.Integer)
    options=db.relationship('PricingOptions', backref='pricing_options', lazy=True)

class PricingOptions(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    pricing_id=db.Column(db.Integer, db.ForeignKey('pricing.Id'))
    option=db.Column(db.String(50))

class Blogs(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50))
    header=db.Column(db.String(150))
    info=db.Column(db.String(250))

class OurInformations(db.Model):
    Id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    location=db.Column(db.String(150))
    email=db.Column(db.String(50))
    phone=db.Column(db.String(50))

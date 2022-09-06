from flask import Flask,render_template
from peoples import peoples_bp

@peoples_bp.route('/', methods=['GET','POST'])
def peoples_index():
    from run import db
    from models import Teams,Portfolio,PortfolioCategory,Clients,FeaturedServices,Services,Pricing,PricingOptions,NavLinks,Testimanials
    from admin.forms import MessageForm
    messageForm=MessageForm()
    navlinks=NavLinks.query.all()
    teams=Teams.query.filter_by(IsActive=True).order_by(Teams.Order)
    portfolios=Portfolio.query.all()
    categories=PortfolioCategory.query.all()
    clients=Clients.query.all()
    featuredservices=FeaturedServices.query.all()
    services=Services.query.all()
    pricings=Pricing.query.all()
    testimonials=Testimanials.query.all()
    return render_template('peoples/index.html',messageForm=messageForm, navlinks=navlinks, teams=teams,portfolios=portfolios,categories=categories,PortfolioCategory=PortfolioCategory,clients=clients,featuredservices=featuredservices,services=services,pricings=pricings,pricingoptions=PricingOptions,testimonials=testimonials)
from flask import Flask,render_template
from peoples import peoples_bp

@peoples_bp.route('/', methods=['GET','POST'])
def peoples_index():
    from run import db
    from models import Teams,Portfolio,PortfolioCategory,Clients,FeaturedServices,Services,Pricing,PricingOptions,NavLinks,Testimanials
    from models import Features,FeatureOptions,Blogs,OurInformations
    from admin.forms import MessageForm
    context={
        'navlinks':NavLinks.query.all(),
        'teams':Teams.query.filter_by(IsActive=True).order_by(Teams.Order),
        'portfolios':Portfolio.query.all(),
        'categories':PortfolioCategory.query.all(),
        'clients':Clients.query.all(),
        'featuredservices':FeaturedServices.query.all(),
        'services':Services.query.all(),
        'pricings':Pricing.query.all(),
        'testimonials':Testimanials.query.all(),
        'featuresOne':Features.query.filter_by(order=1).first(),
        'features':Features.query.order_by(Features.order).all()[1:],
        'FeatureOtionsOne':FeatureOptions.query.filter_by(features_id=Features.query.filter_by(order=1).first().Id).first(),
        'FeatureOptionsAll':FeatureOptions.query.all()[1:],
        'FeatureOptions':FeatureOptions,
        'FeatuersModel':Features,
        'blogs':Blogs.query.all(),
        'information':OurInformations.query.first(),
        'messageForm':MessageForm(),
        'PortfolioCategory':PortfolioCategory,
        'pricingoptions':PricingOptions    
    }
    return render_template('peoples/index.html',**context)
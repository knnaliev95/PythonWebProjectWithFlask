from flask import render_template,redirect,request
from admin import admin_bp
from models import *
from admin.forms import *
import os
import random
from werkzeug.utils import secure_filename

@admin_bp.route('/', methods=['GET','POST'])
def index():
    return render_template('admin/index.html')

# Messages start
@admin_bp.route('/messages')
def messages():
    messages=Messages.query.all()
    return render_template('admin/messages/messages.html', messages=messages)

@admin_bp.route('/message/add', methods=['GET','POST'])
def message_add():
    from run import db
    messageForm=MessageForm()
    if request.method=='POST':
        message=Messages(
            Name=messageForm.name.data,
            Email=messageForm.email.data,
            Subject=messageForm.subject.data,
            Message=messageForm.message.data
        )
        db.session.add(message)
        db.session.commit()
        return redirect('/')

@admin_bp.route('/message/delete/<id>', methods=['GET','POST'])
def message_delete(id):
    from run import db
    message=Messages.query.get(id)
    db.session.delete(message)
    db.session.commit()
    return redirect('/admin/messages')
# messages end

# navigation start
@admin_bp.route('/navlinks', methods=['GET','POST'])
def navlinks():
    navlinks=NavLinksForm()
    navigationlink=NavLinks.query.all()
    return render_template('admin/navbar/navlinks.html', navlinks=navlinks, navigationlink=navigationlink)

@admin_bp.route('/navlinks/add', methods=['GET','POST'])
def navlinks_add():
    from run import db
    navlinkForm=NavLinksForm()
    if request.method=='POST':
        navlink=NavLinks(
            Name=navlinkForm.name.data,
            Url=navlinkForm.url.data,
            Order=navlinkForm.order.data,
            IsActive=navlinkForm.isactive.data
        )
        db.session.add(navlink)
        db.session.commit()
        return redirect('/admin/navlinks')

@admin_bp.route('/navlinks/delete/<id>',methods=['GET','POST'])
def navlinks_delete(id):
    from run import db
    link=NavLinks.query.get(id)
    db.session.delete(link)
    db.session.commit()
    return redirect('/admin/navlinks')

@admin_bp.route('/navlinks/edit/<id>', methods=['GET','POST'])
def navlinks_edit(id):
    from run import db
    navlinks=NavLinks.query.get(id)
    navlinksform=NavLinksForm()
    if request.method=='POST':
        navlinks.Name=navlinksform.name.data
        navlinks.Url=navlinksform.url.data
        navlinks.Order=navlinksform.order.data
        navlinks.IsActive=navlinksform.isactive.data
        db.session.commit()
    return render_template('admin/navbar/navlinksedit.html',navlinksform=navlinksform,navlinks=navlinks)
# navigation end

# teams start
@admin_bp.route('/teams', methods=['GET','POST'])
def teams():
    teamsform=TeamsForm()
    teams=Teams.query.all()
    return render_template('admin/teams/teams.html', teamsform=teamsform, teams=teams)

@admin_bp.route('/teams/add', methods=['GET','POST'])
def teams_add():
    from run import db
    teamsform=TeamsForm()
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Teams{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        team=Teams(
            Name=teamsform.name.data,
            Profession=teamsform.profession.data,
            Image=new_filename,
            TwitterAdress=teamsform.twitter.data,
            FacebookAdress=teamsform.facebook.data,
            InstagramAdress=teamsform.instagram.data,
            LinkedinAdress=teamsform.linkedin.data,
            Order=teamsform.order.data,
            IsActive=teamsform.isactive.data
        )
        db.session.add(team)
        db.session.commit()
        return redirect('/admin/teams')

@admin_bp.route('/teams/delete/<id>')
def teams_delete(id):
    from run import db
    team=Teams.query.get(id)
    filename=f"./static/uploads/{team.Image}"
    os.remove(filename)
    db.session.delete(team)
    db.session.commit()
    return redirect('/admin/teams')

@admin_bp.route('/teams/edit/<id>', methods=['GET','POST'])
def teams_edit(id):
    from run import db
    team=Teams.query.get(id)
    teamsform=TeamsForm()
    if request.method=='POST':
        if request.files['image']:
            file_name=f"./static/uploads/{team.Image}"
            os.remove(file_name)
            file=request.files['image']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'Teams{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            team.Image=new_filename
        team.Name=teamsform.name.data
        team.Profession=teamsform.profession.data
        team.TwitterAdress=teamsform.twitter.data
        team.FacebookAdress=teamsform.facebook.data
        team.InstagramAdress=teamsform.instagram.data
        team.LinkedinAdress=teamsform.linkedin.data
        team.Order=teamsform.order.data
        team.IsActive=teamsform.isactive.data
        db.session.commit()
    return render_template('admin/teams/teamsedit.html',team=team, teamsform=teamsform)
# teams end

# teams image start
@admin_bp.route('/teamsimage', methods=['GET','POST'])
def teamsimage():
    from models import Teams
    teams=Teams.query.all()
    teamimagesform=TeamImagesForm()
    teamimages=TeamImages.query.all()
    return render_template('admin/teams/teamsimage.html',teams=teams,teamimagesform=teamimagesform,teamimages=teamimages,Teamsdata=Teams)

@admin_bp.route('/teamsimage/add', methods=['GET','POST'])
def teamsimage_add():
    from run import db
    if request.method=='POST':
        name=Teams.query.filter_by(Id=request.form['Teams']).first().Name
        files=request.files.getlist('image')
        for file in files:
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'TeamImages{random.randint(1,2000)}.{extension}'
            if os.path.isdir(f'./static/uploads/{name}'):
                file.save(os.path.join(f'./static/uploads/{name}/', new_filename))
            else:
                os.makedirs(f'./static/uploads/{name}')
                file.save(os.path.join(f'./static/uploads/{name}/', new_filename))
            teamsimage=TeamImages(
                Teamsid=request.form['Teams'],
                image=new_filename
            )
            db.session.add(teamsimage)
        db.session.commit()
        return redirect('/admin/teamsimage')

@admin_bp.route('/teamsimage/delete/<id>', methods=['GET','POST'])
def teamsimage_delete(id):
    from run import db
    image=TeamImages.query.get(id)
    filename=f"./static/uploads/{image.image}"
    os.remove(filename)
    db.session.delete(image)
    db.session.commit()
    return redirect('/admin/teamsimage')
# teams image end

# portfoliocategory start
@admin_bp.route('/portfoliocategory', methods=['GET','POST'])
def portfoliocategory():
    portfoliocategoryform=PortfolioCategoryForm()
    categories=PortfolioCategory.query.all()
    return render_template('admin/portfolio/PortfolioCategory.html',portfoliocategoryform=portfoliocategoryform,categories=categories)

@admin_bp.route('/portfoliocategory/add', methods=['GET','POST'])
def portfoliocategory_add():
    from run import db
    from models import PortfolioCategory
    if request.method=='POST':
        category=PortfolioCategory(
            name=request.form['name']
        )
        db.session.add(category)
        db.session.commit()
        return redirect('/admin/portfoliocategory')

@admin_bp.route('/portfoliocategory/delete/<id>', methods=['GET','POST'])
def portfoliocategory_delete(id):
    from run import db
    portfoliocategory=PortfolioCategory.query.get(id)
    db.session.delete(portfoliocategory)
    db.session.commit()
    return redirect('/admin/portfoliocategory')

@admin_bp.route('/portfoliocategory/edit/<id>', methods=['GET','POST'])
def portfoliocategory_edit(id):
    from run import db
    category=PortfolioCategory.query.get(id)
    portfoliocategoryform=PortfolioCategoryForm()
    if request.method=='POST':
        category.name=portfoliocategoryform.name.data
        db.session.commit()
        return redirect('/admin/portfoliocategory')
    return render_template('admin/portfolio/portfoliocategoryedit.html',portfoliocategoryform=portfoliocategoryform,category=category)
# portfoliocategory end

# portfolio start
@admin_bp.route('/portfolio', methods=['GET','POST'])
def portfolio():
    from models import PortfolioCategory
    categoies=PortfolioCategory.query.all()
    portfolios=Portfolio.query.all()
    portfolioform=PortfolioForm()
    return render_template('admin/portfolio/portfolio.html',portfolioform=portfolioform,categoies=categoies,portfolios=portfolios,PortfolioCategory=PortfolioCategory)

@admin_bp.route('/portfolio/add', methods=['GET','POST'])
def protfolio_add():
    from run import db
    from models import Portfolio
    portfolioform=PortfolioForm()
    if request.method=='POST':
        file=request.files['img']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Portfolio{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        portfolio=Portfolio(
            name=portfolioform.name.data,
            Category_id=request.form['Category'],
            img=new_filename,
            info=portfolioform.info.data
        )
        db.session.add(portfolio)
        db.session.commit()
        return redirect('/admin/portfolio')

@admin_bp.route('/portfolio/delete/<id>', methods=['GET','POST'])
def portfolio_delete(id):
    from run import db
    portfolio=Portfolio.query.get(id)
    filename=f"./static/uploads/{portfolio.img}"
    os.remove(filename)
    db.session.delete(portfolio)
    db.session.commit()
    return redirect('/admin/portfolio')

@admin_bp.route('/portfolio/edit/<id>', methods=['GET','POST'])
def portfolio_edit(id):
    from run import db
    portfolioform=PortfolioForm()
    categories=PortfolioCategory.query.all()
    portfolio=Portfolio.query.get(id)
    if request.method=='POST':
        if request.files['img']:
            file_name=f"./static/uploads/{portfolio.img}"
            os.remove(file_name)
            file=request.files['img']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'Portfolio{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            portfolio.img=new_filename
        portfolio.name=portfolioform.name.data
        portfolio.Category_id=request.form['Category']
        portfolio.info=portfolioform.info.data
        db.session.commit()
        return redirect('/admin/portfolio')
    return render_template('admin/portfolio/portfolioedit.html',portfolioform=portfolioform,portfolio=portfolio,categories=categories)
# portfolio end

# clients start
@admin_bp.route('/clients', methods=['GET','POST'])
def clients():
    clientform=ClientsForm()
    clients=Clients.query.all()
    return render_template('admin/clients/clients.html', clientform=clientform,clients=clients)

@admin_bp.route('/clients/add', methods=['GET','POST'])
def clients_add():
    from run import db
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Clients{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        client=Clients(
            image=new_filename
        )
        db.session.add(client)
        db.session.commit()
        return redirect('/admin/clients')

@admin_bp.route('/clients/delete/<id>', methods=['GET','POST'])
def clients_delete(id):
    from run import db
    client=Clients.query.get(id)
    filename=f"./static/uploads/{client.image}"
    os.remove(filename)
    db.session.delete(client)
    db.session.commit()
    return redirect('/admin/clients')
# clients end

# featuredservice start
@admin_bp.route('/featuredservice', methods=['GET','POST'])
def featuredservice():
    featuredserviceform=FeaturedserviceForm()
    featuredservices=FeaturedServices.query.all()
    return render_template('admin/featuredservice/featuredservice.html',featuredserviceform=featuredserviceform,featuredservices=featuredservices)

@admin_bp.route('/featuredservice/add', methods=['GET','POST'])
def featuredservice_add():
    featuredserviceform=FeaturedserviceForm()
    from run import db
    if request.method=='POST':
        featuredservice=FeaturedServices(
            icon=featuredserviceform.icon.data,
            name=featuredserviceform.name.data,
            info=featuredserviceform.info.data
        )
        db.session.add(featuredservice)
        db.session.commit()
        return redirect('/admin/featuredservice')

@admin_bp.route('/featuredservice/delete/<id>', methods=['GET','POST'])
def featuredservice_delete(id):
    from run import db
    featuredservice=FeaturedServices.query.get(id)
    db.session.delete(featuredservice)
    db.session.commit()
    return redirect('/admin/featuredservice')

@admin_bp.route('/featuredservice/edit/<id>', methods=['GET','POST'])
def featuredservice_edit(id):
    from run import db
    service=FeaturedServices.query.get(id)
    featuredserviceform=FeaturedserviceForm()
    if request.method=='POST':
        service.icon=featuredserviceform.icon.data
        service.name=featuredserviceform.name.data
        service.info=featuredserviceform.info.data
        db.session.commit()
        return redirect('admin/featuredservice')
    return render_template('admin/feturedservice/featuredserviceedit.html',featuredserviceform=featuredserviceform,service=service)
# featuredservice end

# service start
@admin_bp.route('/service', methods=['GET','POST'])
def service():
    servicesform=ServiceForm()
    services=Services.query.all()
    return render_template('admin/service/service.html',servicesform=servicesform,services=services)

@admin_bp.route('/service/add', methods=['GET','POST'])
def service_add():
    from run import db
    serviceform=ServiceForm()
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Service{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        service=Services(
            name=serviceform.name.data,
            info=serviceform.info.data,
            icon=serviceform.icon.data,
            image=new_filename
        )
        db.session.add(service)
        db.session.commit()
        return redirect('/admin/service')

@admin_bp.route('/service/delete/<id>', methods=['GET','POST'])
def service_delete(id):
    from run import db
    service=Services.query.get(id)
    filename=f"./static/uploads/{service.image}"
    os.remove(filename)
    db.session.delete(service)
    db.session.commit()
    return redirect('/admin/service')

@admin_bp.route('/service/edit/<id>', methods=['GET','POST'])
def service_edit(id):
    from run import db
    servicesform=ServiceForm()
    service=Services.query.get(id)
    if request.method=='POST':
        if request.files['image']:
            file_name=f"./static/uploads/{service.image}"
            os.remove(file_name)
            file=request.files['image']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'Service{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            service.image=new_filename
        service.name=servicesform.name.data
        service.info=servicesform.info.data
        service.icon=servicesform.icon.data
        db.session.commit()
        return redirect('/admin/service')
    return render_template('admin/service/serviceedit.html',servicesform=servicesform,service=service)
# service end

# pricing start
@admin_bp.route('/pricing', methods=['GET','POST'])
def pricing():
    pricingform=PricingForm()
    pricings=Pricing.query.all()
    return render_template('admin/pricing/pricing.html',pricingform=pricingform,pricings=pricings)

@admin_bp.route('/pricing/add', methods=['GET','POST'])
def pricing_add():
    from run import db
    pricingform=PricingForm()
    if request.method=='POST':
        price=Pricing(
            name=pricingform.name.data,
            amount=pricingform.amount.data
        )
        db.session.add(price)
        db.session.commit()
        return redirect('/admin/pricing')

@admin_bp.route('/pricing/delete/<id>', methods=['GET','POST'])
def pricing_delete(id):
    from run import db
    pricing=Pricing.query.get(id)
    db.session.delete(pricing)
    db.session.commit()
    return redirect('/admin/pricing')

@admin_bp.route('/pricing/edit/<id>', methods=['GET','POST'])
def pricing_edit(id):
    from run import db
    pricingform=PricingForm()
    pricing=Pricing.query.get(id)
    if request.method=='POST':
        pricing.name=pricingform.name.data
        pricing.amount=pricingform.amount.data
        db.session.commit()
        return redirect('/admin/pricing')
    return render_template('admin/pricing/pricingedit.html',pricingform=pricingform,pricing=pricing)
# pricing end

# pricing option start
@admin_bp.route('/pricingoption', methods=['GET','POST'])
def pricingoption():
    from models import Pricing
    pricings=Pricing.query.all()
    pricingoptionform=PricingOptionsForm()
    pricingoptions=PricingOptions.query.all()
    return render_template('admin/pricing/pricingoptions.html',pricings=pricings,pricingoptionform=pricingoptionform,pricingoptions=pricingoptions,Pricing=Pricing)

@admin_bp.route('/pricingoption/add', methods=['GET','POST'])
def pricingoption_add():
    from run import db
    pricingoptionform=PricingOptionsForm()
    if request.method=='POST':
        pricingoption=PricingOptions(
            pricing_id=request.form['pricing'],
            option=pricingoptionform.option.data
        )
        db.session.add(pricingoption)
        db.session.commit()
        return redirect('/admin/pricingoption')

@admin_bp.route('/pricingoption/delete/<id>', methods=['GET','POST'])
def pricingoption_delete(id):
    from run import db
    pricingoption=PricingOptions.query.get(id)
    db.session.delete(pricingoption)
    db.session.commit()
    return redirect('/admin/pricingoption')

@admin_bp.route('/pricingoption/edit/<id>', methods=['GET','POST'])
def procongoptions_edit(id):
    from run import db
    pricingoptionform=PricingOptionsForm()
    pricingoption=PricingOptions.query.get(id)
    pricings=Pricing.query.all()
    if request.method=='POST':
        pricingoption.pricing_id=request.form['pricing']
        pricingoption.option=pricingoptionform.option.data
        db.session.commit()
        return redirect('/admin/pricingoption')
    return render_template('admin/pricing/pricingoptionsedit.html',pricingoptionform=pricingoptionform,pricingoption=pricingoption,pricings=pricings)
# pricing option end

# ourInformation start
@admin_bp.route('/information', methods=['GET','POST'])
def information():
    informationform=OurInformationsForm()
    informations=OurInformations.query.all()
    return render_template('admin/information/information.html',informationform=informationform,informations=informations)

@admin_bp.route('/information/add', methods=['GET','POST'])
def information_add():
    from run import db
    informationform=OurInformationsForm()
    if request.method=='POST':
        information=OurInformations(
            location=informationform.location.data,
            email=informationform.email.data,
            phone=informationform.phone.data
        )
        db.session.add(information)
        db.session.commit()
        return redirect('/admin/information')

@admin_bp.route('/information/delete/<id>', methods=['GET','POST'])
def information_delete(id):
    from run import db
    information=OurInformations.query.get(id)
    db.session.delete(information)
    db.session.commit()
    return redirect('/admin/information')

@admin_bp.route('/information/edit/<id>', methods=['GET','POST'])
def information_edit(id):
    from run import db
    informationform=OurInformationsForm()
    information=OurInformations.query.get(id)
    if request.method=='POST':
        information.location=informationform.location.data
        information.email=informationform.email.data
        information.phone=informationform.phone.data
        db.session.commit()
        return redirect('/admin/information')
    return render_template('admin/information/informationedit.html',informationform=informationform,information=information)
# ourInformation end

# testimonials start
@admin_bp.route('/testimonials', methods=['GET','POST'])
def testimonials():
    testimonialsform=TestimonialsForm()
    testimonials=Testimanials.query.all()
    return render_template('admin/testimonials/testimonials.html',testimonialsform=testimonialsform,testimonials=testimonials)

@admin_bp.route('/testimonials/add', methods=['GET','POST'])
def testimonials_add():
    from run import db
    testimonialsform=TestimonialsForm()
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Testimonials{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        testimonial=Testimanials(
            name=testimonialsform.name.data,
            profession=testimonialsform.profession.data,
            image=new_filename,
            info=testimonialsform.info.data
        )
        db.session.add(testimonial)
        db.session.commit()
        return redirect('/admin/testimonials')

@admin_bp.route('/testimonials/delete/<id>', methods=['GET','POST'])
def testimonials_delete(id):
    from run import db
    testimonial=Testimanials.query.get(id)
    filename=f"./static/uploads/{testimonial.image}"
    os.remove(filename)
    db.session.delete(testimonial)
    db.session.commit()
    return redirect('/admin/testimonials')

@admin_bp.route('/testimonials/edit/<id>', methods=['GET','POST'])
def testimonials_edit(id):
    from run import db
    testimonial=Testimanials.query.get(id)
    testimonialsform=TestimonialsForm()
    if request.method=='POST':
        if request.files['image']:
            file_name=f"./static/uploads/{testimonial.image}"
            os.remove(file_name)
            file=request.files['image']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'Testimonials{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            testimonial.image=new_filename
        testimonial.name=testimonialsform.name.data
        testimonial.profession=testimonialsform.profession.data
        testimonial.info=testimonialsform.info.data
        db.session.commit()
        return redirect('/admin/testimonials')
    return render_template('admin/testimonials/testimonialsedit.html',testimonialsform=testimonialsform,testimonial=testimonial)
# testimonials end

# features start
@admin_bp.route('/features', methods=['GET','POST'])
def features():
    featuresform=FeaturesForm()
    features=Features.query.all()
    return render_template('admin/features/features.html',featuresform=featuresform,features=features)

@admin_bp.route('/features/add', methods=['GET','POST'])
def features_add():
    from run import db
    featuresform=FeaturesForm()
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Features{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        feature=Features(
            name=featuresform.name.data,
            icon=featuresform.icon.data,
            info=featuresform.info.data,
            image=new_filename,
            order=featuresform.order.data
        )
        db.session.add(feature)
        db.session.commit()
        return redirect('/admin/features')
    return render_template('admin/features/add',featuresform=featuresform)

@admin_bp.route('/features/delete/<id>', methods=['GET','POST'])
def features_delete(id):
    from run import db
    feature=Features.query.get(id)
    file_name=f"./static/uploads/{feature.image}"
    os.remove(file_name)
    db.session.delete(feature)
    db.session.commit()
    return redirect('/admin/features')

@admin_bp.route('/features/edit/<id>', methods=['GET','POST'])
def features_edit(id):
    featuresform=FeaturesForm()
    feature=Features.query.get(id)
    if request.method=='POST':
        if request.files['image']:
            file_name=f"./static/uploads/{feature.image}"
            os.remove(file_name)
            file=request.files['image']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'Features{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            feature.image=new_filename
        feature.name=featuresform.name.data
        feature.icon=featuresform.icon.data
        feature.info=featuresform.info.data
        feature.order=featuresform.order.data
        db.session.commit()
        return redirect('/admin/features')
    return render_template('admin/features/featuresedit.html',featuresform=featuresform,feature=feature)
# features end

# features option start
@admin_bp.route('/featureoptions', methods=['GET','POST'])
def featureoptions():
    from models import Features
    featureoptionsform=FeatureOptionsForm()
    featureoptions=FeatureOptions.query.all()
    features=Features.query.all()
    return render_template('admin/features/featureoptions.html',featureoptionsform=featureoptionsform,featureoptions=featureoptions,features=features,data=Features)

@admin_bp.route('/featureoptions/add', methods=['GET','POST'])
def featureoptions_add():
    from run import db
    featureoptionsform=FeatureOptionsForm()
    if request.method=='POST':
        featureoption=FeatureOptions(
            features_id=request.form['Featureoptions'],
            option=featureoptionsform.option.data
        )
        db.session.add(featureoption)
        db.session.commit()
        return redirect('/admin/featureoptions')

@admin_bp.route('/featureoptions/delete/<id>', methods=['GET','POST'])
def featureoptions_delete(id):
    from run import db
    featureoption=FeatureOptions.query.get(id)
    db.session.delete(featureoption)
    db.session.commit()
    return redirect('/admin/featureoptions')

@admin_bp.route('/featureoptions/edit/<id>', methods=['GET','POST'])
def featureoptions_edit(id):
    from run import db
    featureoptionsform=FeatureOptionsForm()
    feature=Features.query.get(id)
    features=Features.query.all()
    if request.method=='POST':
        feature.features_id=request.form['Featureoptions']
        feature.option=featureoptionsform.option.data
        db.session.commit()
        return redirect('/admin/featureoptions')
    return render_template('admin/features/featureoptionsedit.html',featureoptionsform=featureoptionsform,feature=feature,features=features)
# features option end

# blogs start
@admin_bp.route('/blog', methods=['GET','POST'])
def blog():
    blogform=BlogForm()
    blogs=Blogs.query.all()
    return render_template('admin/blog/blog.html',blogform=blogform,blogs=blogs)

@admin_bp.route('/blog/add', methods=['GET','POST'])
def blog_add():
    blogform=BlogForm()
    from run import db
    if request.method=='POST':
        file=request.files['image']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[1]
        new_filename=f'Blog{random.randint(1,2000)}.{extension}'
        file.save(os.path.join('./static/uploads/', new_filename))
        blog=Blogs(
            name=blogform.name.data,
            header=blogform.header.data,
            image=new_filename,
            content=blogform.content.data
        )
        db.session.add(blog)
        db.session.commit()
        return redirect('/admin/blog')

@admin_bp.route('/blog/delete/<id>',methods=['GET','POST'])
def blog_delete(id):
    from run import db
    blog=Blogs.query.get(id)
    file_name=f"./static/uploads/{blog.image}"
    os.remove(file_name)
    db.session.delete(blog)
    db.session.commit()
    return redirect('/admin/blog')

@admin_bp.route('/blog/edit/<id>', methods=['GET','POST'])
def blog_edit(id):
    from run import db
    blogform=BlogForm()
    blog=Blogs.query.get(id)
    if request.method=='POST':
        if request.files['image']:
            file_name=f"./static/uploads/{blog.image}"
            os.remove(file_name)
            file=request.files['image']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'Blog{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            blog.image=new_filename
        blog.name=blogform.name.data
        blog.header=blogform.header.data
        blog.content=blogform.content.data
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('admin/blog/blogedit.html',blogform=blogform,blog=blog)
# blogs end
from flask import render_template,redirect,request
from admin import admin_bp
from models import Messages, NavLinks, TeamImages, Teams, Portfolio, PortfolioCategory
from admin.forms import MessageForm, NavLinksForm, TeamsForm, PortfolioCategoryForm, PortfolioForm,TeamImagesForm
import os
import random
from werkzeug.utils import secure_filename

@admin_bp.route('/', methods=['GET','POST'])
def index():
    return render_template('admin/index.html')

@admin_bp.route('/messages')
def messages():
    messages=Messages.query.all()
    return render_template('admin/messages.html', messages=messages)

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

@admin_bp.route('/navlinks', methods=['GET','POST'])
def navlinks():
    navlinks=NavLinksForm()
    navigationlink=NavLinks.query.all()
    return render_template('admin/navlinks.html', navlinks=navlinks, navigationlink=navigationlink)

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
    return render_template('admin/navlinkedit.html')

@admin_bp.route('/teams', methods=['GET','POST'])
def teams():
    teamsform=TeamsForm()
    teams=Teams.query.all()
    return render_template('admin/teams.html', teamsform=teamsform, teams=teams)

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

@admin_bp.route('/teamsimage', methods=['GET','POST'])
def teamsimage():
    from models import Teams
    teams=Teams.query.all()
    teamimagesform=TeamImagesForm()
    teamimages=TeamImages.query.all()
    return render_template('admin/teamsimage.html',teams=teams,teamimagesform=teamimagesform,teamimages=teamimages,Teamsdata=Teams)

@admin_bp.route('/teamsimage/add', methods=['GET','POST'])
def teamsimage_add():
    from run import db
    if request.method=='POST':
        files=request.files.getlist('image')
        for file in files:
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[1]
            new_filename=f'TeamImages{random.randint(1,2000)}.{extension}'
            file.save(os.path.join('./static/uploads/', new_filename))
            teamsimage=TeamImages(
                Teamsid=request.form['Teams'],
                image=new_filename
            )
            db.session.add(teamsimage)
        db.session.commit()
        return redirect('/admin/teamsimage')

@admin_bp.route('/portfoliocategory', methods=['GET','POST'])
def portfoliocategory():
    portfoliocategoryform=PortfolioCategoryForm()
    categories=PortfolioCategory.query.all()
    return render_template('admin/PortfolioCategory.html',portfoliocategoryform=portfoliocategoryform,categories=categories)

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

@admin_bp.route('/portfolio', methods=['GET','POST'])
def portfolio():
    from models import PortfolioCategory
    categoies=PortfolioCategory.query.all()
    portfolios=Portfolio.query.all()
    portfolioform=PortfolioForm()
    return render_template('admin/portfolio.html',portfolioform=portfolioform,categoies=categoies,portfolios=portfolios,PortfolioCategory=PortfolioCategory)

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
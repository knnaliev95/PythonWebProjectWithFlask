from distutils import extension
from email.mime import image
from flask import render_template,redirect,request
from admin import admin_bp
from models import Messages, NavLinks, Teams
from admin.forms import MessageForm, NavLinksForm, TeamsForm
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

@admin_bp.route('navlinks/delete/<id>',methods=['GET','POST'])
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
        file.save(os.path.join('./admin/static/uploads/', new_filename))
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
    db.session.delete(team)
    db.session.commit()
    return redirect('/admin/teams')
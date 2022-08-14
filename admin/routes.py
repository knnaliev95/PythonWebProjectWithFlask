from flask import render_template,redirect,request
from admin import admin_bp
from models import Messages, NavLinks
from admin.forms import MessageForm, NavLinksForm

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
    from run import db
    navlinksform=NavLinksForm()
    navlink=NavLinks.query.get(id)
    if request.method=='POST':
        navlink.Name=navlinksform.name.data
        navlink.Url=navlinksform.url.data
        navlink.Order=navlinksform.order.data
        navlink.IsActive=navlinksform.isactive.data
        db.session.commit()
        return redirect('/admin/navlinks')
    return render_template('admin/navlinks_edit.html', navlink=navlink, navlinksform=navlinksform)
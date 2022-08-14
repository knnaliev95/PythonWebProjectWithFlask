from dataclasses import dataclass
from flask import render_template,redirect,request
from admin import admin_bp
from models import Messages
from admin.forms import MessageForm

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
from flask import Flask,render_template
from peoples import peoples_bp
from admin.forms import MessageForm

@peoples_bp.route('/', methods=['GET','POST'])
def peoples_index():
    messageForm=MessageForm()
    from run import db
    from models import Messages
    return render_template('peoples/index.html', messageForm=messageForm)
from flask import render_template,redirect,request
from admin import admin_bp

@admin_bp.route('/', methods=['GET','POST'])
def index():
    return render_template('admin/index.html')

@admin_bp.route('/messages')
def messages():
    return render_template('admin/messages.html')
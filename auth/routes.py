from flask import render_template,redirect,request
from auth import auth_bp
from auth.forms import *
from flask_login import login_user, logout_user, login_required, current_user

@auth_bp.route('/', methods=['GET','POST'])
def auth():
    return render_template('auth/index.html')

@auth_bp.route('/register', methods=['GET','POST'])
def auth_register():
    registerform=RegisterForm()
    from run import db
    from models import Users
    if request.method=='POST':
        user=Users(
            name=registerform.name.data,
            email=registerform.email.data,
            password=registerform.password.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/auth/login')
    return render_template('auth/register.html',registerform=registerform)

@auth_bp.route('/login', methods=['GET','POST'])
def auth_login():
    loginform=LoginForm()
    from models import Users
    if request.method=='POST':
        user=Users.query.filter_by(email=loginform.email.data).first()
        if user:
            if user.password==loginform.password.data:
                login_user(user)
                return redirect('/admin')
        else:
            return redirect('/auth/login')
    return render_template('auth/login.html', loginform=loginform)

@auth_bp.route('/logout', methods=['GET','POST'])
def auth_logout():
    logout_user()
    return redirect('/auth/login')
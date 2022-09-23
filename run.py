from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db=SQLAlchemy(app)
app.config['SECRET_KEY']='secretkey'
migrate=Migrate(app,db)
login_manager=LoginManager(app)


from admin.routes import *
from peoples.routes import *
from auth.routes import *

from admin import admin_bp
from peoples import peoples_bp
from auth import auth_bp

app.register_blueprint(admin_bp)
app.register_blueprint(peoples_bp)
app.register_blueprint(auth_bp)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.auth_login'))

if __name__=='__main__':
    app.run(port=8000,debug=True)
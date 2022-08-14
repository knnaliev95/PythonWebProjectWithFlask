from flask import Flask,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db=SQLAlchemy(app)
app.config['SECRET_KEY']='secretkey'
from admin.routes import *
from peoples.routes import *

from admin import admin_bp
from peoples import peoples_bp

app.register_blueprint(admin_bp)
app.register_blueprint(peoples_bp)

if __name__=='__main__':
    app.run(port=8000,debug=True)
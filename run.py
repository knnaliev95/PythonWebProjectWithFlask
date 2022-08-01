from flask import Flask, redirect,render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_migrate import Migrate
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db=SQLAlchemy(app)
migrate = Migrate(app, db)
class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    Subject = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    m_date = db.Column(db.String(50), nullable=False)
class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(25), nullable=False)
    email=db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(50), nullable=False)
    login_status=db.Column(db.Boolean)
@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='POST':
        name = request.form["m_name"]
        email=request.form["m_email"]
        subject=request.form["m_subject"]
        message=request.form["m_message"]
        msj=Messages(name=name,email=email,Subject=subject,message=message,m_date=str(datetime.datetime.now()))
        db.session.add(msj)
        db.session.commit()
        return redirect("/messages")
    return render_template("index.html")

@app.route("/messages", methods=['GET','POST'])
def messages():
    user=Users.query.all()
    for i in user:
        if i.login_status==True:
            userid=i.id
            msj=Messages.query.all()
        else:
            return redirect('/login')
    return render_template("messages.html",messages=msj,id=userid)

@app.route("/delete/<id>", methods=['GET','POST'])
def delete(id):
    msj=Messages.query.get(id)
    db.session.delete(msj)
    db.session.commit()
    return redirect("/messages")

@app.route("/update/<id>", methods=['GET','POST'])
def update(id):
    msj=Messages.query.get(id)
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        msj.name=name
        msj.email=email
        msj.message=message
        db.session.commit()
    return render_template("update.html", mesage=msj)

@app.route("/registration", methods=['GET','POST'])
def registration():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        user=Users(name=name,email=email,password=password,login_status=False)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template("registration.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method=="POST":
        email=request.form['email']
        password=request.form['password']
        user=Users.query.all()
        for i in user:
            if email==i.email and password==i.password:
                i.login_status=True
                db.session.commit()
                return redirect('/messages')
            else:
                return redirect('/login')
    return render_template("login.html")

@app.route("/logout/<id>", methods=['GET','POST'])
def logout(id):
    user=Users.query.get(id)
    user.login_status=False
    db.session.commit()
    return redirect('/login')

if __name__=="__main__":
    app.run(port=5000,debug=True)
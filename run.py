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
    msj=Messages.query.all()
    return render_template("messages.html",messages=msj)

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
        msj.emal=email
        msj.message=message
        db.session.commit()

    return render_template("update.html", mesage=msj)



if __name__=="__main__":
    app.run(port=5000,debug=True)
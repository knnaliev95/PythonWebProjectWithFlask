from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db=SQLAlchemy(app)
class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    Subject = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(200), nullable=False)
@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='POST':
        name = request.form["m_name"]
        email=request.form["m_email"]
        subject=request.form["m_subject"]
        message=request.form["m_message"]
        msj=Messages(name=name,email=email,Subject=subject,message=message)
        db.session.add(msj)
        db.session.commit()
    return render_template("index.html")

if __name__=="__main__":
    app.run(port=5000,debug=True)
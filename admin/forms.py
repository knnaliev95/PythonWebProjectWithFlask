from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TextAreaField,SubmitField,URLField,IntegerField,BooleanField,FileField

class MessageForm(FlaskForm):
    name=StringField('name')
    email=EmailField('email')
    subject=StringField('subject')
    message=TextAreaField('message')
    submit=SubmitField('Send Message')

class NavLinksForm(FlaskForm):
    name=StringField('name')
    url=StringField('url')
    order=IntegerField('order')
    isactive=BooleanField('isactive')
    submit=SubmitField('Add URL')

class TeamsForm(FlaskForm):
    name=StringField('name')
    profession=StringField('profession')
    image=FileField('image')
    twitter=StringField('twitter')
    facebook=StringField('facebook')
    instagram=StringField('instagram')
    linkedin=StringField('linkedin')
    order=IntegerField('order')
    isactive=BooleanField('isacctive')
    submit=SubmitField('Add data')
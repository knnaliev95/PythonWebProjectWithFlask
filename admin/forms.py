from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TextAreaField,SubmitField,URLField,IntegerField,BooleanField

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
from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TextAreaField,SubmitField

class MessageForm(FlaskForm):
    name=StringField('name')
    email=EmailField('email')
    subject=StringField('subject')
    message=TextAreaField('message')
    submit=SubmitField('Send Message')
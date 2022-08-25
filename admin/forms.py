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

class TeamImagesForm(FlaskForm):
    Teamsid=IntegerField('teamsid')
    image=FileField('image')
    submit=SubmitField('Add image')

class PortfolioCategoryForm(FlaskForm):
    name=StringField('name')
    submit=SubmitField('Add data')

class PortfolioForm(FlaskForm):
    name=StringField('name')
    category_id=IntegerField('category_id')
    img=FileField('img')
    info=StringField('info')
    submit=SubmitField('Add Portfolio')
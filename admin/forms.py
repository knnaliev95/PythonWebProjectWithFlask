from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TextAreaField,SubmitField,URLField,IntegerField,BooleanField,FileField,SelectField
from flask_ckeditor import CKEditorField

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

class ClientsForm(FlaskForm):
    image=FileField('image')
    submit=SubmitField('Add Client')

class FeaturedserviceForm(FlaskForm):
    name=StringField('name')
    icon=StringField('icon')
    info=TextAreaField('info')
    submit=SubmitField('Add Feature')

class ServiceForm(FlaskForm):
    name=StringField('name')
    icon=StringField('icon')
    image=FileField('image')
    info=TextAreaField('info')
    submit=SubmitField('Add Service')

class PricingForm(FlaskForm):
    name=StringField('name')
    amount=IntegerField('amount')
    submit=SubmitField('Add Price')

class PricingOptionsForm(FlaskForm):
    option=StringField('option')
    submit=SubmitField('Add Option')

class OurInformationsForm(FlaskForm):
    location=StringField('location')
    email=EmailField('email')
    phone=StringField('phone')
    submit=SubmitField('Add Information')

class TestimonialsForm(FlaskForm):
    name=StringField('name')
    profession=StringField('profession')
    image=FileField('image')
    info=TextAreaField('info')
    submit=SubmitField('Add Testimonials')

class FeaturesForm(FlaskForm):
    name=StringField('name')
    icon=StringField('icon')
    image=FileField('image')
    info=TextAreaField('info')
    order=IntegerField('order')
    submit=SubmitField('Add Features')

class FeatureOptionsForm(FlaskForm):
    features_id=IntegerField('features_id')
    option=StringField('option')
    submit=SubmitField('Add option')

class BlogForm(FlaskForm):
    name=StringField('name')
    header=StringField('header')
    image=FileField('image')
    content=CKEditorField('content')
    submit=SubmitField('Add Blog')

class TestForm(FlaskForm):
    department=SelectField('department')
    section=SelectField('section')
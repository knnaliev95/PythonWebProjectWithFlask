from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TextAreaField,SubmitField,URLField,IntegerField,BooleanField,FileField,PasswordField,validators


class LoginForm(FlaskForm):
    email=EmailField('email')
    password=PasswordField('password')
    submit=SubmitField('Login')

class RegisterForm(FlaskForm):
    name=StringField('name')
    email=EmailField('email')
    password=PasswordField('password',validators=[validators.length(min=5,max=10),validators.Regexp("^(?=.*[a-z])"),
            validators.Regexp("^(?=.*[A-Z])"),])
    submit=SubmitField('Register')
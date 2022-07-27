from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp


class RegistrationForm(FlaskForm):
    name = StringField('Name')
    phone = StringField('Phone')
    email =  StringField('email')
    department = StringField('department')
    identification = StringField('identification')
    

    submit = SubmitField('Sign Up')


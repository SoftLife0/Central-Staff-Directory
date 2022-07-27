from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp


class RegistrationForm(FlaskForm):
    name = StringField('Name')
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=10, message="Number must be 10 digits")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=16, message="Password must be less than 16 characters")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    
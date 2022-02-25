import wtforms, wtforms.validators
from flask_wtf import FlaskForm
from .models import User




class RegistrationForm(FlaskForm):
    username = wtforms.StringField('Username', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100)
    ])
    email = wtforms.StringField('Email', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100),
        wtforms.validators.Email()
    ])
    password = wtforms.PasswordField('Password', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100)
    ])
    confirm_password = wtforms.PasswordField('Confirm Password', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100),
        wtforms.validators.EqualTo('password')
    ])

    submit = wtforms.SubmitField('Sign Up')


    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise wtforms.validators.ValidationError(message='Username Already Exists')
    

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise wtforms.validators.ValidationError(message='Email Already Exists')



class LoginForm(FlaskForm):
    email = wtforms.StringField('Email', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100),
        wtforms.validators.Email()
    ])
    password = wtforms.PasswordField('Password', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100)
    ])

    remember_me = wtforms.BooleanField('Remember Me')

    submit = wtforms.SubmitField('Login')


class RequestResetForm(FlaskForm):
    email = wtforms.StringField('Email', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100),
        wtforms.validators.Email()
    ])

    submit = wtforms.SubmitField('Request Reset Password')


    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first() is None:
            raise wtforms.validators.ValidationError(message='Email Not Found')


class ResetPasswordForm(FlaskForm):
    password = wtforms.PasswordField('Password', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100)
    ])
    confirm_password = wtforms.PasswordField('Confirm Password', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100),
        wtforms.validators.EqualTo('password')
    ])

    submit = wtforms.SubmitField('Reset Password')

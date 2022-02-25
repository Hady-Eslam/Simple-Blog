import wtforms, wtforms.validators
from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from App.Blueprints.Authentication.models import User



class UpdateAccountForm(FlaskForm):
    username = wtforms.StringField('Username', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100)
    ])
    email = wtforms.StringField('Email', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100),
        wtforms.validators.Email()
    ])
    image_file = FileField('Profile Avatar', validators=[FileAllowed(['jpg', 'png'])])

    submit = wtforms.SubmitField('Update')

    def validate_username(self, username):
        if current_user.username != username.data:
            if User.query.filter_by(username=username.data).first():
                raise wtforms.validators.ValidationError(message='Username Already Exists')
    

    def validate_email(self, email):
        if current_user.email != email.data:
            if User.query.filter_by(email=email.data).first():
                raise wtforms.validators.ValidationError(message='Email Already Exists')

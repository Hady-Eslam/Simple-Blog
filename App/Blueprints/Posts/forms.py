from flask_wtf import FlaskForm
import wtforms, wtforms.validators


class CreatePostForm(FlaskForm):
    title = wtforms.StringField('Title', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100),
    ])
    content = wtforms.TextAreaField('Content', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100)
    ])

    submit = wtforms.SubmitField('Create')


class UpdatePostForm(FlaskForm):
    title = wtforms.StringField('Title', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100),
    ])
    content = wtforms.TextAreaField('Content', validators=[
        wtforms.validators.DataRequired(), wtforms.validators.Length(min=1, max=100)
    ])

    submit = wtforms.SubmitField('Update')

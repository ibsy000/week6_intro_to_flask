from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo


class SignUpForm(FlaskForm): # Create class that inherits from FlaskForm class
    email = StringField('Email', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
#   class attribute   field       label     validate form not submitted with empty data, and equalto label 'password'
    submit = SubmitField()


class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    body = StringField('Body', validators=[InputRequired()])
    submit = SubmitField()


class LoginForm(FlaskForm): # Create class that inherits from FlaskForm class
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField()
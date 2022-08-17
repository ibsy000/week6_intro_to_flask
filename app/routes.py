from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm
from app.models import User

@app.route('/')
def index():   # also an endpoint
    user_info = {
        'username': 'brians',
        'email': 'brians@codingtemple.com'
    }
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('index.html', user=user_info, colors=colors)

@app.route('/signup', methods=['GET', 'POST'])
def signup():   # also an endpoint
    form = SignUpForm() # instantiate SignUpForm class
    # if the form is submitted and all the data is valid
    if form.validate_on_submit():
        print('Form has been validated! Hooray!!!')
        # each form field has a data attribute
        email = form.email.data
        username = form.username.data
        password = form.password.data
        new_user = User(email=email, username=username, password=password)
        flash(f"{new_user.username} has been created.", "success")
        # the flash can have two parameters (message, category) in this case
        # our category is a color being added to our alert when submitting form
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)
from app import app
from flask import render_template
from app.forms import SignUpForm

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
        print(form.email.data, form.username.data, form.password.data) 
        # each form field has a data attribute
    return render_template('signup.html', form=form)
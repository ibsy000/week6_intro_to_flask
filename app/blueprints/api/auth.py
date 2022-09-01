from datetime import datetime
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models import User


basic_auth = HTTPBasicAuth() # creating an instance of this BasicAuth class
token_auth = HTTPTokenAuth()

@basic_auth.verify_password # verify_password - receives the username and password sent by the client
def verify(username, password):
    user = User.query.filter_by(username=username).first()
    if user is not None and user.check_password(password):
        return user
    # If the credentials are invalid the function can return None or False
    # so you don't have to add an else or return statement

# as with the verify_password, the function should return the user object if
# the token is valid
@token_auth.verify_token
def verify(token):
    user = User.query.filter_by(token=token).first() # either give us a token or none
    now = datetime.utcnow()
    if user is not None and user.token_expiration > now: # if user has a token and it is not expired
        return user
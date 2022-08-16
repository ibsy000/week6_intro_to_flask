from flask import Flask # Flask is a class

app = Flask(__name__) # create first instance of class Flask, parameter will always
# be __name__
app.config['SECRET_KEY'] = 'you-will-never-guess'
#   config subclass of a dictionary


from . import routes
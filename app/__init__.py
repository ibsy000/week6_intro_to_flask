from flask import Flask # Flask is a class

app = Flask(__name__) # create first instance of class Flask, parameter will always
# be __name__


from . import routes
from flask import Flask 
import os 
from flask_login import LoginManager

thisdir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
login = LoginManager(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(thisdir,'database.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['SECRET_KEY'] = os.urandom(10)
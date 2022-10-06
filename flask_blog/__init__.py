from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(base_dir,'blog.db')
app.config['SECRET_KEY'] = '870ff445738e9be3bedd2602c88a795d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

db = SQLAlchemy(app)

from flask_blog import routes
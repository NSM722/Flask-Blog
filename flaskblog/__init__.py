import os
import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '73eb0c0c212b4a564452579b8d0a0fc0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
my_database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'   # pop3 - Post Office Protocol
app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com' # stmp - Simple Mail Transfer Protocol
app.config['MAIL_PORT'] = 587 
#app.config['MAIL_PORT'] = 465
#app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
#app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
#app.config['MAIL_USERNAME'] = 'anikas35@yahoo.uk'
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
mail = Mail(app)

from flaskblog import routes

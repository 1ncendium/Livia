import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


login_manager = LoginManager()

app = Flask(__name__)
upload_folder = 'main/static/assets/img/'
data_folder = 'main/static/assets/data/'

app.config['SECRET_KEY'] = 'mijngeheimesleutel'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = upload_folder
app.config['DATA_FOLDER'] = data_folder

db = SQLAlchemy(app)
Migrate(app, db)

login_manager.init_app(app)

login_manager.login_view = "login"

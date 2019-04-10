import os
from flask import Flask
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy
from config import Base
from sqlalchemy import func


app = Flask(__name__, static_folder='static/common', template_folder='templates')
app.config.from_object('config.Development')

babel = Babel(app)

db = SQLAlchemy(session_options={'autoflush': False})
db.app = app
db.init_app(app)

from app.models.data import *
from app.views import *

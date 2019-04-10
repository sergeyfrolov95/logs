from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models.data import *

from datetime import datetime
from flask import request, url_for
from jinja2 import Markup
from sqlalchemy import func
from flask_admin import expose

class EnrollmentView(ModelView):

    can_create = False
    can_delete = False
    can_edit = False
    can_view_details = True
    can_export = True

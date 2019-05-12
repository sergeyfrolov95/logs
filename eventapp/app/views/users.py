# -*- coding: utf-8 -*-
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models.data import *

from datetime import datetime
from flask import request, url_for
from jinja2 import Markup
from sqlalchemy import func
from flask_admin import expose

class UsersView(ModelView):

        can_create = False
        can_delete = False
        can_edit = False
        can_view_details = True
        can_export = True

        column_list = ('id', 'username')

        column_labels = dict(
            id=u'Идентификатор пользователя',
            username=u'Имя пользователя'
        )

        column_default_sort = 'id'
        column_display_pk = True
        column_searchable_list = ('username',)

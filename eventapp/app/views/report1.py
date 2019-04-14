from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models.data import *

from datetime import datetime
from flask import request, url_for
from jinja2 import Markup
from sqlalchemy import func
from flask_admin import expose

class Report1View(ModelView):

    can_create = False
    can_delete = False
    can_edit = True
    can_view_details = True
    can_export = True

    column_list = ('user_id', 'course', 'per_start', 'per_end')

    column_labels = dict(
        user_id='Имя пользователя',
        course='Идентификатор курса',
        per_start='Начало промежутка',
        per_end='Конец промежутка'
    )

    column_formatters = dict(
        user_id=lambda v, c, m, p: db.session.query(Users.username).filter(Users.id == m.user_id).one_or_none()[0] if m.user_id else '',
        per_start=lambda v, c, m, p: datetime.strftime(m.per_start, '%d.%m.%Y') if m.per_start else '',
        per_end=lambda v, c, m, p: datetime.strftime(m.per_end, '%d.%m.%Y') if m.per_end else ''
    )

    column_display_pk = False

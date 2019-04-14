from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models.data import *

from datetime import datetime
from flask import request, url_for
from jinja2 import Markup
from sqlalchemy import func
from flask_admin import expose

class CertificateView(ModelView):

    can_create = False
    can_delete = False
    can_edit = False
    can_view_details = True
    can_export = True

    column_list = ('user_id', 'course', 'event_time', 'course_id')

    column_labels = dict(
        user_id='Имя пользователя',
        course='Идентификатор курса',
        event_time='Время события',
        course_id='Курс'
    )

    column_formatters = dict(
        user_id=lambda v, c, m, p: db.session.query(Users.username).filter(Users.id == m.user_id).one_or_none()[0],
        event_time=lambda v, c, m, p: datetime.strftime(m.event_time, '%d.%m.%Y %H:%M:%S')
    )

    column_default_sort = ('event_time', True)
    column_display_pk = False
    column_searchable_list = ('course',)

    column_filters = ('course', 'event_time')

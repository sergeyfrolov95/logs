# -*- coding: utf-8 -*-
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models.data import *

from datetime import datetime
from flask import request, url_for
from jinja2 import Markup
from sqlalchemy import func
from flask_admin import expose

class SequenceView(ModelView):

    can_create = False
    can_delete = False
    can_edit = False
    can_view_details = True
    can_export = True

    column_list = ('user_id', 'course', 'event_time', 'type', 'old', 'new')

    column_labels = dict(
        user_id=u'Имя пользователя',
        course=u'Идентификатор курса',
        event_time=u'Время события',
        type=u'Тип события',
        new=u'Новое расположение',
        old=u'Предыдущее расположение'
    )

    column_formatters = dict(
        user_id=lambda v, c, m, p: db.session.query(Users.username).filter(Users.id == m.user_id).one_or_none()[0],
        event_time=lambda v, c, m, p: datetime.strftime(m.event_time, '%d.%m.%Y %H:%M:%S'),
        type=lambda v, c, m, p: app.config['seq_types'][m.type]
    )

    column_default_sort = ('event_time', True)
    column_display_pk = False
    column_searchable_list = ('course',)

    column_choices = {
        'type': app.config['seq_types'].items()
    }
    column_filters = ('course', 'event_time', 'type')

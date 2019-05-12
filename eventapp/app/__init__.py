# -*- coding: utf-8 -*-
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

app.config['check_types'] = dict(
    showanswer=u'показан ответ',
    problem_show=u'показан ответ',
    problem_check=u'проверка ответа'
)
app.config['doc_types'] = dict()
app.config['enrollment_types'] = dict(
    enrollment_activated=u'регистрация на курсе',
    enrollment_deactivated=u'завершение курса'
)
app.config['seq_types'] = dict(
    seq_goto=u'Переход',
    seq_next=u'Следующая',
    seq_prev=u'Предыдущая'
)
app.config['video_types'] = dict(
    paused=u'Пауза',
    played=u'Воспроизведение',
    position_changed=u'Перемотка',
    stoped=u'Остановка',
    speed_change=u'Изменение скорости'
)

from app.models.data import *
from app.views import *

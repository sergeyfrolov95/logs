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
    showanswer='показан ответ',
    problem_show='показан ответ',
    problem_check='проверка ответа'
)
app.config['doc_types'] = dict()
app.config['enrollment_types'] = dict(
    enrollment_activated='регистрация на курсе',
    enrollment_deactivated='завершение курса'
)
app.config['seq_types'] = dict(
    seq_goto='Переход',
    seq_next='Следующая',
    seq_prev='Предыдущая'
)
app.config['video_types'] = dict(
    paused='Пауза',
    played='Воспроизведение',
    position_changed='Перемотка',
    stoped='Остановка',
    speed_change='Изменение скорости'
)

from app.models.data import *
from app.views import *

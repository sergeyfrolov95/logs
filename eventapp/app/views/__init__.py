# -*- coding: utf-8 -*-
from flask_admin import AdminIndexView, Admin

from app import app, db
from app.models.data import *

from .checkanswer import CheckAnswerView
from .users import UsersView
from .links import LinksView
from .sequence import SequenceView
from .video import VideoView
from .document import DocumentView
from .certificate import CertificateView
from .enrollment import EnrollmentView
from .others import OthersView
from .report1 import Report1View

admin = Admin(
    app,
    name='Event Logs',
    index_view=AdminIndexView(
        name='',
        url='/'
    )
)

admin.add_view(UsersView(Users, name=u'Пользователи', session=db.session, category=u'Справочники'))
admin.add_view(Report1View(Report1, name=u'Отчет 1', session=db.session, category=u'Справочники'))

admin.add_view(CheckAnswerView(CheckAnswerEvents, name=u'Проверка ответов', session=db.session, category=u'Типы событий'))
admin.add_view(LinksView(LinkEvents, name=u'Переходы по ссылкам', session=db.session, category=u'Типы событий'))
admin.add_view(SequenceView(SequenceEvents, name=u'Переходы по секциям', session=db.session, category=u'Типы событий'))
admin.add_view(VideoView(VideoEvents, name=u'Взаимодействие с видео', session=db.session, category=u'Типы событий'))
admin.add_view(DocumentView(DocumentEvents, name=u'Взаимодействие с докуметами', session=db.session, category=u'Типы событий'))
admin.add_view(CertificateView(CertificateEvents, name=u'Получение сертификата', session=db.session, category=u'Типы событий'))
admin.add_view(EnrollmentView(EnrollmentEvents, name=u'Регистрация на курсе', session=db.session, category=u'Типы событий'))
admin.add_view(OthersView(Others, name=u'Прочие события', session=db.session, category=u'Типы событий'))

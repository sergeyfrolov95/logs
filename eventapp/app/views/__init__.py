from flask_admin import AdminIndexView, Admin

from app import app, db
from app.models.data import *

from .checkanswer import CheckAnswerView
from .users import UsersView
from .links import LinksView
from .courses import CoursesView
from .sequence import SequenceView
from .video import VideoView
from .document import DocumentView
from .certificate import CertificateView
from .enrollment import EnrollmentView

admin = Admin(
    app,
    index_view=AdminIndexView(
        name='Home',
        url='/'
    )
)

admin.add_view(UsersView(Users, session=db.session, category='Справочники'))
admin.add_view(CoursesView(Courses, session=db.session, category='Справочники'))

admin.add_view(CheckAnswerView(CheckAnswerEvents, session=db.session, category='Типы событий'))
admin.add_view(LinksView(LinkEvents, session=db.session, category='Типы событий'))
admin.add_view(SequenceView(SequenceEvents, session=db.session, category='Типы событий'))
admin.add_view(VideoView(VideoEvents, session=db.session, category='Типы событий'))
admin.add_view(DocumentView(DocumentEvents, session=db.session, category='Типы событий'))
admin.add_view(CertificateView(CertificateEvents, session=db.session, category='Типы событий'))
admin.add_view(EnrollmentView(EnrollmentEvents, session=db.session, category='Типы событий'))

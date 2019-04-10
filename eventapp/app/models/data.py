from app import db, app
from geoalchemy2 import Geometry
from datetime import datetime

__all__ = (
    'Users',
    'Courses',
    'SequenceEvents',
    'VideoEvents',
    'DocumentEvents',
    'LinkEvents',
    'CheckAnswerEvents',
    'CertificateEvents',
    'EnrollmentEnent'
)

class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))


class Courses(db.Model):

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(128))


class SequenceEvents(db.Model):

    __tablename__ = 'sequence_events'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    user_id = db.Column(db.Integer)
    event_time = db.Column(db.DateTime)
    type = db.Column(db.String(128))
    new = db.Column(db.Integer)
    old = db.Column(db.Integer)


class VideoEvents(db.Model):

    __tablename__ = 'video_events'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    user_id = db.Column(db.Integer)
    event_time = db.Column(db.DateTime)
    type = db.Column(db.String(128))
    timecode = db.Column(db.String(128))


class DocumentEvents(db.Model):

    __tablename__ = 'document_events'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    user_id = db.Column(db.Integer)
    event_time = db.Column(db.DateTime)
    type = db.Column(db.String(128))
    new = db.Column(db.Integer)
    old = db.Column(db.Integer)


class LinkEvents(db.Model):

    __tablename__ = 'link_events'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    user_id = db.Column(db.Integer)
    event_time = db.Column(db.DateTime)
    current_url = db.Column(db.String)
    target_url = db.Column(db.String)


class CheckAnswerEvents(db.Model):

    __tablename__ = 'check_answer_events'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    user_id = db.Column(db.Integer)
    event_time = db.Column(db.DateTime)
    type = db.Column(db.String(128))
    problem_id = db.Column(db.String)
    attempts = db.Column(db.Integer)
    success = db.Column(db.Boolean)


class CertificateEvents(db.Model):

    __tablename__ = 'certificate_events'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    user_id = db.Column(db.Integer)
    event_time = db.Column(db.DateTime)
    course_id = db.Column(db.String)


class EnrollmentEnent(db.Model):

    __tablename__  = 'enrollment_evnts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    user_id = db.Column(db.Integer)
    event_time = db.Column(db.DateTime)
    type = db.Column(db.String(128))
    course_id = db.Column(db.String)

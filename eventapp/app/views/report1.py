# -*- coding: utf-8 -*-
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models.data import *
from flask import flash, redirect, request, url_for, send_file
from flask_admin.model.template import EndpointLinkRowAction
from appy.pod.renderer import Renderer
from os.path import join as os_join, basename, exists
from sqlalchemy import and_

from datetime import datetime
from jinja2 import Markup
from sqlalchemy import func
from flask_admin import expose
from os import remove
import matplotlib.pyplot as plt

class Report1View(ModelView):

    column_extra_row_actions = [
        EndpointLinkRowAction('fa fa-file glyphicon icon-file', 'report1.create_report'),
    ]

    can_create = False
    can_delete = False
    can_edit = True
    can_view_details = False
    can_export = True

    column_list = ('user_id', 'course', 'per_start', 'per_end')
    form_columns = ('user_id', 'course', 'per_start', 'per_end')

    column_labels = dict(
        user_id=u'Имя пользователя',
        course=u'Идентификатор курса',
        per_start=u'Начало промежутка',
        per_end=u'Конец промежутка'
    )

    column_formatters = dict(
        user_id=lambda v, c, m, p: db.session.query(Users.username).filter(Users.id == m.user_id).one_or_none()[0] if m.user_id else '',
        per_start=lambda v, c, m, p: datetime.strftime(m.per_start, '%d.%m.%Y') if m.per_start else '',
        per_end=lambda v, c, m, p: datetime.strftime(m.per_end, '%d.%m.%Y') if m.per_end else ''
    )

    column_display_pk = False

    @expose('/report')
    def create_report(self):
        data={}
        user_id = db.session.query(Report1.user_id)\
                .filter(Report1.id == request.args.get('id')).one_or_none()[0]
        data['username'] = db.session.query(Users.username)\
                .filter(Users.id == user_id).one_or_none()[0]
        data['lastseen'] = datetime.strftime(
            db.session.query(Others.event_time)\
            .filter(Others.user_id == user_id)\
            .order_by(Others.event_time.desc()).first()[0],
            '%d.%m.%Y %H:%M:%S')
        courses = db.session.query(EnrollmentEvents.course, EnrollmentEvents.event_time)\
                .filter(and_(EnrollmentEvents.user_id == user_id,
                            EnrollmentEvents.type == 'enrollment_activated'))
        data['courses'] = []
        count = 1
        for c in courses.all():
            row = {}
            row['pp'] = count
            row['course'] = c.course
            count += 1
            row['reg_time'] = datetime.strftime(c.event_time, '%d.%m.%Y %H:%M:%S')
            deact_time = db.session.query(EnrollmentEvents.event_time)\
                .filter(and_(EnrollmentEvents.user_id == user_id,
                        EnrollmentEvents.type == 'enrollment_deactivated')).first()
            row['deact_time'] = datetime.strftime(deact_time[0], '%d.%m.%Y %H:%M:%S') if deact_time else u'---'
            cert_time = db.session.query(CertificateEvents.event_time)\
                .filter(and_(CertificateEvents.course == c.course,
                        CertificateEvents.user_id == user_id)).first()
            row['cert_time'] = datetime.strftime(cert_time[0], '%d.%m.%Y %H:%M:%S') if cert_time else u'---'
            right = db.session.query(CheckAnswerEvents.event_time)\
                .filter(and_(CheckAnswerEvents.type == 'problem_check',
                            CheckAnswerEvents.success == True,
                            CheckAnswerEvents.user_id == user_id)).all()
            false = db.session.query(CheckAnswerEvents.event_time)\
                .filter(and_(CheckAnswerEvents.type == 'problem_check',
                            CheckAnswerEvents.success == False,
                            CheckAnswerEvents.user_id == user_id)).all()
            row['rf'] = str(len(right)) + u'/' + str(len(false))

            data['courses'].append(row)

        #second plot
        plt.rcdefaults()
        fig, ax = plt.subplots()
        events = (u'Серт.',
                u'Пров. отв.',
                u'Докум.',
                u'Регистр.',
                u'Сылки',
                u'Навиг.',
                u'Видео')
        y_pos = range(len(events))
        plot_values = (
            len(db.session.query(CertificateEvents.id).filter(CertificateEvents.user_id == user_id).all()),
            len(db.session.query(CheckAnswerEvents.id).filter(CheckAnswerEvents.user_id == user_id).all()),
            len(db.session.query(DocumentEvents.id).filter(DocumentEvents.user_id == user_id).all()),
            len(db.session.query(EnrollmentEvents.id).filter(EnrollmentEvents.user_id == user_id).all()),
            len(db.session.query(LinkEvents.id).filter(LinkEvents.user_id == user_id).all()),
            len(db.session.query(SequenceEvents.id).filter(SequenceEvents.user_id == user_id).all()),
            len(db.session.query(VideoEvents.id).filter(VideoEvents.user_id == user_id).all())
        )

        ax.barh(y_pos, plot_values, xerr=None, align='center', color='orange', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(events)
        ax.invert_yaxis()
        ax.set_xlabel(u'Количество событий')
        ax.set_title(u'Количество собыий по группам')
        plt.savefig(os_join(app.config['REPORT_PATH'], 'plt2.png'))
        data['plt2_path'] = os_join(app.config['REPORT_PATH'], 'plt2.png')

        #third plot
        plt.rcdefaults()
        fig, ax = plt.subplots()
        events = (u'Докум.',
                u'Курс',
                u'Видео')
        y_pos = range(len(events))
        plot_values = (
            len(db.session.query(DocumentEvents.id).filter(DocumentEvents.user_id == user_id).all()),
            len(db.session.query(LinkEvents.id).filter(LinkEvents.user_id == user_id).all())+\
            len(db.session.query(SequenceEvents.id).filter(SequenceEvents.user_id == user_id).all()),
            len(db.session.query(VideoEvents.id).filter(VideoEvents.user_id == user_id).all())
        )

        ax.barh(y_pos, plot_values, xerr=None, align='center', color='blue', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(events)
        ax.invert_yaxis()
        ax.set_xlabel(u'Количество собыий')
        ax.set_title(u'Предпочитаемые материалы')
        plt.savefig(os_join(app.config['REPORT_PATH'], 'plt3.png'))
        data['plt3_path'] = os_join(app.config['REPORT_PATH'], 'plt3.png')

        f_name = os_join(app.config['REPORT_PATH'], 'report_res.odt')
        if exists(f_name):
            remove(f_name)
        Renderer(
            os_join(app.config['REPORT_PATH'], "user_report.odt"),
            data,
            f_name,
            pythonWithUnoPath='/usr/bin/python3'
        ).run()

        return send_file(
            filename_or_fp=f_name,
            as_attachment=True,
            attachment_filename=basename(f_name),
            mimetype='application/vnd.oasis.opendocument.text'
        )

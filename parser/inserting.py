import psycopg2
import json


conn = psycopg2.connect(dbname='events', user='sergey',
                        host='localhost')
cursor = conn.cursor()

_dict = {
	'"event_type": "problem_check"': {
		'type': 'problem_check',
	},
    '"event_type": "edx.course.enrollment.activated"': {
        'type': 'enrollment_activated'
    },
    '"event_type": "page_close"': {
        'type': 'page_close'
    },
    '"event_type": "seq_goto"': {
        'type': 'seq_goto'
    },
    '"event_type": "seq_next"': {
        'type': 'seq_next'
    },
    '"event_type": "seq_prev"': {
        'type': 'seq_prev'
    },
    '"event_type": "problem_show"': {
        'type': 'problem_show'
    },
    '"event_type": "showanswer"': {
        'type': 'showanswer'
    }
}

users = {}

def others(event, users):
    if not event['context'].get('user_id', None):
        return 0
    if not event['time']:
        return 0
    user = (event['context']['user_id'], event['username'])
    if user[0] not in users:
        users[user[0]] = user[1]
        insert = """insert into users (id, username)
                values {}""".format(user)
        cursor.execute(insert)
    tup = (
        user[0],
        event['time']
    )
    insert = """insert into others (user_id, event_time) values
            {}""".format(tup)
    cursor.execute(insert)


def problem_check(event, users):
    user = (event['context']['user_id'], event['username'])
    if user[0] not in users:
        users[user[0]] = user[1]
        insert = """insert into users (id, username)
                values {}""".format(user)
        cursor.execute(insert)

    tup = [
        event['context']['user_id'],
        event['context']['course_id'],
        event['time'],
        _dict['"event_type": "problem_check"']['type'],
        event['event']['attempts'] if type(event.get('event', None)) != str else 0,
        event['event']['success'] if type(event.get('event', None)) != str else ''
    ]
    tup[5] = True if tup[5] == 'correct' else False
    insert = """insert into check_answer_events
                (user_id, course, event_time, type, attempts, success)
                values {}""".format(tuple(tup))

    cursor.execute(insert)

def enrollment_activated(event, users):
    user = (event['event']['user_id'], event['username'])
    if user[0] not in users:
        users[user[0]] = user[1]
        insert = """insert into users (id, username)
                values {}""".format(user)
        cursor.execute(insert)

    tup = (
        event['event']['user_id'],
        event['context']['course_id'],
        event['time'],
        _dict['"event_type": "edx.course.enrollment.activated"']['type']
    )
    insert = """insert into enrollment_evnts
                (user_id, course, event_time, type)
                values {}""".format(tup)

    cursor.execute(insert)

def page_close(event, users):
    if not event['context'].get('user_id', None):
        return 0
    user = (event['context']['user_id'], event['username'])
    if user[0] not in users:
        users[user[0]] = user[1]
        insert = """insert into users (id, username)
                values {}""".format(user)
        cursor.execute(insert)

    tup = (
        event['context']['user_id'],
        event['context']['course_id'],
        event['time'],
        event['page'],
        ''
    )
    insert = """insert into link_events
                (user_id,course, event_time, current_url, target_url)
                values {}""".format(tup)

    cursor.execute(insert)

def seq_goto(event, users):
    user = (event['context']['user_id'], event['username'])
    if user[0] not in users:
        users[user[0]] = user[1]
        insert = """insert into users (id, username)
                values {}""".format(user)
        cursor.execute(insert)

    new_old = json.loads(event['event'])
    tup = (
        event['context']['user_id'],
        event['context']['course_id'],
        event['time'],
        _dict['"event_type": "seq_goto"']['type'],
        new_old['new'],
        new_old['old']
    )
    insert = """insert into sequence_events
                (user_id, course, event_time, type, new, old)
                values {}""".format(tup)
    cursor.execute(insert)

def seq_next(event, users):
    user = (event['context']['user_id'], event['username'])
    if user[0] not in users:
        users[user[0]] = user[1]
        insert = """insert into users (id, username)
                values {}""".format(user)
        cursor.execute(insert)

    new_old = json.loads(event['event'])
    tup = (
        event['context']['user_id'],
        event['context']['course_id'],
        event['time'],
        _dict['"event_type": "seq_next"']['type'],
        new_old['new'],
        new_old['old']
    )
    insert = """insert into sequence_events
                (user_id, course, event_time, type, new, old)
                values {}""".format(tup)
    cursor.execute(insert)

def seq_prev(event, users):
    user = (event['context']['user_id'], event['username'])
    if user[0] not in users:
        users[user[0]] = user[1]
        insert = """insert into users (id, username)
                values {}""".format(user)
        cursor.execute(insert)

    new_old = json.loads(event['event'])
    tup = (
        event['context']['user_id'],
        event['context']['course_id'],
        event['time'],
        _dict['"event_type": "seq_prev"']['type'],
        new_old['new'],
        new_old['old']
    )
    insert = """insert into sequence_events
                (user_id, course, event_time, type, new, old)
                values {}""".format(tup)
    cursor.execute(insert)

def problem_show(event, users):
    user = (event['context']['user_id'], event['username'])
    if user[0] not in users:
        users[user[0]] = user[1]
        insert = """insert into users (id, username)
                values {}""".format(user)
        cursor.execute(insert)

    tup = (
        event['context']['user_id'],
        event['context']['course_id'],
        event['time'],
        _dict['"event_type": "problem_show"']['type'],
        0,
        False
    )
    insert = """insert into check_answer_events
                (user_id, course, event_time, type, attempts, success)
                values {}""".format(tup)

    cursor.execute(insert)

def showanswer(event, users):
    user = (event['context']['user_id'], event['username'])
    if user[0] not in users:
        users[user[0]] = user[1]
        insert = """insert into users (id, username)
                values {}""".format(user)
        cursor.execute(insert)

    tup = (
        event['context']['user_id'],
        event['context']['course_id'],
        event['time'],
        _dict['"event_type": "showanswer"']['type'],
        0,
        False
    )
    insert = """insert into check_answer_events
                (user_id, course, event_time, type, attempts, success)
                values {}""".format(tup)

    cursor.execute(insert)

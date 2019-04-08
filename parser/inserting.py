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

def problem_check(event):
    tup = [
        event['username'],
        event['context']['user_id'],
        event['time'],
        _dict['"event_type": "problem_check"']['type'],
        event['context']['course_id'],
        event['event']['attempts'] if type(event.get('event', None)) != str else 0,
        event['event']['success'] if type(event.get('event', None)) != str else ''
    ]
    tup[6] = True if tup[6] == 'correct' else False
    insert = """insert into check_answer_events
                (username, user_id, event_time, type, problem_id, attempts, success)
                values {}""".format(tuple(tup))

    cursor.execute(insert)
    conn.commit()

def enrollment_activated(event):
    tup = (
        event['username'],
        event['event']['user_id'],
        event['time'],
        _dict['"event_type": "edx.course.enrollment.activated"']['type'],
        event['context']['course_id']
    )
    insert = """insert into enrollment_evnts
                (username, user_id, event_time, type, course_id)
                values {}""".format(tup)

    cursor.execute(insert)
    conn.commit()

def page_close(event):
    tup = (
        event['username'],
        event['context']['user_id'] if event['context']['user_id'] is not None else 0,
        event['time'],
        event['page'],
        ''
    )
    insert = """insert into link_events
                (username, user_id, event_time, current_url, target_url)
                values {}""".format(tup)

    cursor.execute(insert)
    conn.commit()

def seq_goto(event):
    new_old = json.loads(event['event'])
    tup = (
        event['username'],
        event['context']['user_id'],
        event['time'],
        _dict['"event_type": "seq_goto"']['type'],
        new_old['new'],
        new_old['old']
    )
    insert = """insert into sequence_events
                (username, user_id, event_time, type, new, old)
                values {}""".format(tup)
    cursor.execute(insert)
    conn.commit()

def seq_next(event):
    new_old = json.loads(event['event'])
    tup = (
        event['username'],
        event['context']['user_id'],
        event['time'],
        _dict['"event_type": "seq_next"']['type'],
        new_old['new'],
        new_old['old']
    )
    insert = """insert into sequence_events
                (username, user_id, event_time, type, new, old)
                values {}""".format(tup)
    cursor.execute(insert)
    conn.commit()

def seq_prev(event):
    new_old = json.loads(event['event'])
    tup = (
        event['username'],
        event['context']['user_id'],
        event['time'],
        _dict['"event_type": "seq_prev"']['type'],
        new_old['new'],
        new_old['old']
    )
    insert = """insert into sequence_events
                (username, user_id, event_time, type, new, old)
                values {}""".format(tup)
    cursor.execute(insert)
    conn.commit()

def problem_show(event):
    tup = (
        event['username'],
        event['context']['user_id'],
        event['time'],
        _dict['"event_type": "problem_show"']['type'],
        event['context']['course_id'],
        0,
        False
    )
    insert = """insert into check_answer_events
                (username, user_id, event_time, type, problem_id, attempts, success)
                values {}""".format(tup)

    cursor.execute(insert)
    conn.commit()

def showanswer(event):
    tup = (
        event['username'],
        event['context']['user_id'],
        event['time'],
        _dict['"event_type": "showanswer"']['type'],
        event['context']['course_id'],
        0,
        False
    )
    insert = """insert into check_answer_events
                (username, user_id, event_time, type, problem_id, attempts, success)
                values {}""".format(tup)

    cursor.execute(insert)
    conn.commit()

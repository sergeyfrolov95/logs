import psycopg2


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
        event['time'],
        _dict['"event_type": "problem_check"']['type'],
        event['context']['course_id'],
        event['event']['attempts'] if type(event.get('event', None)) != str else 0,
        event['event']['success'] if type(event.get('event', None)) != str else ''
    ]
    tup[5] = True if tup[5] == 'correct' else False
    insert = """insert into check_answer_events
                (user_id, event_time, type, problem_id, attempts, success)
                values {}""".format(tuple(tup))

    cursor.execute(insert)
    conn.commit()

def enrollment_activated:
    pass

def page_close:
    pass

def seq_goto:
    pass

def seq_next:
    pass

def seq_prev:
    pass

def problem_show:
    pass

def showanswer::
    pass

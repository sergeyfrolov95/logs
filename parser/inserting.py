import psycopg2


conn = psycopg2.connect(dbname='events', user='sergey',
                        host='localhost')
cursor = conn.cursor()

_dict = {
	'"event_type": "problem_check"': {
		'type': 'problem_check',
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

import os
import json
from json import JSONDecodeError

from inserting import *

import time
start_time = time.time()


cool_list = [
	'"event_type": "book"', 								#document_events
	'"event_type": "edx.certificate.created"',				#certificate_events
	'"event_type": "edx.course.enrollment.activated"',		###enrollment_evnts
	'"event_type": "edx.course.enrollment.deactivated"',	#enrollment_evnts
	'"event_type": "edx.video.paused"',						#video_events
	'"event_type": "edx.video.played"',						#video_events
	'"event_type": "edx.video.position.changed"',			#video_events
	'"event_type": "edx.video.stoped"',						#video_events
	'"event_type": "speed_change_video"',					#video_events
	'"event_type": "page_close"',							###link_events
	'"event_type": "seq_goto"',								###sequence_events
	'"event_type": "seq_next"',								###sequence_events
	'"event_type": "seq_prev"',								###sequence_events
	'"event_type": "problem_check"',						###check_answer_events
	'"event_type": "problem_check_fail"',					#check_answer_events
	'"event_type": "problem_show"',							###check_answer_events
	'"event_type": "showanswer"',							###check_answer_events
	'"event_type": "hint"'									#check_answer_events
]

cool_dict = {
    "book": 0,
	"edx.certificate.created": 0,
	"edx.course.enrollment.activated": 0,
	"edx.course.enrollment.deactivated": 0,
	"edx.video.paused": 0,
	"edx.video.played": 0,
	"edx.video.position.changed": 0,
	"edx.video.stoped": 0,
	"speed_change_video": 0,
	"page_close": 0,
	"seq_goto": 0,
	"seq_next": 0,
	"seq_prev": 0,
	"problem_check": 0,
	"problem_check_fail": 0,
	"problem_show": 0,
	"showanswer": 0,
	"hint": 0
}

sourse_path = "/home/sergey/Documents/logs/data_source/"
count = 0
cool = 0
for filename in os.listdir(sourse_path):
	if filename.startswith("tracking"):
		with open(sourse_path + filename, "r") as f:
			f = f.read()
			_list = f.split("\n")
			for l in _list:
				other = True
				for c in cool_list:
					if c in l:
						other = False
						cool += 1
						cool_dict[c.split(': ')[1].replace('"', '')] += 1
						if c == '"event_type": "problem_check"':
							event = json.loads(l)
							problem_check(event, users)
						elif c == '"event_type": "edx.course.enrollment.activated"':
							event = json.loads(l)
							enrollment_activated(event, users)
						elif c == '"event_type": "page_close"':
							event = json.loads(l)
							page_close(event, users)
						elif c == '"event_type": "seq_goto"':
							event = json.loads(l)
							seq_goto(event, users)
						elif c == '"event_type": "seq_next"':
							event = json.loads(l)
							seq_next(event, users)
						elif c == '"event_type": "seq_prev"':
							event = json.loads(l)
							seq_prev(event, users)
						elif c == '"event_type": "problem_show"':
							event = json.loads(l)
							problem_show(event, users)
						elif c == '"event_type": "showanswer"':
							event = json.loads(l)
							showanswer(event, users)
				if other:
					try:
						event = json.loads(l)
						others(event, users)
					except JSONDecodeError as e:
						continue

			count += len(_list)
insert_courses()
conn.commit()
print("\nTotal:\t" + str(count))
print("\nUseful:\t" + str(cool) + "\n")
print("Types with count:\n")
for k, v in cool_dict.items():
	print(k + ': ' + str(v))
print("\n--- %s seconds ---" % round((time.time() - start_time), 1))

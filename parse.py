import os

cool_list = [
	'"event_type": "book"',
	'"event_type": "edx.certificate.created"',
	'"event_type": "edx.course.enrollment.activated"',
	'"event_type": "edx.course.enrollment.deactivated"',
	'"event_type": "edx.video.paused"',
	'"event_type": "edx.video.played"',
	'"event_type": "edx.video.position.changed"',
	'"event_type": "edx.video.stoped"',
	'"event_type": "speed_change_video"',
	'"event_type": "page_close"',
	'"event_type": "seq_goto"',
	'"event_type": "seq_next"',
	'"event_type": "seq_prev"',
	'"event_type": "problem_check"',
	'"event_type": "problem_check_fail"',
	'"event_type": "problem_show"',
	'"event_type": "showanswer"',
	'"event_type": "hint"'
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

sourse_path = "/home/seleza/Documents/logs/data_source/"
count = 0
cool = 0
for filename in os.listdir(sourse_path):
	if filename.startswith("tracking"):
		with open(sourse_path + filename, "r") as f:
			f = f.read()
			_list = f.split("\n")
			for l in _list:
				for c in cool_list:
					if c in l:
						cool_dict[c.split(': ')[1].replace('"', '')] += 1
						cool +=1
 			count += len(_list)
			print filename + "\t" + str(len(_list))
print  "\nTotal:" + "\t" + str(count)
print "\nUseful:" + "\t" + str(cool) + "\n"
print "Types with count:\n"
for k, v in cool_dict.iteritems():
	print k + ': ' + str(v)

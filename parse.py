import os

count = 0
for filename in os.listdir('/home/seleza/Documents/logs'):
	if filename.startswith('tracking'):
		with open(filename, 'r') as f:
			f = f.read()
			_list = f.split('\n')
			print '\n' + _list[0] + '\n'
 			count += len(_list)
			print filename + '\t' + str(len(_list))
print  "\nTotal:" + '\t' + str(count)

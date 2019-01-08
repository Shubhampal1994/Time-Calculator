def time_calc(last_total, time):
	"""
	'time' must be in format '(+/-)hh:mm:ss'
	"""
	
	
	time_format = time[0]
	print(time_format)
	pure_time = time[1:]
	print(pure_time)

	input_time_list = [int(mono_time) for mono_time in pure_time.split(':')]
	print(input_time_list)

	total_time_list = [int(mono_time) for mono_time in last_total.split(':')]
	print(total_time_list)

	if (time_format == '+'):
	
		t_sec = input_time_list[-1] + total_time_list[-1]
		print(t_sec)
		t_min = input_time_list[-2] + total_time_list[-2]
		print(t_min)
		t_hour = input_time_list[-3] + total_time_list[-3]
		print(t_hour)

		if t_sec > 59:
			t_min += 1
			t_sec = t_sec - 60

		if t_min > 59:
			t_hour += 1
			t_min = t_min - 60

		last_total = [str(t_hour), str(t_min), str(t_sec)]
		print(last_total)
		last_total = ':'.join(last_total)
		print('Total time: {}'.format(last_total))
		return last_total

	elif (time_format == '-'):
		
		t_sec = total_time_list[-1] - input_time_list[-1]
		print(t_sec)
		t_min = total_time_list[-2] - input_time_list[-2]
		print(t_min)
		t_hour = total_time_list[-3] - input_time_list[-3]
		print(t_hour)

		if t_sec < 0:
			t_min -= 1
			t_sec = 60 + t_sec

		if t_min < 0:
			t_hour -= 1
			t_min = 60 + t_min

		last_total = [str(t_hour), str(t_min), str(t_sec)]
		print(last_total)
		last_total = ':'.join(last_total)
		print('Total time: {}'.format(last_total))
		return last_total

	else:
		print('Please enter time in correct format')

last_total = '00:00:00'

while True:

	input_time = input("Please Enter time (format: '(+/-)hh:mm:ss'): ")
	last_total = time_calc(last_total, input_time)
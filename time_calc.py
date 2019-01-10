def time_calculator(input_time):
	"""
	'time' must be in format '(+/-)hh:mm:ss'
	+02:30:10-01:40:20
	"""
	
	if input_time[0] not in '+-':
		# formating the first time if no sign given
		input_time = '+' + input_time

	positive_time_hours = 0
	positive_time_min = 0
	positive_time_sec = 0

	negative_time_hours = 0
	negative_time_min = 0
	negative_time_sec = 0

	for time in range(0, len(input_time), 9):
		get_time_list = input_time[(time + 1):(time + 9)].split(':')

		if input_time[time] == '+':
			# it can also calculate by separating out to this way
			positive_time_hours += int(get_time_list[0])
			positive_time_min += int(get_time_list[1])
			positive_time_sec += int(get_time_list[2])

		else:
			negative_time_hours += int(get_time_list[0])
			negative_time_min += int(get_time_list[1])
			negative_time_sec += int(get_time_list[2])

	positive_times = get_correct_calculation_time(
		positive_time_hours,
		positive_time_min,
		positive_time_sec
	)

	negative_times = get_correct_calculation_time(
		negative_time_hours,
		negative_time_min,
		negative_time_sec
	)

	return final_calculation(positive_times, negative_times)

def get_correct_calculation_time(hours, mins, secs):
	
	if secs >= 60:
		mins += (secs // 60)
		secs = (secs % 60)

	if mins >= 60:
		hours += (mins // 60)
		mins = (mins % 60)

	return (hours, mins, secs)

def final_calculation(positive_times, negative_times):

	secs = positive_times[2] - negative_times[2]
	secs = (60*positive_times[1]) - (60 *negative_times[1]) + secs
	secs = (3600*positive_times[0]) - (3600 *negative_times[0]) + secs

	sign = '+' if secs >= 0 else '-'
	secs = abs(secs)

	hours = secs // 3600
	secs = secs % 3600

	mins = secs // 60
	secs = secs % 60

	return "%s%s:%s:%s" % (sign, str(hours).zfill(2), str(mins).zfill(2), str(secs).zfill(2))

initial_time = '+00:00:00'

while True:
	
	input_time = input("Enter the Time (format: '(+/-)hh:mm:ss'): ")
	input_time_list = input_time[1:].split(':')

	if (len(input_time_list[0]) < 2):
		input_time_list[0] = input_time_list[0].zfill(2)

	input_time_str = ':'.join(input_time_list)
	input_time = input_time[0] + input_time_str
	input_time = '{}{}'.format(initial_time, input_time)
	print('Input Time: ', input_time)

	initial_time = time_calculator(input_time)
	print('Total Time: ', initial_time)
import math
raw_data = open('data.txt', 'r').read().replace('\r', ',').replace('\n', ',')

data = [i for i in raw_data.split(',')]

def getSeat(boarding_pass: str):
	row_range = range(128)
	col_range = range(8)
	for i in boarding_pass:
		if i == 'F':
			row_range = row_range[0:math.floor(len(row_range)/2)]
		elif i == 'B':
			row_range = row_range[math.floor(len(row_range)/2):]
		elif i == 'L':
			col_range = col_range[0:math.floor(len(col_range)/2)]
		elif i == 'R':
			col_range = col_range[math.floor(len(col_range)/2):]
	result = []
	for i in row_range:
		result.append(i)
	for i in col_range:
		result.append(i)
	return result[0]*8 + result[1]

max_ID = 0
num_list = []
for i in data:
	num = getSeat(i)
	num_list.append(getSeat(i))
	if num >= max_ID:
		max_ID = num

print('Part 1: ' + str(max_ID))

num_list = sorted(num_list)

for i in range(len(num_list) - 1):
	if num_list[i] + 2 == num_list[i + 1]:
		print('Part 2: ' + str(num_list[i] + 1))






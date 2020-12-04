raw_data = open("data.txt", "r").read().replace('\r', ',').replace('\n', ',')

data = [i.split(' ') for i in raw_data.split(',')]

class Password():
	def __init__(self, num, char, pw):
		self.char = char
		self.pw = pw
		self.num = num.replace('-', ' ').split(' ')
		self.from_num = int(self.num[0])
		self.to_num = int(self.num[1])

	def check_pass(self):
		count = 0
		for i in self.pw:
			if i in self.char:
				count += 1
		if count >= self.from_num and count <= self.to_num:
			return True

	def check_pass_OTCAS(self):
		for i in self.pw:
			if i in self.char:
				if len(self.pw) >= self.to_num:
					first_place = self.pw[self.from_num-1]
					second_place = self.pw[self.to_num-1]
					if (i == first_place and i != second_place) or (i != first_place and i == second_place):
						return True

num = 0
for i in data:
	pw = Password(i[0], i[1], i[2])
	if pw.check_pass():
		num += 1
print('Part 1: ' + str(num))

num2 = 0
for i in data:
	pw = Password(i[0], i[1], i[2])
	if pw.check_pass_OTCAS():
		num2 += 1
print('Part 2: ' + str(num2))


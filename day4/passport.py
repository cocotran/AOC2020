import re
data = open('data.txt', 'r').readlines()

batch_file = []

for i in data:
	if i.strip() != '':
		batch_file.append(i.rstrip())
	else:
		batch_file.append('@')

file_str = ' '.join(batch_file)
batch_file = [i.strip() for i in file_str.split('@')]

fiels = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def isMatch(words: list, text: str):
	count = 0
	for i in words:
		if re.search(i, text):
			count += 1
	return (count == len(words))


count = 0
for i in batch_file:
	if isMatch(fiels, i):
		count += 1
print("Part 1: " + str(count))


batch_file_array= []
for i in batch_file:
	batch_file_array.append([i])

batch_file_array = [i[0].split(' ') for i in batch_file_array]

def check_passport(passport: list):
	def check_byr(arr: str):
		return (len(arr) == 4 and int(arr) >= 1920 and int(arr) <= 2002)
	
	def check_iyr(arr: str):
		return (len(arr) == 4 and int(arr) >= 2010 and int(arr) <= 2020)

	def check_eyr(arr: str):
		return (len(arr) == 4 and int(arr) >= 2020 and int(arr) <= 2030)

	def check_height(arr: str):
		if 'cm' in arr:
			arr = int(arr.replace('cm', ''))
			return (arr >= 150 and arr <= 193)
		else:
			arr = int(arr.replace('in', ''))
			return (arr >= 59 and arr <= 76)

	def check_hcl(arr: str):
		if '#' in arr:
			arr = arr.replace('#','')
			return (len(arr) == 6 and arr.isalnum())

	def check_ecl(arr: str):
		colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		return (arr in colors)

	def check_pid(arr: str):
		return (len(arr) == 9 and arr.isdigit())

	def scan(passport: list):
		fiels = {'byr': check_byr,'iyr': check_iyr,'eyr': check_eyr,'hgt': check_height,'hcl': check_hcl,'ecl': check_ecl,'pid': check_pid}
		count = 0
		for i in passport:
			if i[:3] in fiels.keys():
				if fiels[i[:3]](i[4:]):
					count += 1
		return (count == 7)

	return scan(passport)


count1 = 0
for i in batch_file_array:
	if check_passport(i):
		count1 += 1

print('Part 2: ' + str(count1))







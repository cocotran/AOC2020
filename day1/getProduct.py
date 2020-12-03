report_str = open("data.txt", "r").read().replace('\r', ',').replace('\n', ',')

report = [int(i) for i in report_str.split(',')]

def getProduct3(report):
	for i in report:
		for j in report:
			third_num = 2020 - (i + j)
			if third_num in report:
				product = i * j * third_num
				return product

print("Part 2: " + str(getProduct3(report)))

def getProduct2(report):
	for i in report:
		for j in range(len(report)):
			sum = i + report[j]
			if sum == 2020:
				product = i * report[j]
				return product
		report.pop(0)

print("Part 1: " + str(getProduct2(report)))
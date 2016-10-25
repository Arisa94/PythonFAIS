def roman2int(number):
	roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
	iterator = 1
	result = roman[number[-iterator]]
	temp = result
	numberTemp = number
	number = number[:-1]
	for i in number[::-1]:
		if temp > roman[i]:
			result = result - roman[i]
		else:
			result = roman[i] + result
		if iterator < len(number):
			iterator = iterator + 1
			temp = roman[numberTemp[-iterator]]
	return result
number = "MMXVI"
result = roman2int(number)

print result
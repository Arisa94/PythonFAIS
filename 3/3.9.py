def accumulate(i):
	x = 0
	for j in i:
		x = x + j
	return x
	
list = [[],[4],(1,2),[3,4],(5,6,7)]
x = []
for i in list:
	x.append(accumulate(i))
print x
	
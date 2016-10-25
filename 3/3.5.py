def fillWithSpaces(x):
	while len(x) < 5:
		x = " " + x
	return x

x = input("")

print "|...." * x + "|"
numbers = "0"
for i in range(x):
	numbers = numbers + fillWithSpaces(str(i+1))
print numbers
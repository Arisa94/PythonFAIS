sekwencja1 = "To moja pierwsza sekwencja"
sekwencja2 = "To moja druga sekwencja to moja"

sekwencja1 = sekwencja1.lower()
sekwencja2 = sekwencja2.lower()
x = sekwencja1.split()
y = sekwencja2.split()

x = list(set(x))
y = list(set(y))

z = []

for i in x:
	for j in y:
		if i == j:
			z.append(i)
print z

z = x + y
z = list(set(z))

print z
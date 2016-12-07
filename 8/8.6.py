from time import *

P = {(0, 0): 0.5, (0, 1): 1.0, (1, 0): 0.0}

def Dyn(i, j):
	if i < 0:
		raise ValueError('i < 0')
	elif j < 0:
		raise ValueError('j < 0')
	else:
		if i == 0:
			return 1.0
		elif j == 0:
			return 0.0
		else:
			result = P.get((i, j))
			if result != None:
				return result
			else:
				result = 0.5 * (Dyn(i - 1, j) + Dyn(i, j - 1))
				P[(i, j)] = result
				return result

def Rec(i, j):
	if i < 0:
		raise ValueError('i < 0')
	elif j < 0:
		raise ValueError('j < 0')
	else:
		if i == 0 and j == 0:
			return 0.5
		elif i == 0:
			return 1.0
		elif j == 0:
			return 0.0
		else:
			return 0.5 * (Rec(i - 1, j) + Rec(i, j - 1))

a = 1
b = 2			
			
startTime = clock()
str(Rec(a, b))
time = clock() - startTime
startTime = clock()
str(Dyn(a, b))
time2 = clock() - startTime

if time < time2:
	print 'Rekurencja!'
else:
	print 'Dynamiczne!'
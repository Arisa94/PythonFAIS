from math import *
from random import *

def calc_pi(n):
	field = 0
	fieldSquare = 0
	r = 1
	
	for i in range(0, n):
		x = uniform(0, 1)
		y = uniform(0, 1)
		distance = sqrt(pow(x, 2) + pow(y, 2))
		
		if distance <= r:
			field += 1
			
		else:
			fieldSquare += 1
			
	if fieldSquare == 0:
		raise ValueError ("Dzielenie przez 0")
		
	return field / float(fieldSquare)
	
print calc_pi(999999999)
# -*- coding: utf-8 -*-
def solve1(a, b, c):
	if(a == 0):
		return 'y = ' + str(-c/b)
	if(b == 0):
		return 'x = ' + str(-c/a)
	if(a == 1):
		return 'x = -' + str(b) + 'y - ' + str(c)
	return 'x = -(' + str(b) + 'y + ' + str(c) +') / ' + str(a) 

print(solve1(1,4,3))
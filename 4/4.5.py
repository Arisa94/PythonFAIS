def odwracanieIteracyjnie(L, left, right):
	while left < right:
		L[left], L[right] = L[right], L[left]
		left += 1
		right -= 1

def odwracanieRekurencyjnie(L, left, right):
	if(left < right):
		L[left], L[right] = L[right], L[left]
		odwracanieRekurencyjnie(L, left+1, right - 1)

list  = [1, 2, 3, 4]
print list
odwracanieIteracyjnie(list, 0, 2);
print list

list  = [1, 2, 3, 4]
print list
odwracanieRekurencyjnie(list, 0, 2);
print list

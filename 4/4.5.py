def odwracanie(L, left, right):
    L = L[:left] + L[left:(right + 1)][::-1] + L[(right + 1):]
    return L
   
L = [1, 2, 3, 4, 10, 13, 9, 4, 5]
left = 2
right = 7
result = odwracanie(L, left, right)
print result

L = ['10', '190', '2', '34', '53']
for n,i in enumerate(L):
    L[n] = L[n].zfill(3)
line = ", ".join(str(x) for x in L)
print line

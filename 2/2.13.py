line = ("""Dlugi napis
Drugi wiersz
No i trzeci
Taki dlugi""")
z = line.split()
dlugosc = 0
for x in z:
    dlugosc = dlugosc + len(x)
print dlugosc

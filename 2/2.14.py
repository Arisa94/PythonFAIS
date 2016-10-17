line = ("""Dlugi napis
Drugi wiersz
No i trzeci
Taki dlugiiiiii""")
z = line.split()
dlugosc = 0
najdluzszy = z[0]
for x in z:
    if len(x) >= dlugosc:
        dlugosc = len(x)
        najdluzszy = x
print najdluzszy
print dlugosc


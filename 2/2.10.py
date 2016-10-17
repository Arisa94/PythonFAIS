line = ("""Przykladowy tekst do policzenia
Drugi wiersz""")
z = line.split('.')
for x in z:
	print "Ilosc wyrazow: ", len(x.split())

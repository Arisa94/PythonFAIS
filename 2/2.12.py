#Pierwsza czesc zadania
line = ("""To jest moj tekst
Drugi wiersz
Trzeci tez
A nawet czwarty!""")
newList = line.split('\n')
temp = [x[0] for x in newList]
word = "".join(str(x) for x in temp)
print word
#Druga czesc zadania
temp = [x[-1] for x in newList]
word = "".join(str(x) for x in temp)
print word

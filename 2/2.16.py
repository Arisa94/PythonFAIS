line = ("Napis GvR Taki dlugi")
z = line.split()
for n,i in enumerate(z):
    if i == "GvR":
        z[n] = "Guido van Rossum"
line = " ".join(str(x) for x in z)
print line

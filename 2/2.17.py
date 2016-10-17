line = ("To jest moj napis a b z c")
z = sorted(line.split(), key=str.lower)
line = " ".join(str(x) for x in z)
print line

z = line.split()
z.sort(key=lambda item: (-len(item), item))
line = " ".join(str(x) for x in z)
print line

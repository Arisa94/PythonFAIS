def doMeASquare(x, y):
    result = ""
    for i in range(y):
        result = result + "+---" * x + "+"
        result = result + "\n" + "|   " * x + "|" +"\n"
    result = result + "+---" * x + "+"
    return result
 
x = input("Podaj szerokosc ")
y = input("Podaj wysokosc ")
result = doMeASquare(x, y)
print result

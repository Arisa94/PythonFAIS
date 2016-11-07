def fillWithSpaces(x):
    numbers = "|...." * x + "| \n0"
    #print numbers
    for i in range(x):
        temp = str(i+1)
        while len(temp) < 5:
            temp = " " + temp
        numbers = numbers + temp
    return numbers
 
x = input("")
 
numbers = fillWithSpaces(x)
 
print numbers

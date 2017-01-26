from random import *
#globalna tablica przechowujaca wynik dzialania algorytmu
result = ""


def knapsack(objects, capacity, currentObject):

    global result

    #jesli dojdziemy do konca elementow nie znajdujac wczesniej rozwiazania zwracamy false
    if currentObject == len(objects):

        return False

    #jesli element zmiesci sie do plecaka
    elif objects[currentObject] < capacity:

        #jesli nie mozemy spakowac plecaka z tym elementem probujemy dalej bez niego
        if not knapsack(objects, capacity - objects[currentObject], currentObject + 1):

            return knapsack(objects, capacity, currentObject + 1)

        else:

            #jesli mozemy dodajemy element do zmiennej globalnej przechowujacej wynik i zwracamy true
            result = str(objects[currentObject]) + ' ' + result
            return True

    #jesli element wypelni plecak dodajemy element do zmiennej globalnej przechowujacej wynik i zwracamy true
    elif objects[currentObject] == capacity:

        result = str(objects[currentObject]) + ' ' + result
        return True

    #jesli nie miesci sie do plecaka probujemy z nastepnym elementem
    else:

        return knapsack(objects, capacity, currentObject + 1)


choice = input("Do you want to add your variables [1], check proposed ones? [2] or get them from file of yours [3]? ")

while not choice == 1 and not choice == 2 and not choice == 3:
    choice = input("Are you sure your answer was correct? Try again! Do you want to add your variables [1], "
                   "check proposed ones? [2] or get them from file of yours [3]? ")

if choice == 1:

    n = input("How many of data sets you want to enter? ")

    while n > 0:

        result = ""
        capacity = input("How big is your knapsack? ")
        amountOfObjects = input("How many objects you want to pack? ")
        objects = []
        j = 0

        while j < amountOfObjects:
            objects.append(input("Add object number " + str(j + 1) + " "))
            j += 1

        if knapsack(objects, capacity, 0):

            print(str(capacity) + " = " + result)

        else:

            print("There is no solution!")

        n -= 1

elif choice == 2:

    result = ""
    capacity = 30
    amountOfObjects = 5
    objects = [10, 10, 9, 5, 5]

    print "For data: Size of knapsack = " + str(capacity) + " and objects " + str(objects)[1:-1]

    if knapsack(objects, capacity, 0):

        print(str(capacity) + " = " + result)

    else:

        print("There is no solution!")

    result = ""
    capacity = 300
    amountOfObjects = 20
    objects = [10, 10, 90, 5, 5, 30, 10, 50, 40, 32, 14, 5, 10, 98, 36, 29, 30, 40, 67, 30]

    print "For data: Size of knapsack = " + str(capacity) + " and objects " + str(objects)[1:-1]

    if knapsack(objects, capacity, 0):

        print(str(capacity) + " = " + result)

    else:

        print("There is no solution!")

    result = ""
    capacity = 38
    amountOfObjects = 5
    objects = [10, 10, 9, 7, 15]

    print "For data: Size of knapsack = " + str(capacity) + " and objects " + str(objects)[1:-1]

    if knapsack(objects, capacity, 0):

        print(str(capacity) + " = " + result)

    else:

        print("There is no solution!")

    result = ""
    capacity = int((random()) * 1000)
    amountOfObjects = capacity - int((random()) * capacity)
    objects = []
    for i in range(0, amountOfObjects):
        objects.append(randint(0, amountOfObjects))

    print "For data: Size of knapsack = " + str(capacity) + " and objects " + str(objects)[1:-1]

    if knapsack(objects, capacity, 0):

        print(str(capacity) + " = " + result)

    else:

        print("There is no solution!")

elif choice == 3:

    fileName = raw_input("What is the name of your file? ")

    file = open(fileName + '.txt', 'r').read()
    lines = file.split('\n')
    i = 0
    n = int(lines[i])
    i += 1

    while n > 0:

        result = ""
        objects = []
        capacity = int(lines[i])
        i += 1
        amountOfObjects = int(lines[i])
        i += 1
        j = 0

        while j < amountOfObjects:
            objects.append(int(lines[i]))
            i += 1
            j += 1

        if knapsack(objects, capacity, 0):

            print(str(capacity) + " = " + result)

        else:

            print("There is no solution!")

        n -= 1

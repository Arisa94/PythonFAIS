from math import *
import random


def randomList(N):

    result = []

    for i in range(0, int((random.random()) * 1000)):
        result.append(random.randint(0, N - 1))

    return result


def almostSorted(N):

    l = list(range(N))
    distance = round(log(N) * 2)

    for i in range(N):

        a = i - distance
        b = i + distance

        if a < 0:
            a = 0

        if b >= N:
            b = N - 1

        r = random.randint(a, b)
        l[i], l[r] = l[r], l[i]

    return l


def reversedAlmostSorted(N):

    result = almostSorted(N)
    result.reverse()
    return result


def gauss(N):

    result = []

    for _ in range(N):
        result.append(round(random.gauss(N / 2, N / 6)))

    return result


def repeatingElements(N):

    result = []

    for _ in range(N):
        result.append(random.randint(0, floor(sqrt(N))))

    return result

print randomList(10)
print almostSorted(10)
print reversedAlmostSorted(10)
print gauss(10)
print repeatingElements(10)
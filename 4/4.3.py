def factorial(n):
    result = 1
    for i in range(n):
        result = result * (i + 1)
    return result
 
n = input("Jaka liczba?")
result = factorial(n)
print result

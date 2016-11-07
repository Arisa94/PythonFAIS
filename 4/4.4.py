def fibonacci(n):
    result = 1
    lastValue1 = 1
    lastValue2 = 1
    for i in range(n):
        if i >= 2:
            result = lastValue1 + lastValue2
            lastValue1 = lastValue2
            lastValue2 = result
    return result
   
n = input("Ktory wyraz ciagu?")
result = fibonacci(n)
print result

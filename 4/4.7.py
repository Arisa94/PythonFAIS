def flatten(sequence):
    result = []
    for i in sequence:
        if(isinstance(i, (list, tuple))):
            result = result + flatten(i)
        else:
            result.append(i)
    return result

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
result = flatten(sequence)
print result

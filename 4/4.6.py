def sum_seq(sequence):
    result = 0
    for i in sequence:
        if(isinstance(i, (list, tuple))):
            result = result + sum_seq(i)
        else:
            result = result + i
    return result
    
sequence = (1, 2, (3, 4, 5), 2, 5)
result = sum_seq(sequence)
print result

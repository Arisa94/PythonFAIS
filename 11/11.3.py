def smaller(number1, number2):

    if number1 < number2:
        return True

    else:
        return False


def selectSort(result, left, right):

    for i in range(left, right):

        k = i

        for j in range(i + 1, right + 1):

            if smaller(result[j], result[k]):
                k = j

        result[i], result[k] = result[k], result[i]

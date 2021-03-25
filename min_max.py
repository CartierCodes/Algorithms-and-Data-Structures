def findMinimum(array):
    if len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]
    return min(array[0], findMinimum(array[1:]))

def findMaximum(array):
    if len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]
    return max(array[0], findMaximum(array[1:]))


testArray = [20, 6, 15, 35, 4]
print(findMinimum(testArray))
print(findMaximum(testArray))
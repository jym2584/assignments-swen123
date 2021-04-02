import arrays

def merge_sort(an_array):
    if len(an_array) == 0:
        return an_array
    if len(an_array) == 1:
            return an_array
    else:
        half1, half2 = split(an_array)
        return merge(merge_sort(half1), merge_sort(half2))


def split(an_array):
    evens = arrays.Array((len (an_array) + 1) // 2) # Rounds up
    odds = arrays.Array(len (an_array) // 2) #Rounds down
    isEven = True
    for i in range(len(an_array)):
        if isEven:
            evens[i // 2] = an_array[i]
        else:
            odds[i // 2] = an_array[i]
        isEven = not isEven
    return evens, odds

def merge(sorted1, sorted2):
    result = arrays.Array(len(sorted1) + len(sorted2))
    i1 = 0
    i2 = 0
    while i1 < len(sorted1) and i2 < len(sorted2):
        if sorted1[i1] <= sorted2[i2]:
            result[i1 + i2] = sorted1[i1]
            i1 = i1 + 1
        else:
            result[i1 + i2] = sorted2[i2]
            i2 = i2 + 1
    
    if i1 < len(sorted1):
        for j in range(i1, len(sorted1)):
            result[j + i2] = sorted1[j]
    elif i2 < len(sorted2):
        for j in range(i2, len(sorted2)):
            result[j + i1] = sorted1[j]
    
    return result

import random

def swapper(a_list): # with slicing, my attempt
    half_length = len(a_list) // 2
    half1 = a_list[0:half_length]
    half2 = a_list[half_length:]
    swapped = half2 + half1
    return swapped

def swapper2(a_list): ## without slicing
    swapped = []
    half = len(a_list) // 2
    for i in range(0, half):
        swapped.append(a_list[i])
    for i in range(half, len(a_list)):
        swapped.append(a_list[i])
    
    return swapped

def swapper3(a_list): ## without slicing
    swapped = []
    half = len(a_list) // 2
    for i in range(0, half):
        swapped.append(a_list[i])
    for i in range(half, len(a_list)):
        swapped.append(a_list[i])
    swapped = a_list[half:] + a_list[:half]
    return swapped

def run_swapper():
    a_list = [1,2,3,4,5,6]
    print(swapper(a_list)) # with slicing

    print(swapper2(list(range(1,11)))) # without slicing
    print(swapper2(list([])))
    print(swapper2(list([1])))
    print(swapper2(list([1,2,3])))
    print(swapper2(list([1,2,3,4,5,6,7,8,9,10])))

    print(swapper3(list(range(1,11)))) # without slicing
    print(swapper3(list([])))
    print(swapper3(list([1])))
    print(swapper3(list([1,2,3])))
    print(swapper3(list([1,2,3,4,5,6,7,8,9,10])))

##################################################################

def chunky(a_list, size):
    for i in range(0, len(a_list), size):
        print(a_list[i:i+size])

def run_chunky():
    a_list = list(range(1,11))
    for i in range(1,11):
        print("\nSize",i)
        chunky(a_list, i)

##################################################################

def sevens_key(num):
    print(str(num)[0])
    if str(num)[0] == '7': # if it starts with a 7
        return 0, num # we want the smallest 7 to be first
    else:
        return 1, num

def lucky_7s(a_list):
    print(a_list)
    a_list.sort(key = sevens_key)
    print(a_list)

def run_lucky_7s():
    a_list = list(range(0,100,7))
    random.shuffle(a_list)
    lucky_7s(a_list)

##################################################################

def list_comprehension():
    print([None for _ in range (5)])
    string = "abcde"
    print([char for char in string])
    print([char.upper() for char in string])

    print([5 for _ in range(100)])
    #print([x//2 for x in data])
    #print([q for q in numbers if q % 2 == 0])

def comprehension():
    string = "foobar"
    print([char for char in string]) # or ([char for char in "foobar"])
    print([0 for i in range(15)])
    print([num for num in range(0,13)])
    print([num for num in range(0,21,2)])
    print([num for num in range(0,51) if num % 5 == 0 or num % 3 == 0])

##################################################################

def make_table(rows, columns, value): # Like rows and columns
    table = []
    for i in range(rows):
        table +=[[value for _ in range(columns)]]
        print(table[i])
    return [[value for _ in range(columns)] for _ in range(rows)]
def main():
    #run_swapper()
    #run_chunky()
    #run_lucky_7s()
    #list_comprehension()
    #comprehension()
    make_table(5,4,0)
    pass

main()
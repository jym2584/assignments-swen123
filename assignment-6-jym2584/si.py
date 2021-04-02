import re
import arrays

def get_file_length(filename):
    length = 0
    with open(filename) as file:
        for line in file:
            length += 1
        return length

def arrays_from_file(filename):
    length = get_file_length(filename)
    file_array = arrays.Array(length)
    count = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()
            file_array[count] = line
            count+= 1
        return file_array

def a_count(file_array):
    length = len(file_array)
    num_a = 0
    for i in range(length):
        word = file_array[i]
        if word[0] == "a" or word[0] == "A":
            num_a += 1
    return num_a

def item_search(file_array, target):
    length = len(file_array)
    for i in range(length):
        if file_array[i] == target:
            return i
    return None

def add_odd(num):
    if num < 0: # Base 
        raise ValueError
    elif num > 100:
        return 0
    else: # Unit of work
        if num% 2 ==1:
            return add_odd(num+1) + num
        else:
            return add_odd(num+1)

#print(add_odd(0))

def bender(string):
    if string <= 0:
        return 1
    else:
        if string % 7 == 0:
            return string * bender(string-1)
        else:
            return bender(string-1)

print(bender(500))

def funcname(self, parameter_list):
    pass
def main():
    print("Odd numbers", add_odd(0))
    #items = arrays_from_file("stockroom.txt")
    #num_a = a_count(items)
    #output = item_search(items, "apricot")
    #if output == None:
    #    print("Apricot was not found")
    #else:
    #    print("Apricot was found")

main()
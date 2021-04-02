import arrays as a
import array_utils as au
import time
import random 
import re

def array_copy(an_array):
    copy = []
    for i in range(len(an_array)):
        copy += [an_array[i]]
    return copy

def list_copy(a_list):
    copy = a.Array(len(a_list))
    for i in range(len(a_list)):
        copy[i] = a_list[i]
    return copy
#############################################################
def random_numbers(max):
    counts = set()
    start = time.perf_counter()
    while len(counts) < max:
        counts.add(random.randint(1,max))
    end = time.perf_counter()
    return end-start

def print_time(num):
    time = random_numbers(num)
    print(num, "took", time,"seconds")
#############################################################
def find_maximum(dictionary):
    max_key = None
    max_value = 0 # or float('-inf')
    for key in dictionary:
        if dictionary[key] > max_value:
            max_key = key 
            max_value = dictionary[key] # Sets max value to the first number, then compares the next number to that first number
    return max_key, max_value

def random_counts(max):
    counts = {}
    while len(counts) < max: # While the length of counts is less than the max numbers
        num = random.randint(1, max)
        if num not in counts:
            counts[num] = 0
        counts[num] = counts[num] + 1 # Adds the key of the value by 1
    return counts

def print_counts(num):
    key, value = find_maximum(random_counts(num))
    print(num, "max count", key, ":", value)
#############################################################
def ascii_codes(a_string):
    for i in a_string:
        print(i,":",ord(i))

def decode(encoded_message):
    message = ""
    split = encoded_message.split()
    for each_int in split:
        message += chr(int(each_int))

def encode(string):
    for i in string:
        print(str(ord(i)), end= " ")
#############################################################
def string_hash(a_string):
    max = 0
    for char in a_string:
        if ord(char) > max:
            max = ord(char)
    return max * len(a_string)

def print_string_hash(string):
    print(string_hash(string))

def collisions(filename, length): # Conflict
    detector = a.Array(length)
    count = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if len(line) > 0:
                hash_code = string_hash(line)
                index = hash_code % length
                if detector[index] != None:
                    return count
                else:
                    detector[index] = line
                    count += 1      
    return count


#############################################################
def collisions_ascii(filename, length): # Conflict
    detector = a.Array(length)
    count = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if len(line) > 0:
                hash_code = ascii_hash(line)
                index = hash_code % length
                if detector[index] != None:
                    return count
                else:
                    detector[index] = line
                    count += 1      
    return count

def ascii_hash(a_string):
    hash_code = 0
    for char in a_string:
        hash_code += ord(char)
    return hash_code

###############################
def collisions_good(filename, length): # Conflict
    detector = a.Array(length)
    count = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if len(line) > 0:
                hash_code = good_hash(line)
                index = hash_code % length
                if detector[index] != None:
                    return count
                else:
                    detector[index] = line
                    count += 1      
    return count

def good_hash(a_string):
    exponent = len(a_string) - 1
    hash_code = 0
    for char in a_string:
        hash_code += ord(char)*31**exponent
        exponent -= 1
    return hash_code
#############################################################

def main():
    #main_copy()
    #main_printtime()
    #main_dictionary()
    #main_ascii()
    main_hash_string()
    print("How many lines before collision using ascii (higher the better):", collisions_ascii("data/alice.txt", 100))
    print("How many lines before collision using good (higher the better):", collisions_good("data/alice.txt", 100))

#############################################################

def main_copy():
    an_array = au.range_array(1,10)
    a_list = [i for i in range(1,11)]
    print(array_copy(an_array))
    print(list_copy(a_list))

def main_printtime():
    print_time(100)
    print_time(1000)
    print_time(100000)

def main_dictionary():
    dictionary = {'a': 50, 'b': 100, 'c': 12}
    key, value = find_maximum(dictionary)
    print(key, value)

    print_counts(100)
    print_counts(1000)
    print_counts(10000)

def main_ascii():
    ascii_codes("Hello")
    decode("66 101 32 115 117 114 101 32 116 111 32 100 114 105 110 107 32 121 111 117 114 32 79 118 97 108 116 105 110 101 46")
    encode("Hello")

def main_hash_string():
    #print_string_hash("hello")
    #print_string_hash("this")
    #print_string_hash("that")
    print("How many lines before collision using hash (higher the better):", collisions("data/alice.txt", 10))

#############################################################

if __name__ == "__main__":
    main()    
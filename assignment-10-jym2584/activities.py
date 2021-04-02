import arrays
import array_utils
import time
import re
def unique_array(an_array, value):
    for i in range(len(an_array)): # O(n) - have to search one to one
        if value == an_array[i]:
            return
        elif an_array[i] == None:
            an_array[i] = value
            return

def fill_array(length):
    an_array = arrays.Array(length)
    begin = time.perf_counter()
    for i in range(length): # O(n) times
        unique_array(an_array, i) # O(n) times
    end = time.perf_counter() 
    return end - begin   # results in n^2

def unique_list(a_list, value):# Time Complexity - O(n)
                             # or              if value not in a_list:
    for item in a_list:                             #a_list.append(value)
        if item == value:
            return
        else:
            a_list.append(value)

def unique_list2(a_list, value): # Alternative
    if value not in a_list:
        a_list.append(value)

def fill_list(length): # Time Complexity - n^2
    a_list = []
    begin = time.perf_counter()
    for i in range(length): # O(n) times
        unique_list(a_list, i) # O(n) times
    end = time.perf_counter() 
    return end - begin   # results in n^2

#   Complexities
# Linear Search - O(n)
# Binary Search - O(log2n)

def main_fill_array():
    delta = fill_array(5000)
    print("It took", delta, "seconds to fill the array")
    
    delta2 = fill_list(5000)
    print("It took", delta2, "seconds to fill the list")
#####################################################################

def set_from_slide():
    a_set = {1,2,3}
    a_set.add(4)
    if 3 in a_set:
        print("3 is in the set")
    else:
        a_set.add(3)

    a_set.add(2)

    for value in a_set:
        print(value)
    
    b_set = set("abcdcba")
    print(b_set)

def sets():
    the_set = {11, 3, 57}
    print("Original", the_set)
    the_set.add(2)
    the_set.add(10)
    the_set.add(100)
    the_set.add(1)
    the_set.add(1)
    print("Adding", the_set)

    set2 = set("abcdefabcdef") # letters change by each run
    print(set2)

def unique_set(a_set, value):
    if value not in a_set:
        a_set.add(value)

def fill_set(length): # Time Complexity - n^2
    a_set = set()
    begin = time.perf_counter()
    for i in range(length): # O(n) times
        unique_set(a_set, i) # O(n) times
    end = time.perf_counter() 
    return end - begin   # results in n^2

def the_sets_main():
    delta2 = fill_list(5000)
    print("It took", delta2, "seconds to fill the list")
    delta3 = fill_set(5000)
    print("It took", delta3, "seconds to fill the set")

#################################################################
def mixup():
    the_set = set("Hello World!")
    #print(the_set)
    for i in the_set:
        print(i, end = "")
    print()

def mixup_main():
    for i in range(3):
        mixup()

def unique_words(filename):
    word_set = set()
    word_set_list = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            tokens = line.split()
            for word in tokens:
                word = word.lower()
                words = re.findall("[\w\']+",word) # breaks up the word in alphanumeric
                for word in words:
                    word_set.add(word)
    return word_set

def main():
    #main_fill_array()
    ####
    #set_from_slide()
    #sets()
    ###########################
    #mixup()
    #the_sets_main()
    #mixup_main()
    words = unique_words("data/alice.txt")
    print("There are", len(words), "words in alice")

main()
import random

def string_hash_bad(a_string):
    '''Bad hash string, should result in the same value regardless of string

    @param max, our hash code
    @return max, returns the hash code
    '''
    max = 0
    for char in a_string:
        max = ord(char)
    return max * 0

def string_hash_inconsistent(a_string):
    '''Bad hash string, should result in the same value regardless of string

    @return max, returns the hash code times the random
    '''
    max = 0
    for char in a_string:
        if ord(char) > max:
            max = ord(char)
    return max * random.randint(0,max)

def string_hash_ascii(a_string):
    ''' Converts a string hash by adding each character to the max
    '''
    max = 0
    for char in a_string:
        max += ord(char)
    return max

def string_hash_better(a_string):
    ''' Converts a string hash by modifying each character so that they have different ascii values
    @param exp, Takes the length of the string to use as an exponent for the equation
    series starting from i=0 to length-1, a_string[i] * 31^exp

    @return max, returns the hash_code from the equation
    '''
    exp = len(a_string) -1
    max = 0
    for char in a_string:
        max += ord(char)*31**exp
        exp -= 1
    return max

def collisions(size, hash_func):
    ''' Calculates the collisions of each hashing function
    @param string, this will be ran with our hashing functions, runs each string from aaa, aab, aac, ---> zzx, zzy, zzz
    @param hash_index, this is where we grab our hash index based on the size and hashcode result from the hash_func
    @param a_list, this is where we make our list to grab our index
    @param total_collisions, used to calculate the collisions (if a string's hash code has the same value as the others from the hash_func)
    @param collision_indexes, Appends 1 every time the value in the list is greater than 1 (meaning there is a collision)
    @param average_collisions, divides total_collisions by collision_indexes

    @return total_collisions, returns the value of the total collision
    @return average_collisions, returns the value of the average collision
    '''
    print("Hashing", size, "with function", hash_func.__name__)
    #hash_code = abs(hash_func("aaa"))
    #print(hash_code)
    string = ""
    hash_index = 0
    a_list = [0 for i in range(size)] # Our table where collisions will be counted
    for i in range(97,123): # From a to z on the first_char
        for j in range(97,123): # From a to z on the second_char
            for k in range(97,123): # From a to z on the third_char
                string_char1 = chr(i) # Converts ascii value into a character
                string_char2 = chr(j)
                string_char3 = chr(k)

                string += string_char1 + string_char2 + string_char3 # Adds each character into a single string

                hash_code = abs(hash_func(string)) # We then take the absolute value of the hash function of the string
                hash_index = int(hash_code % size) # We grab the hash's index by dividing hash_code by size
                a_list[hash_index] += 1 # We add 1 to the index

                string = "" # We set the string back to empty so that we can iterate again to aab, aac, aad, ----> zzx, zzy,zzz

    total_collisions = 0
    collision_indexes = 0
    average_collisions = 0

    for value in a_list: # For each value in the list
        if value >1: # If the value of an index contains 1 or more collision
            total_collisions += value -1 # Add that
            collision_indexes += 1 # Indicate the number of collisions
    
    if collision_indexes > 0:
        average_collisions = total_collisions/ collision_indexes # Calculates the average collisions
    print("Total collisions", total_collisions)
    print("Average collisions", average_collisions)
    return total_collisions, average_collisions

def main(): 
    #a_string = "Helloooo"
    #print("Bad", string_hash_bad(a_string))
    #print("Inconsistent", string_hash_inconsistent(a_string))
    #print("Ascii", string_hash_ascii(a_string))
    #print("Better", string_hash_better(a_string))

    collisions(100000, string_hash_bad)
    collisions(100000, string_hash_inconsistent)
    collisions(100000, string_hash_ascii)
    collisions(100000, string_hash_better)
    collisions(100000, hash)

if __name__ == "__main__":
    main()
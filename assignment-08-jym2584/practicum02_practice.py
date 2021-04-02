
"""
Practice Practicum 02

1. Read a file and place the numbers and characters into their list 
2. Figure out the time complexities for every sorting algorithm you know and write them down,
   then tell your SI which one you should use. Correct answer gets the code.
3. Take the character list and recursively count all vowels

binary and linear search and sorts
"""

# BONUS: Find out what parts you can use TDD for this file 

# Read the file and put the numbers and characters in their own list
# Lol use .isdigit()
def read_file(filename, numbers = [], characters = []):
    with open(filename) as file:
        for line in file:
            stripped = line.strip()
            if stripped.isdigit():
                numbers.append(stripped)
            else:
                characters.append(stripped)
        #print(numbers)
        #print(characters)
    return numbers, characters

# Sort the numbers list from leastest to greatest
# Try to choose the fastest sorting algo you know
def get_sorted(numbers):
    if len(numbers) >1: 
        mid = len(numbers)//2 # Finding the mid of the numbersay 
        L = numbers[:mid] # Dividing the numbersay elements  
        R = numbers[mid:] # into 2 halves 
  
        get_sorted(L) # Sorting the first half 
        get_sorted(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp numbersays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                numbers[k] = L[i] 
                i+= 1
            else: 
                numbers[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            numbers[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            numbers[k] = R[j] 
            j+= 1
            k+= 1
    return numbers

# Count all vowels from the character list
def get_vowels(chars, count = 0):
    if 0 >= len(chars)-1:
        return count
    elif chars[0] == "a":
        return get_vowels(chars, count + 1)
    elif chars[0] == "e":
        return get_vowels(chars, count + 1)
    elif chars[0] == "i":
        return get_vowels(chars, count + 1)
    elif chars[0] == "o":
        return get_vowels(chars, count + 1)
    elif chars[0] == "u":
        return get_vowels(chars, count + 1)
    else:
        return get_vowels(chars, count)

## Si answers
def get_vowels2(chars, num = 0):
    if chars == []:
        return None
    else:
        if chars[0] == "a" or chars[0] == "e" or chars[0] == "i" or chars[0] == "o" or chars[0] == "u":
            return get_vowels(chars[1:], num+1)
        else:
            return get_vowels(chars[1:], num)
# Good luck
def main():
    filename = "file.txt"
    read_file(filename)

    get_numbers, get_characters = read_file(filename)
    #Step 2
    print(get_sorted(get_numbers))

    #Step 3
    print(get_vowels2(get_characters, 10))

if __name__ == "__main__":
    main()
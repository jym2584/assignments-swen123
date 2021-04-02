import turtle as t
import csv

def pig_latin_translator(word):
    '''Translates a word into ze pig latin
    Grabs everything before and after the first vowel and makes it into a word

    EG: smile
    i is our first vowel
    start = sm
    end = le
    translated = first vowel + end + start + "ay"
    = ilesmay

    @param translated, where our end + start + "ay" values will be appended to, or just translated + "ay"
    @param first_vowel, grabs our very first vowel from the word
    @param start, grabs everything before the first vowel
    @param end, grabs everything after the first vowel

    @return translated, returns the pig latin of the word
    '''
    translated = ""
    vowels = "aeiou"

    first_vowel = ""
    start = ""
    end = ""

    if word[0] in vowels:
        translated += word + "ay"
        print("The word is", translated)
        return translated

    for letters in word:
        if letters in vowels:
            first_vowel += letters
            break
        
    for letters in word:
        if letters != first_vowel:
            start += letters
        else:
            break

    for letters in word:
        if letters not in start:
            end += letters

    translated += end + start + "ay"

    print("start =", start)
    print("end =", end)
    print("The word is", translated)
    return translated


def polygon (side_length, sides, color = "green"):
    '''Draws our polygon'''
    if sides < 2:
        raise ValueError("Sides needs to be greater than 2")

    t.fillcolor(color)
    t.begin_fill()
    t.pendown()
    i = 0

    while i < sides:
        t.forward(side_length)
        t.right(360/sides)
        i+=1

    t.penup()
    t.end_fill()

def find_streets(filename, street_name):
    '''Find the streets given a name and file
    @param street_names, appends the streetname if found
    '''
    street_names = ""
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            for record in reader:
                if record[0].lower() == street_name:
                    street_names += record[0] + " "  # Street
                    street_names += record[1] + " " # Street Type
                    street_names += record[2] + "\n" # Post Direction
            print(street_names)
            if street_names.strip() == "":
                print("There are no streets with that name")
    except FileNotFoundError:
        print("File has not been found")

##################################

def count_streets(street_name):
    '''Our helper function for counting the occurrences of a street
    @param count, adds up if a street name is found on the csv file
    @return count, returns the occurreences of a street name
    '''
    count = 0
    with open("data/streets.csv") as file:
        reader = csv.reader(file)
        for record in reader:
            if record[0].lower() == street_name:
                count +=1
    #print("found", street_name, count, "times")
    return count

def find_popular_streets(filename):
    '''Finds the most popular street name given its count
    @address1, iterating through an address and finding that address's occurrences
    @stored_count, where we will store our occurrences of address1

    Time complexity: n^3
    while loop: n
        for loop inside of a while loop: n
            for loop (because of helper function) inside of a for loop: n
    '''
    #stores a address
    #stores the count of the address
    #compare it with another address (and its count)
    # if the occurrence of the address is less than the other address, go to a different address
    address1 = ""
    stored_count = 0

    with open(filename) as file:
        reader = csv.reader(file)
        next(reader) # skips the title of the csv file

        while stored_count != 4:
            for record in reader:
                address1 = record[0].lower() # grabs the first address
                break

            count = count_streets(address1) # count the occurrences of that adddress

            if count > stored_count: # If the address count is greater than the stored
                stored_count = count # Make that stored count the greatest
                next(reader) # Let's go to the next address and iterate again
    
    print("Found", address1, "with the highest occurrences of", stored_count)
    

def main():
    #Step 2
    pig_latin_translator("smile")
    #Step 4
    polygon(100, 5)
    #Step 5
    find_streets("data/streets.csv", "mission bay")
    #Step 6
    count_streets("mission bay")
    find_popular_streets("data/streets.csv")

if __name__ == "__main__":
    main()
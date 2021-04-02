import csv
import arrays
def divisible_3_5(number, a_list = [], index = 1):
    '''Recursion function that returns an iterative list given a number
    @param number, counts up every number if it's divisible by 3 or 5 up to the specified limit
    @param a_list, where we append our number if it is divisible
    @param index, counts up by 1 for base case

    @return a_list, returns a list of numbers divisible by 3 or 5, but not 3 and 5
    '''
    if index > number: # If the index surpasses the defined number
        pass # Don't do anything
    else:
        if index % 3 == 0 or index % 5 == 0 and not index % 3 == 0 and index % 5 == 0: # If the current number is divisible by 3 or 5, but not 3 and 5
            a_list.append(index)
        divisible_3_5(number, a_list, index + 1)
        return a_list

def find_words(filename, letter, number):
    '''Finds a specified number of unique words given a letter
    @param array, our array where we 'append' the words given the size of it
    @return array, returns a list/array of words of the specified limit
    '''
    array = arrays.Array(number)
    with open(filename) as file:
        i = 0
        for line in file:
            line = line.strip().lower().split()
            for word in line:
                    if letter == word[0] and word not in array and i < number:
                        ''' Conditionals:
                        1. If the letter matches the first letter of a word
                        2. If the word is already not in the array (has to be unique)
                        3. We want to make sure that the array doesn't go over our specified limit
                        '''
                        array[i] = word # If the conditionals are met, add that word to the array's slot
                        i += 1 # Our limiter so that i doesn't go over the size
    return array

def calendar_month(weekday, days):
    ''' Creates a calendar based on the defined number of weekday and days
    @param value, our counter value for our days
    @param calendar, a list of weeks
    @arrays
    '''
    value = 0
    calendar = []

    for week in range(0, 5): # For weeks in the month
        create_week = arrays.Array(7, "00") 
        calendar.append(create_week)
        for day in range(weekday, 7): # For days in the week
            value += 1

            if value != days + 1: # If the number of days doesn't surpass our days parameter 
                calendar[week][day] = "{:02}".format(value) # Keep creating the calendar days
            else:
                break # Otherwise, don't create any more days
            weekday = 0 # Resets the weekday loop to 0 

    return calendar

def main():
    #print(divisible_3_5(20))
    #print(find_words("data/atotc.txt", "a", 5))
    
    
    calendar = calendar_month(2, 31)
    for weeks in calendar:
        print(weeks)

if __name__ == "__main__":
    main()
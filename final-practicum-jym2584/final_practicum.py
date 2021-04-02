SHOW_SCORE = True

"""
Q1
Write code to convert words into a version of 'l337-speak' representation,
 which we will call S!mpletext.

Other than the first letter of a word, S!mpletext replaces letter 'a' with '4',
 'e', with '3', and the letter 'i' with '!'. Letters 'o' and 'u' should be
 removed.

Define a function named convert_to_l33t that:
1. declares a string parameter,
2. converts the string parameter to S!mpletext,
3. and returns the converted string

You may not use regular expressions in any way.

Hint: you can't modify strings, but you can add to them.

E.g:
 Linguistic -> L!ng!st!c
 Barrier -> B4rr!3r
 Hooray -> Hr4y
 Exceptional -> Exc3pt!n4l
"""

VOWELS = {'a', 'o', 'u', 'e', 'i'}
s = "Barrier"

def convert_to_l33t(s: str):
    if s == "":
        return s
    elif s == None: # need to change soon
        return None

    try:
        result = s[0] + ""
        s_copy = s[1:]
        for word in s_copy:
            if word == "a":
                result += "4"
            elif word == "e":
                result += "3"
            elif word == "i":
                result += "!"
            elif word == "o" or word == "u":
                pass
            else:
                result += word
    except TypeError:
        return None

    return result

print(convert_to_l33t(s))

"""
Q2
Define a function named most_popular_character that:
1. declares a string parameter, 
2. determines which character occurred most frequently in the string, 
3. and returns the character and its frequency. 
The time compelixty must be O(n).
"""
a_string = 'Hello World'
def most_popular_character(a_string):
    char_dict = dict()
    max_count = 0
    max_ch = ""
    for char in a_string:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
            if char_dict[char] > max_count:
                max_count = char_dict[char]
                max_ch = char
    
    #print(char_dict)
    #print(max_ch, max_count)
    return max_ch, max_count

print(most_popular_character(a_string))
"""
Q3
Interest on an account compounds at 10% per year.  That is, the value of an 
account after 1 year is the initial value + (initial value * 0.1), the value
of an account after 2 years is year 1 value + (year 1 value * 0.1), and so on.

F(0) = initial value
F(N) = F(N-1) + F(N-1) * 0.1

Define a function named compound_interest that:
1. declares parameters for the value of the account (float) and the number of
   years (float),
2. uses recursion to compute the value of the account (float) after the 
   specified number of years has passed,
3. and returns the computed value rounded to the nearest dollar hint: round(return_val,0)
"""

value = 5000
n = 10
#expected = 5500
def compound_interest(value,n):
    '''Rounded to 12969 instead of the expected 12968
    '''
    if n == 0:
        return round(value)
    else:
        value = value * 1.1
        return compound_interest(value, n-1)
    
print(compound_interest(value, n))

"""
Q4 - Part A
Write a function to filter out elements from a list.
This function is *non-destructive*, i.e., returns a new
list based on the parameter list.
The filter is as follows: remove any duplicate integers,
and also remove any elements less than the global minimum integer 
declared below. Think about what data structures you can use to achieve 
this.
Write appropriate comments/docstrings.

Define a non-destructive function named list_filter that:
1. declares a parameter for an input list,
2. creates a copy of the list with any values less than MIN_LIST_FILTER removed
   from the list, and any duplicates removed from the list
3. returns the copy

E.g.

"""

"""
Referencing

        update_score(scores, 4, list_filter,  [21, 211, 30], [21, 211, 21, 5, 3, 1, 1, -2, 30, 30] )
        update_score(scores, 4, list_filter,  [], [5, 3, 1, 1, -2] )
        update_score(scores, 4, list_filter,  None, None )
        update_score_exception(scores, 4, list_filter, AttributeError, [100, 200, 'A' , -1] )
        update_score_exception(scores, 4, list_filter, AttributeError, 999.99 )
"""

MIN_LIST_INTEGER = 21

input_list = [21, 211, 21, 5, 3, 1, 1, -2, 30, 30]
def list_filter(input_list):
    ''' Filters the list by removing duplicates and non-integer types while raising errors if the list can't be iterated
    @param result_temp, where we will append our values that is greater than equal to the MIN_LIST_INTEGER, also given that there is no repeats
                        Preserves the order of the list without using set which does not
    @param result, What result_temp will be replaced with, giving us the list after filtering everything

    @return result, returns the filtered list
    '''
    if input_list == None: # If the input_list is None, return None
        return None

    result_temp = []
    result = []
    try:
        for num in input_list:
            if num >= MIN_LIST_INTEGER and num not in result_temp: # If the number is >= MIN_LIST_INTEGER and given that there is no existing repeats
                result_temp.append(num) # Append the number to the temporary list

        result = result_temp # replace the empty list with our filtered list (result_temp)
        return result
    except: 
        raise AttributeError # Returns AttributeError regardless of the error type

print(list_filter(input_list))
"""
Q4 - Part B 
Add exception handling code in your function above, to handle
unexpected values or types that may be passed in. The function 
should return None when it receives None as the input_list
parameter, and should throw an AttributeError exception in case of
other types.
You may skip if you have already done this.
"""


"""
Q5
A queue can be used to sort a list containing a range of integers from 1-N
where N is the length of the list, e.g. [1, 5, 3, 4, 2].
The list will contain ALL intger values from 1 - N

Define a function that:
1. declares a paramter for a list of integer values in the range 1-N where N
   is the length of the list,
2. counts the total number of times that an integer is removed from the queue
   while sorting the range of integers,
3. and returns the count.

While you may find it useful to do so for testing and debugging, you do not
need to sort the list of integers; you only need to count the total number of 
times that the integers are dequeued from the queue before the sort is 
finished.

ex:
[1,2,3,4,5] -> 5
[1,3,2] -> 4
[2,4,6,8,1,3,5,7] -> 24
"""


from node_queue import *
a_list = [2,4,6,8,1,3,5,7]
def queue_counter(a_list):
    count = 0
    list_queue = Queue()
    for num in a_list:
        list_queue.enqueue(num)
    
    while list_queue.size() is not 0:
        list_queue.dequeue()
        count += 1
    return count

# *********************************************************************
# **************  DO NOT MODIFY ANYTHING BELOW THIS LINE **************
# *********************************************************************

'''
Helper function to run tests and update the score
Pass in:
    scores list (in order to pass the score by reference rather than using a
      global) 
    points for this test
    function being tested
    expected result
    arguments to function under test (this must come last since there are a
      variable number of arguments)
'''
def update_score(scores, pts, func, ex_result, *args):
    test_score = 0
    try:
        if (func(*args) == ex_result): test_score = pts
        else: test_score = 0
    except Exception as e:
        print(e)
    scores[0] += test_score
    scores[1] += 1
    print('Score for',func.__name__,'test', scores[1],'=', test_score, 'Total score =', scores[0])

'''
Helper function to run tests and update the score
Pass in:
    scores list (in order to pass the score by reference rather than using a
      global) 
    points for this test
    function being tested
    expected exception type
    arguments to function under test (this must come last since there are a
      variable number of arguments)
'''
def update_score_exception(scores, pts, func, exception_type, *args):
    test_score = 0
    try:
        func(*args)
        print("Expecting exception",exception_type,"to be thrown")
    except exception_type:
        test_score = pts
    except Exception as e:
        print("Expecting", exception_type, "got", type(e))

    scores[0] += test_score
    scores[1] += 1
    print('Score for',func.__name__,'test', scores[1],'=', test_score, 'Total score =', scores[0])

def main():
    scores = [0,0]

    if SHOW_SCORE:
        # convert_to_l33t tests
        scores[1] = 0
        update_score(scores, 4, convert_to_l33t,  'L!ng!st!c', 'Linguistic' )
        update_score(scores, 4, convert_to_l33t,  'B4rr!3r', 'Barrier' )
        update_score(scores, 4, convert_to_l33t,  '', '' )
        update_score(scores, 4, convert_to_l33t,  None, 3 )
        update_score(scores, 4, convert_to_l33t,  None, None )

        # most_popular_character tests
        scores[1] = 0
        update_score(scores, 5, most_popular_character,  ('', 0), '' )
        update_score(scores, 5, most_popular_character,  ('l', 3), 'Hello World' )
        update_score(scores, 5, most_popular_character,  ('A', 3), 'aaAAA' )
        update_score(scores, 5, most_popular_character,  ('b', 2), 'bb' )

        # compound_interest tests
        scores[1] = 0
        update_score(scores, 5, compound_interest,  5000, 5000, 0 )
        update_score(scores, 5, compound_interest,  5500, 5000, 1 )
        update_score(scores, 5, compound_interest,  12968, 5000, 10 )
        update_score(scores, 5, compound_interest,  0, 0, 5 )

        # list_filter tests
        scores[1] = 0
        update_score(scores, 4, list_filter,  [21, 211, 30], [21, 211, 21, 5, 3, 1, 1, -2, 30, 30] )
        update_score(scores, 4, list_filter,  [], [5, 3, 1, 1, -2] )
        update_score(scores, 4, list_filter,  None, None )
        update_score_exception(scores, 4, list_filter, AttributeError, [100, 200, 'A' , -1] )
        update_score_exception(scores, 4, list_filter, AttributeError, 999.99 )

        # queue_counter tests
        scores[1] = 0
        update_score(scores, 5, queue_counter,  5, [1,2,3,4,5] )
        update_score(scores, 5, queue_counter,  15, [5,4,3,2,1] )
        update_score(scores, 5, queue_counter,  24, [2,4,6,8,1,3,5,7] )
        update_score(scores, 5, queue_counter,  0, [] )

        # Show total score
        print('')
        print("Your Total Score is:",scores[0])

if __name__ == "__main__":
    main()

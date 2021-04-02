import arrays
import array_utils as a
import math
import turtle
def making_array():
    #array = arrays.Array(20)
    #array[4] = 0
    #array[9] = ""
    #array[19] = False

    #print(array)
    size5 = arrays.Array(5)
    size1 = arrays.Array(1,0)
    size10 = arrays.Array(10, "")
    size20 = arrays.Array(20, False)
    print(size5)
    print(size1)
    print(size10)
    print(size20)

def while_fill(an_array):
    #Fill the array with the value of its index
    #Using a while loop
    count = 0
    #an_array = arrays.Array(len(an_array)) # Incorrect
    while count < len(an_array):
        an_array[count] = count
        count += 1

def for_fill(an_array):
    for i in range(len(an_array)):
        an_array[i] = i

def string_fill(string):
    string == "New string"

#6.2
def print_odds(an_array):
    #print all the odd values in the array
    for i in range(0, len(an_array)):
        if an_array[i] % 2:
            print(an_array[i], end=" ")
    '''
    for element in an_array: # or range(len(an_array))
        if element % 2:
            print(element, end=" ")
    '''
def print_odds_rec(an_array, index=0):
    if index >= len(an_array):
        pass
    else:
        if an_array[index] % 2:
            print(an_array[index], end =" ")
        #if index < 99:
        print_odds_rec(an_array,index+1)

def countdown(number):
    if number < 0:
        raise ValueError ("Must use a number of 0 or greater")
    print(number)
    if number == 0:
        return 0
    else:
        sum = number + countdown(number - 1)
        return sum

def factorial(num):
    if num < 0:
        raise ValueError ("Number has to be greater than 0")
    print(num)
    if num == 0 or num == 1:
        return 1
    else:
        #sum = num * factorial(num-1)
        #return sum

        # or
        return num * factorial(num-1)

def circles(radius, depth):
    if depth == 0:
        return 0
    if depth == 1:
        turtle.circle(radius)
        return 2 * math.pi* radius
    turtle.circle(radius,90)
    sum = circles(radius/2,depth - 1)
    turtle.circle(radius,90)
    sum += circles(radius/2,depth - 1)
    turtle.circle(radius,90)
    sum += circles(radius/2,depth - 1)
    turtle.circle(radius,90)
    sum += circles(radius/2,depth - 1)
    
    sum += 2*math.pi*radius
    return sum

def count_up(num, counter = 0):
    if counter > num:
        pass
    else:
        print(counter)
        count_up(num, counter + 1)

def main():
    print(count_up(10))
    #an_array = a.range_array(0,100)
    #print_odds(an_array)
    #print_odds_rec(an_array)
    #print("Sum =", countdown(10))
    #print("Factorial = ", factorial(100))
    #turtle.speed(0)
    #print("Sum=", circles(150,6))
    #turtle.done()

'''
Activity 6.3.5:
target = 79
    iteration = 0   1   2   3
    start       0   8   12  12
    end         16  16  16  14
    mid         8   12  14  13
    value       39  77  83  79
Lecture Actual:
    iteration = 0   1   2   3
    start       0   9   13  13
    end         16  16  16  13
    mid         8   12  14  13
    value       39  77  83  79

target = 11
    iteration = 0   1   2   3   4
    start       0   0   0  0    2
    end         16  7  3   2    2
    mid         8   4  2   1    2
    value       39  21  12 10   10




    #string = "Old string"
    #string_fill(string)
    #print(string)

    #an_array = arrays.Array(10)
    #print(an_array)
    #print("While Fill")
    #while_fill(an_array)
    #print("For Fill")
    #for_fill(an_array)
    #print(an_array)
    

main()
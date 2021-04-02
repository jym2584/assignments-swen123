'''Prints fibonacci sequence in 2 ways
'''
import time
import plotter

def fibonacci_naive(n):
    ''' Prints the fibonacci sequence via recursion
    '''
    if n < 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    value = fibonacci_naive(n-1) + fibonacci_naive(n-2)
    #print(value, end = " ")
    return value

def naive_timer(n):
    ''' Timer for calculating fibonacci_naive sequence
    '''
    begin = time.perf_counter()
    fibonacci_naive(n)
    end = time.perf_counter()
    elapsed = end - begin
    #print("Time elapsed:", elapsed)
    return elapsed

def naive_plot(n):
    ''' Utilizes naive_timer to plot fibonacci_naive
    '''
    plotter.init("Fibonacci Compute Time", "n", "Time")
    for i in range(0,n):
        plotter.add_data_point(naive_timer(i)) #Prints class average using get_average function
    plotter.plot()

#fibonacci_array = {}  #dictionary
#def fibonacci_fast(n, fn_minus_1 = 1, fn_minus_2 = 2):
    '''From  https://codereview.stackexchange.com/a/165060
    '''
#    if n in fibonacci_array:
#        return fibonacci_array[n]
#    if n < 0:
#        raise ValueError ("N must be greater than 0")
#    if n == 1:
#        return 0
#    if n == 2:
#        return 1

#    fn_minus_1 = fibonacci_fast(n-1)
#    fn_minus_2 = fibonacci_fast(n-2)

#    fibonacci_array[n] = fn_minus_1 + fn_minus_2
#    return fn_minus_1 + fn_minus_2

def fibonacci_fast(n, fn_minus_1 = 1, fn_minus_2 = 0):
    ''' Prints the fibonacci sequence via recursion
    Algorithm from: https://www.codegrepper.com/code-examples/python/fibonacci+series+in+python

    returns 0 if n is less than 0
    returns fn_minus_2 if n is 1
    '''
    if n < 0:
        return 0
    if n == 1:
        return fn_minus_2

    value = fibonacci_fast(n-1, fn_minus_2, fn_minus_1 + fn_minus_2)
    return value


def fast_timer(n):
    ''' Timer for calculating fibonacci_fast sequence
    '''
    begin = time.perf_counter()
    fibonacci_fast(n)
    end = time.perf_counter()
    elapsed = end - begin
    #print("Time elapsed:", elapsed)
    return elapsed

def fast_plot(n):
    ''' Utilizes fast_timer to plot fibonacci_fast
    '''
    plotter.init("Fibonacci Fast Compute Time", "n", "Time")
    for i in range(0,n):
        plotter.add_data_point(fast_timer(i)) #Prints class average using get_average function
    plotter.plot()


    #fn_minus_1 = fibonacci_fast(n-1)
    #fn_minus_2 = fibonacci_fast(n-2)
    #value = fn_minus_1 + fn_minus_2
    #return value, fn_minus_1, fn_minus_2

def add_up(n, total=0):
    if n <= 0:
        return total
    else:
        #print(n)
        print(total)
        result = add_up(n-1, total+n)
        #print(result)
    return result

def fast_and_time_plot(n):
    ''' Utilizes fast_timer and naive_timer to plot both fibonacci_fast and fibonacci_naive
    '''
    plotter.init("Fibonacci and Fibonacci Fast Compute Time", "n", "Time")

    for i in range(0,n):
        plotter.add_data_point(naive_timer(i))
    plotter.new_series()
    for i in range(0,n):
        plotter.add_data_point(fast_timer(i))
    plotter.plot()

def main():
    ''' Inputs
    '''
    print(fibonacci_naive(10))
    value_n = int(input("Enter a value for n (fibonacci)"))
    naive_plot(value_n)

    value_n2 = int(input("Enter a value for n (fibonacci fast)"))
    fast_plot(value_n2)

    value_n3 = int(input("Enter a value for n (fibonacci and fib fast plot)"))
    fast_and_time_plot(value_n3)
    input("Enter any key to quit...")
    
    #naive_timer(30)
    #fast_plot(75)
    #print("Fibonacci fast", fibonacci_fast(100))
    #print("finbonacci", fibonacci_naive(10))

if __name__ == "__main__":
    main()
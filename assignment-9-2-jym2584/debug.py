def sum (a_list):
    sum = 0
    for i in range(len(a_list)):
        sum = sum + a_list[i]
    return sum

def fib (num, prev2, prev1):
    if num == 0:
        return prev2
    elif num == 1:
        return prev1
    else:
        return fib (num - 1, prev1, prev1 + prev2)

def main ():
    a_list = [5, 10, 15, 20, 25]
    list_sum = sum (a_list)
    print ('Sum (', a_list, ')=', list_sum)

    num = 5
    fib_of_num = fib (num, 0, 1)
    print ('The ', num, 'th Fibonacci number is ', fib_of_num, sep = '')

if __name__ == "__main__":
    main ()
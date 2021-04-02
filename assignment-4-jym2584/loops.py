def countdown(number):
    sum = 0
    while number >= 0:
        sum = sum + number
        print(number)
        number = number - 1
    return sum

def count_up(number):
    counter = 0
    sum = 0
    while counter <= number:
        sum += counter
        print(counter)
        counter += 1
    return sum

def print_range (a_range):
    # for i in range
    for each_number in a_range:
        print(each_number)

def print_reverse(string):
    for i in range(len(string) - 1,-1,-1):
        print(string[i], sep="", end="")
    print()

def natural_num():
	for i in range(0,100):
	    print(i)
def negative_num():
	for i in range(-1,-100, -1):
		print(i)

def main():
    #natural_num()
    negative_num()
    #a_range = range(0,10)
    #print_range(a_range)
    print_reverse("Hello, World!")


    #print ("Sum =", countdown(5))
    #print("Sum =", count_up(4))
main()
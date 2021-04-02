def count_da_numbas():

    sum = 0
    counter_int = 0
    counter = 0
    try:
        filename = input("Whats your file: ")
        with open(filename) as file:
            for line in file:
                try:
                    numbers = int(line.strip())
                    sum += numbers
                    counter_int += 1
                    result = sum
                    result3 = counter_int
                except ValueError:
                    #print("Not a character")
                    counter += 1
                    result2 = counter
        print("\nCharacters that are an integer",counter_int)
        print("Characters that are not an integer",result2,"\n")
        print("Sum of all valid integers", sum)
    except FileNotFoundError:
        print("Invalid file")

count_da_numbas()

from testing import *

def sum_of_num():
    total = 0
    while True:
        filename = input("Whats the file ")
        try:
            if filename == "":
                break
            with open("data/numbers_"+filename+".txt") as file:
                sum = 0
                for line in file:
                    try:
                        sum += int(line.strip())
                        print("sum for ", filename, ": ",sum, sep="")
                    except ValueError:
                        print("Skipping non-numerc data", line.strip())

                print("Sum for data/numbers_",filename,".txt = ", sum, sep="")
                total += sum
        except ValueError:
            print("File contains non-numeric data")
        except FileNotFoundError:
            print("File does not exist")
        except:
            print("Not sure what you did bro")
    print("Sum of all files =",total)

def x_plus_y():
    try:
        x= int(input("Enter x:"))
        y= int(input("enter Y: ")) 
        print("x + y =", (x + y))
    except ValueError:
        print("Invalid number entered")
    except ArithmeticError:
        print("Arithmetic Error")

def division():
    sum = 0
    attempt = 3
    while True:
        if attempt != 0:
            try:
                num = input("Enter a numerator: ")
                if num == "":
                    break
                den = input("Enter a denominator:")
                if den == "":
                    break

                result = int(num) / int(den)
                sum += result
                print(result)
                attempt = 3

            except ValueError as ve:
                print("Non-numeric value entered")
                attempt -= 1
                if attempt <= 0:
                    raise ve
                print("Tries remaining ", attempt)

            except ArithmeticError as ae:
                print("Arithmetic error: Divide by zero")
                attempt -= 1
                if attempt <= 0:
                    raise ae
                print("Tries remaining ", attempt)

        else:
            print("Quitting program")
            quit()

    print(sum)

def guessing_game():
    number = input("pick a number")
    number = int(number)
    if number < 1 or number > 10:
        raise ValueError("Invalid Guess")
    print("You picked:", number)

def password():
    password = input("Enter a password: ")
    if len(password) < 10 or len(password) > 20:
        raise ValueError ("Password must be 10 to 20 characters")
    
    repeat = input("Re-enter the password")
    if repeat != password:
        raise ValueError("Passwords do not match)")
    
    return password

def login():
    attempts = 4
    while True:
        userid = input("Enter userid ")
        password = input("enter password: ")
        
        try:
            validate(userid, password)
        except ValueError as ve:
            attempts -= 1
            if attempts > 0:
                print("Invalid", attempts, "Attempts remaining")
            else:
                raise ve
def validate(userid,password):
    expected = "username"
    expected2 = "password"
    if userid == expected or password == expected2:
        print("Passed!")
    else:
        print("Not passed")

# TDD Test
def exponent(base, power):
    if power < 0:
        raise ValueError("Exponent is negative")
    return base ** power


#division()
#sum_of_num()
#x_plus_y()
#password()
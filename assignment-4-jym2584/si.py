def evennums():
    counter = 0
    while counter <= 100:
        print(counter)
        counter += 2

def thirdnum():
    counter = 0
    while counter <= 50:
        print(counter)
        counter += 3

def multiple6num():
    counter = 0
    while counter <= 100:
        print(counter)
        counter += 6

def vowels (str):
    print("hello test")
    string = str
    length = len(str)
    print(length)
    count = 0
    counter = 0

    while count < length:
        if string[count] == "a":
            counter += 1
        count +=1
    print("A vowels", counter)
        

def main():
    #multiple6num()
    vowels("Dksajfdkfkjslahfjdnfjasfnasdjlfndjkfdsfsjkfnaldfsjnfak")

main()
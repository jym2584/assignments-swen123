def bday_message ():
    name = input("what's your name?: ")
    birth_month = input("Hey, what's your birth month?: ")
    birth_day = input ("What's your birth date?: ")
    birth_year = input ("what's your bitrth year?: ")
    print (name, ", your birthday is: ", birth_month, " ", birth_day,", ", birth_year,"!", sep="")

bday_message()
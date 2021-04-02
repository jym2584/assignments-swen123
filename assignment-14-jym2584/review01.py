import math
import turtle as t
import csv

#Unit 1
#    a
#    E:\Users\Optimus\primes.txt
#    E:\Users\Optimus\hello.py
#    E:\Users\Program Files\Python\python.exe
#    E:\Users\Program Files\Git\git-bash.exe
#
#    b. cd Users\Optimus
#    c. cd ..
#    d. ls 'E:\Program Files'
#    e. notepad info.txt
#    f. rm hello.py
#########################
''' Git Workflow
a. git status
b. git add names.txt (Adding everything 'git add .')
c. git commit -m "Text"
git push
git pull

git log > log.txt
'''

# Unit 2
def deets():
    print("Jin")
    print("Brooklyn")
    print("SWEN 123 - 4")
    print("MATH 182 - 4")
    print("YOPS 10 - 0")
    print("UWRT 150 - 3")
    print("SWEN 101 - 1")
    print("MATH 190 - 3")

def mathematics():
    x = float(input("Enter an x: "))
    y = float(input("Enter a y: "))
    print ("x^y =", x**y)
    print("y^x =", y**x)
    print("Area of Circle =", 3.14*((x+y)/2)**2) 
    print("Area of triangle =", (x*y)/2)

def circle(radius):
    radius = float(radius)
    print("radius =", radius)
    print("diameter =", radius * 2)
    print("circumference =", 2*3.14*radius)
    print("area =", 3.14*radius**2)
    print("volume =", (4/3)*3.14*radius**3)

def distance(x, y , xx, yy):
    return ((xx - x)*2 + (yy - y)*2)*(1/2)

def triangle(x1, y1, x2, y2, x3, y3, color = "blue"):
    dist = 0
    t.speed(5)
    t.penup()
    t.setpos(x1, y1)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    t.setpos(x2,y2)
    dist = distance(x1, y1, x2, y2)
    t.setpos(x3, y3)
    dist += distance(x2, y2, x3, y3)
    t.setpos(x1,y1)
    dist += distance(x3, y3, x1, y1)
    t.end_fill()
    t.penup()

    return dist

def chop_chop(a_string):
    evens = ''
    odds = ''
    count = 0
    while count < len(a_string):
        if count % 2 == 0:
            evens += a_string[count]
        else:
            odds += a_string[count]
        count += 1
    
    string = evens + odds
    return string

def unchop(a_string):
    unchopped = ''
    first_odd = len(a_string) - len(a_string) // 2
    for i in range(len(a_string) // 2):
        unchopped += a_string[i] + a_string[i + first_odd]
    if len(unchopped) < len (a_string):
        unchopped += a_string[len(a_string) // 2]
    
    print(unchopped)
    return unchopped

def starts_with(filename, letter):
    count = 0
    letter = str.lower(letter)
    with open(filename) as file:
        for line in file:
            line = line.strip().lower()
            words = line.split()
            for word in words:
                if word[0] == letter.lower():
                    count += 1

    print("counted", count, "letters with",letter)

def zip_lookup(filename):
    try:
        zipcode = input("Enter a zipcode: ")
        with open(filename) as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                if line[0] == zipcode:
                    return line[1]
        raise ValueError("Not a valid zipcode")
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Invalid zipcode")

def main():
    #deets()
    #mathematics()
    #circle(5)
    string = chop_chop("Making Sausage")
    unchop(string)
    starts_with("data/atotc.txt", "A")
    print(zip_lookup("data/zip_codes.csv"))

if __name__ == "__main__":
    main()
'''Inputs for gathering student data
@author: Jin Moon


What doesn't work
stu data/grades_010.csv Notareal Student
'''
import plotter
import plots
import csv
import re

def quit():
    '''THis is the main function that gathers various input from the uiser
    quit - quits
    help - help menu
    stu <filename> <first name> <last name>
    avg <filename> <grade item>
    cavg <filename>
    '''
    no_quit = 1
    print("Enter a command or type 'quit' to quit. Type 'help' for help.")
    while no_quit == 1:
        command = input(">> ")
        command = command.split(" ")

        if command[0] == "":
            print("Enter a command or type 'quit' to quit. Type 'help' for help.")
        
        if command[0] == "quit":
            quit = input("Are you sure? Type Y to quit, type any other key to go back.")
            if quit == "y" or quit == "Y":
                print("Quitting program")
                no_quit = 0
            else:
                no_quit = 1
        
        if command[0] == "help":
            print("stu <filename> <first name> <last name> - plot student grades")
            print("cvag <filename> - plot class average")
            print("avg <filename> <number> - prints the average for the grade item")
            print("quit - quits")
            print("help - displays this message")
        try:
            if command[0] == "stu":
                filename = command[1]
                first = command[2]
                last = command[3]
                plot_grades(filename,first,last)
        except IndexError:
            print("Index error for stu. Did you enter in enough arguments? \n   Usage: stu <filename> <first name> <last name>")
        except TypeError:
            print("Not a valid name")

        try:
            if command[0] == "avg":
                filename = command[1]
                grade_item = int(command[2])
                get_average(filename,grade_item)
        except IndexError:
            print("Index error for avg. Did you enter in enough arguments? \n   Usage: avg <filename> <grade item>")
        except ValueError:
            print("Grade item must be a number")
        
        try:
            if command[0] == "cavg":
                filename = command[1]
                first = command[2]
                last = command[3]
                lab_average(filename, first, last)
        except IndexError:
            print("Index error for cavg. Did you enter in enough arguments? \n   Usage: cavg <filename>")
                


def plot_grades(filename, first, last):
    ''' Gathers student average and plots them
    '''
    regex = last + ".*" + first
    sum = 0
    count = 0
    try:
        with open(filename) as file:
            next(file)
            reader = csv.reader(file)
            for record in reader:
                if re.findall(regex, record[0]): # Rows 1 and 2 containg last and first
                    record_count = len(record)
                    plotter.init("Grades for "+ record[0] + " from " + filename, "Grade Item", "Score")

                    for i in range(3, record_count): #From columns 4 to however many columns there are
                        print(record[i])
                        sum += float(record[i])
                        count += 1
                        plotter.add_data_point(float(record[i])) #Let's plot these grades!
                    
                    plotter.plot()
                    print("Plot finished (window may be hidden)")
                    print(record[0],"grade average", sum/count)
                    return True
        print("The student is invalid")
        return False
    except FileNotFoundError:
        print("File",filename,"does not exist")
    except ValueError:
        print("Name not found")



def get_average(filename,grade_item):
    ''' Gathers average of a grade item
    '''
    try:
        with open(filename) as file:
            next(file)
            reader = csv.reader(file)
            count = 0
            sum = 0
            for record in reader:
                #record_count = len(record)
                #plotter.init("Class Averages from " + filename, "Grade Item", "Score")
                #print(record[grade_item])
                #for i in range(3,record_count):
                if record[grade_item] == "": #If the grade in a specific column does not have a value in the cell, then
                    count += 1 # Then we add 1 to the count, technically treating it as a zero! Having a lot of trouble inputting zero... did return 0, grades[column] == 0, and other stuff that I forgot
                else:
                    count += 1
                    sum += float(record[grade_item])
                    average = sum/count
               # plotter.add_data_point(float(record[grade_item])) #Let's plot these grades!
                #plotter.plot()
        print("The entire class average is",average)
        return average
    except FileNotFoundError:
        print("File",filename,"does not exist")

def lab_average(filename,first,last):
    '''Plots lab average of a student
    '''
    regex = last + ".*" + first
    sum = 0
    count = 0

    try:
        with open(filename) as file:
            next(file)
            reader = csv.reader(file)
            
            for record in reader:
                if re.findall(regex, record[0]): # Rows 1 and 2 containg last and first
                    init_name = record[0]
                    #record_count = len(record)
                    
                    for i in range(3, 13): #From columns 4 to however many columns there are
                        sum += float(record[i])
                        count += 1

            average = sum/count
            print("Average for", init_name,":", average)
            return average
        print("The student is invalid")
        return None
    except FileNotFoundError:
        print("File",filename,"does not exist")

    except ValueError:
        print("Name not found")

    except ZeroDivisionError:
        print("Student not found")
        return None

def plot_class_averages(filename):
    ''' Plots the class average using get_average() from i = rows 3 to 29
    '''
    plotter.init("Average grade from " + filename, "Grade Item", "Score")
    for i in range(3,29): #Grabs columns from 3 to 18
        average = get_average(filename, i) #Uses get_average function from line 110
        plotter.add_data_point(float(round(average))) #Prints class average using get_average function
    print("Successfully plotted",filename)
    plotter.plot()

################################################################
# Unused test code
################################################################
def lab_average2(filename):
    ''' Plots the class average using get_average()
    '''
    #regex = last + ".*" + first
    try:
        total = 0
        plotter.init("Average grade from " + filename, "Grade Item", "Score")
        for i in range(2,18): #Grabs columns from 3 to 18
            average = get_average22222(filename, i)
            total += average
            plotter.add_data_point(float(round(average))) #Prints class average using get_average function
        plotter.plot()
        print("Plot is finished (window may be hidden)")
        print("The total average of a lab is", total/i)
        return total
    except FileNotFoundError:
        print("File",filename,"does not exist")

def get_average22222(filename, column):
    with open(filename) as file:
        next(file)
        reader = csv.reader(file)
        count = 0
        sum = 0
        for record in reader:
            if record[column] == "": #If the grade in a specific column does not have a value in the cell, then
                count += 1 # Then we add 1 to the count, technically treating it as a zero! Having a lot of trouble inputting zero... did return 0, grades[column] == 0, and other stuff that I forgot
            else:
                #print(grades[column])
                count += 1
                sum += float(record[column])
                average = sum/count
    #print(header[column], "has an average of",average)
    return average
################################################################

def main():
    plot_grades("data/full_grades_010.csv", "Sion", "Lobasso")
    
    #Step 6
    get_average("data/full_grades_010.csv", 8)
    get_average("data/full_grades_999.csv", 8)
    plot_class_averages("data/full_grades_010.csv")
    plot_class_averages("data/full_grades_999.csv")
    #lab_average("data/full_grades_010.csv", "Sion", "Lobasso")
    #lab_average2("data/grades_010.csv")
    #quit()

if __name__ == "__main__":
    main() 
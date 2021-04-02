""" This plots student grades from .csv
@author: Jin Moon
"""
import plotter

def lab_average(filename, first, last):
    '''Grabs the lab average for the person
    '''
    with open(filename) as file: # Uses filename as file, closes file after
        for line in file: # For each line in the file
            fields = line.strip().split(",") # Seperate every cell using commas
            if fields[0] == last and fields[1] == first: # Rows 1 and 2 containg last and first
                #print(fields[0])
                #print(fields[1])
                sum = 0
                for i in range(8): #Grabs fields from rows 0 to 9
                    #print(fields[i+2])
                    sum+= float(fields[i+2]) # We start at 2 to avoid adding Last and First name as fields. i starts from 0 to 7 + 2 which starts from Lab 1 to Lab 8
                average = sum/8 # Adding the sum of 8 fields and divides that by 8
                print("The lab average for ", first, " ", last, " is: ", round(average,3), sep="") # Prints average
                return average # Returns average for test function
    print(first, " ", last, " is not a valid name.", sep="")
    return None

def get_average(filename, column):
    with open(filename) as file:
        header = next(file).strip().split(",") # Split
        count = 0
        sum = 0
        for line in file: #for each line in the file
            grades = line.strip().split(",")
            if grades[column] == "": #If the grade in a specific column does not have a value in the cell, then
                count += 1 # Then we add 1 to the count, technically treating it as a zero! Having a lot of trouble inputting zero... did return 0, grades[column] == 0, and other stuff that I forgot
            else:
                #print(grades[column])
                count += 1
                sum += float(grades[column])
                average = sum/count
    #print(header[column], "has an average of",average)
    return average

def plot_grades(filename, first, last):
    '''Plotting a student's grade
    '''
    with open(filename) as file:
        for line in file: # For every line in the file
            fields = line.strip().split(",") # Let's split them into commas

            if fields[0] == last and fields[1] == first: # If the first and last name are valid
                field_count = len(fields) #Then let's grab columns
                plotter.init("Grades for "+ first + " " + last + " from " + filename, "Grade Item", "Score")

                for i in range(2, field_count): #From columns 3 to 18
                    plotter.add_data_point(float(fields[i])) #Let's plot these grades!

                plotter.plot()
                print("Successfully plotted student,", first, last,"!")
                return True
    print("The student is invalid")
    return False

def plot_class_averages(filename):
    ''' Plots the class average using get_average()
    '''
    plotter.init("Average grade from " + filename, "Grade Item", "Score")
    for i in range(2,18): #Grabs columns from 3 to 18
        average = get_average(filename, i)
        plotter.add_data_point(float(round(average))) #Prints class average using get_average function
    print("Successfully plotted",filename)
    plotter.plot()

def plot_compare_grade_to_average(filename, filename1, filename2, first, last):
    '''This uses arguments to call plot_grades and plot_class_avaerages
    '''
    plot_grades(filename, first, last)
    plot_class_averages(filename1)
    plot_class_averages(filename2)
        
def input_plot_compare_grade_to_average():
    '''We then utilize plot_compare_Grade_to_average() arguments into inputs!
    '''
    first,last,filename = input("What student and filename do you want the grades of?\n   Arguments: first last filename ('data/' is already inputted for filename)\n> Enter the values: ").split(" ")
    print("   Gathered input for ", first, " ", last, "and filename ", filename, sep="")
    filename1, filename2 = input("What are 2 class averages do you want to compare?\n   Arguments: filename filename2 ('data/' is already inputted for filename)\n > Enter the values: ").split(" ")
    print("   Gathered filename inputs for ", filename1, " and ", filename2, sep="")
    plot_compare_grade_to_average("data/"+filename, "data/"+filename1, "data/"+filename2, first, last)
    
def main():
    #lab_average("data/grades_010.csv", "Sion", "Lobasso")
    #get_average("data/grades_010.csv", 7)
    #get_average("data/grades_010.csv", 4)
    #plot_grades("data/grades_010.csv", "Sion", "Lobasso")
    #plot_class_averages("data/grades_010.csv")
    input_plot_compare_grade_to_average()
    input("Press enter to continue..")

if __name__ == "__main__":
    main() 
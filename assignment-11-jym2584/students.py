class Student:
    #id = "None"
    #name = "student"
    #credits = 0
    #gpa = 0.0
    #email = ['abc123@rit.edu'] #everyone would have the same reference, bad
    __slots__ = ['id', 'name', 'credits', 'gpa', 'email']

    def __init__ (self, id, name): # Prefer to write classes this way
        self.id = id
        self.name = name
        self.credits = 0
        self.gpa = 0.0
        self.email = [] #create our own list specific to the instance
                        #everyone will get their own list

def print_student(student):
    print("**Student**")
    print("id  |   name   |  credits | gpa   |  email")
    print("------------------------------------------------")
    print (student.id, ",", student.name, ",", student.credits, ",", student.gpa, ",", student.email)
    print()

def main():
    student1 = Student("1d", "John Doe") # Instance Attribute
    student1.credits = 10
    student1.email += ['f123@rit.edu']

    student2 = Student("2c", "Jane Derrick") # Instance Attribute
    student2.email += ['c123@rit.edu']

    Student.address = "Home" # does not print because this only applies to static attribute, not instance

    print_student(student1)
    print_student(student2)

main()
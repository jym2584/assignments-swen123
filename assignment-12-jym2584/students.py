"""
A Student class.

@author GCCIS Faculty
"""

__GRADES = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F", "NG"]

__GRADE_WEIGHT = {
    __GRADES[0]: 4.0,
    __GRADES[1]: 3.67,
    __GRADES[2]: 3.33,
    __GRADES[3]: 3.0,
    __GRADES[4]: 2.67,
    __GRADES[5]: 2.33,
    __GRADES[6]: 2.0,
    __GRADES[7]: 1.67,
    __GRADES[8]: 1.0,
    __GRADES[9]: 0,
    __GRADES[10]: 0 # no grade
}

class Course:
    __slots__ = ["__name", "__credits", "__grade"]
    
    def __init__ (self, name, credits):
        self.__name = name
        self.__credits = credits
        self.__grade = None

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        return self.__grade == grade

    def print(self):
        print(self.__name, self.__credits, self.__grade)

class Student:
    """
    A class that represents a student with fields for ID, name, credits, and
    GPA.
    """
    __slots__ = ["__id", "__name", "__credits", "__gpa", "__courses"]

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__credits = 0
        self.__gpa = 0
        self.__courses = []
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits
    
    def get_gpa(self):
        return self.__gpa

    def get_courses(self):
        return self.__courses

    def print_student(self):
        """
        Prints a student's info to standard output.
        """
        print("Student: ID=", self.__id, ", name=", self.__name,
        ", credits=", self.__credits, ", GPA=", self.__gpa, sep="")
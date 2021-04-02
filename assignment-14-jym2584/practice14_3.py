import csv

def street_names(name, type, print_addresses = False):
    count = 0
    with open("data/streets.csv") as file:
        reader = csv.reader(file)
        for record in reader:
            if type == "address":
                address = record[0] + " " + record[1] + " " + record[2]
                address = address.lower().strip()
                if name in address:
                    if print_addresses:
                        print(address)
                    count +=1
            elif type == "streettype":
                for index in record:
                    index = index.lower().strip()
                    if index == name:
                        count += 1
    print("Counted", count, "instances of",name)

class Exam:
    __slots__ = ["__student", "__pointstotal", "__pointsearned"]
    def __init__(self, pointstotal):
        self.__student = ""
        self.__pointstotal = int(pointstotal)
        self.__pointsearned = 0
    
    def get_grade(self):
        return self.__pointsearned

    def take_exam(self, student):
        self.__student = student

    def grade_exam(self, points):
        if points > self.__pointstotal: # Assuming there is no extra credit for the exam
            print("Points exceed the total number of points allowed on the exam.", points, "/", self.__pointstotal)
            print("Give points to student? (Student would have:", points, "points on the exam)")
            ask = input("Type y for YES. Any other key for no: ")
            if ask == "y":
                self.__pointsearned = points
            else:
                pass # don't do anything
        else:
            self.__pointsearned = points

    def __str__(self):
        return "Student " + str(self.__student) + " with grade: " + str(self.__pointsearned) + " out of " + str(self.__pointstotal)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.__pointstotal == other.__pointstotal and self.__student == other.__student
    
def main():
    street_names("dr", "streettype")
    street_names("red leaf ln", "address")
    street_names("vista", "address", True)
    math_exam = Exam(25)
    math_exam.grade_exam(20)
    print(math_exam)

main()
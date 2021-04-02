class Person:
    __slots__ = ["__idd", "__name","__eyecolor"]
    def __init__(self,idd,name):
        self.__idd = idd
        self.__name = name
        self.__eyecolor = "Black"

    def __lt__(self, other):
        if type(self) == type(other):
            return self.__idd < other.__idd

    def __eq__(self, other):
        if type(self) == type(other):
            return self.__idd == other.__idd
        else:
            return False
    
    def __hash__(self):
        return hash(self.__idd)

    def __str__(self):
        return print("A person named", self.__name, "with ID:", self.__idd)
    def __repr__(self):
        string = "Name: " 
        string += self.__name
        string += ", ID: "
        string += str(self.__idd)
        string += " | "
        return string



def main():
    joe1 = Person(123456, "Joe")
    joe2 = Person(123456, "Bob")
    joe4 = Person(12345678, "Jane")
    joe3 = Person(235235325325, "Jill")
    person_dict = [joe1, joe2, joe3, joe4]

    person_dict.sort()
    print("Dictionary ordered", person_dict)

    person_dict_set = set(person_dict)

    print("Set with duplicate IDs", person_dict_set)
    print(joe1 == joe2)
    print(joe2 == joe3)
    print(joe1 == joe3)
    print(joe1.__hash__)
    print(joe2.__hash__)
    print(joe3.__hash__)

main()
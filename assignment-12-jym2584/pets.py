class Pet:
    CALORIES_PER_POUND = 3000

    __slots__ = ["__species", "__name", "__weight", "__fur_color", "__age"]

    def __init__ (self, name, weight, species, fur_color, age = 0):
        self.__name = name
        self.__weight = weight
        self.__species = species
        self.__fur_color = fur_color
        self.__age = age
    
    def feed(self, calories):
        print("Feeding", self.__name, calories, "Calories")
        self.__weight += calories / Pet.CALORIES_PER_POUND
        print(self.__name, "'s weight is", self.__weight, "lb")

    def walk(self, miles):
        print("Walking", self.__name, miles,"miles")
        pound = miles * (100 / Pet.CALORIES_PER_POUND)
        self.__weight -= pound
        print("Our pet is now skinnier!", round(self.__weight,3), "pounds")

    def get_name(self):
        return self.__name
    
    def get_weight(self):
        return self.__weight


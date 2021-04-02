class Car:
    __slots__ = ["__vin", "__make", "__model", "__year", "__mileage", "__fuel", "__fuel_size"]

    def __init__(self, vin, make, model, year):
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = 0
        self.__fuel = 0
        self.__fuel_size = 15

    def get_vin(self):
        return self.__vin

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    def get_fuel(self):
        return self.__fuel
 
    def filler_up(self, amount):
        fuel = self.__fuel + amount
        if fuel > self.__fuel_size:
            print("You cannot fuel your car past 15 gallons. Your",self.__model,"currently has",self.__fuel,"gallons.")
        else:
            self.__fuel += amount
            print("Fueled",self.__model, amount, "gallons. Now:",self.__fuel)

    def drive(self, miles):
        estimated_fuel_left = self.__fuel - (miles/self.__fuel) # Calculates estimated fuel when driving x miles
        if estimated_fuel_left <= 0: # If the estimated fuel consumption depletes the tank
            print("Your", self.__model, "will run out of fuel mid-trip!") # Do not drive the car
        else: # Otherwise drive the car
            self.__fuel = self.__fuel - (miles/self.__fuel)
            print("Drove", miles,"miles. Fuel left:",self.__fuel)


    def print_car(self):
        print("**Model", self.__model, "**\n",
            "Make", self.__make, "\n",
            "Year", self.__year, "\n",
            "VIN", self.__vin, "\n",
            "Mileage", self.__mileage, "\n",
            "Fuel", self.__fuel)

    def __str__(self):
        return "A " + str(self.__make) + " with model "  + str(self.__model) + ". VIN: " + str(self.__vin)
    
    def __repr__(self):
        string = "***VIN: " + str(self.__vin) + "***\n"
        string += "Make: " + str(self.__make) + "\n"
        string += "Model: " + str(self.__model) + "\n"
        string += "Year: " + str(self.__year) + "\n"
        string += "Mileage: " + str(self.__mileage) + "\n"
        string += "Fuel: " + str(self.__fuel) + "\n"
        string += "Fuel Size: " + str(self.__fuel_size) + "\n"
        return string

    def __eq__(self, other):
        if type(self) == type(other): # used to verify that the other value is the same type before trying to access its fields. Avoids AttributeError
            return self.__vin == other.__vin
        else:
            return False

    def __ne__(self, other): # Usually negates the value returned by the __eq__ function, if for example we want unequal vin numbers to be True instead of False
        return not self.__eq__(other)                                                               # or we want equal vin numbers to be False instead of True

    #########################################################################################################################################################################
    '''Comparing VIN number in order to use for sorting
    car_list = [car1, car2, car3, car4, car5]
    car_list.sort()

    print(car_list)
    '''
    def __lt__(self, other): # Less than
        if type(self) == type(other): # used to verify that the other value is the same type before trying to access its fields. Avoids AttributeError
            return self.__vin < other.__vin
        else:
            return False

    def __le__(self, other): # Less than equal to
        if type(self) == type(other): # used to verify that the other value is the same type before trying to access its fields. Avoids AttributeError
            return self.__vin <= other.__vin
        else:
            return False

    def __gt__(self, other): # Greater than
        if type(self) == type(other): # used to verify that the other value is the same type before trying to access its fields. Avoids AttributeError
            return self.__vin > other.__vin
        else:
            return False

    def __ge__(self, other): # Greater than equal to
        if type(self) == type(other): # used to verify that the other value is the same type before trying to access its fields. Avoids AttributeError
            return self.__vin >= other.__vin
        else:
            return False

    #########################################################################################################################################################################

    def __hash__(self):
        return hash(self.__vin)

def print_car(car):
    ''' From lecture
    '''
    print(car.get_vin(), car.get_make(), car.get_model(), car.get_year(), car.get_mileage(), car.get_fuel())
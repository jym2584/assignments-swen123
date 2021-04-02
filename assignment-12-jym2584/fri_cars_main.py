
from fri_cars import *

car1 = Car(2, "Mercedes Benz", "GL 250", 2000)
car2 = Car(59, "Tesla", "Cybertruck", 2021)
car3 = Car(59, "Tesla", "Cyber Car", 2019)
car4 = Car(24, "RIT", "Blue Inn", 2000)
car5 = Car(23, "MTA", "Subway Train", 1995)

def main_other():
    car1.print_car()
    car2.print_car()
    car1.filler_up(10)
    car2.filler_up(15)

    car1.drive(1000)
    car2.drive(150)

    print("PRINTING CLASS:", str(car1)) # samething as print(mercedes)
    print("PRINTING REPR:", repr(car1))
    
    print(car1 == car2) 
    print(car2 == car3) # VIN numbers are the same
    print(car1 == car3)
    '''From lecture
    '''
    #print_car(mercedes)
    #print_car(bmw)

def main_set():
    car_list = [car1, car2, car3, car4, car5]
    car_list.sort()
    car_set = set(car_list)

    print(car_list)
    #print(car_set)
def main():
    main_set()
    #print(hash("da"))

if __name__ == "__main__":
    #main()
    main_other()
    #main_set()
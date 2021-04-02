from among_us_core import *

def the_main():
    ''' The main, the game (Our among us game)
    '''
    tasks_list = create_tasks()
    the_ship = Ship(tasks_list)
    no_quit = True
    while no_quit:
        try:
            num = input("Number of imposters: ")
            if num == "":
                break
            elif int(num) > 0 and int(num) <= 4:
                the_ship.cafeteria(int(num))
                no_quit = False
            else:
                raise ValueError
        except:
            print("Invalid number of imposters (1-4 allowed)")
    

the_main()
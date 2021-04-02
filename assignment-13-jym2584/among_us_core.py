import array_queue
import list_stack
import node_stack
import node_queue
import random

class Task:
    '''Class for our tasks
    asks for name and location
    '''
    __slots__ = ["__name", "__location"]

    def __init__ (self, name, location):
        self.__name = name
        self.__location = location
    
    def get_location(self):
        return self.__location

    def __str__(self):
        return self.__name + " in " + self.__location

    def __repr__(self):
        return self.__name + " in " + self.__location

def create_tasks():
    '''Creates our tasks from the csv file
    @param tasks_list, returns a list of all tasks from the csv file
    '''
    tasks_list = list()
    with open("data/tasks_01.csv") as tasks:
        next(tasks)
        for task in tasks:
            task = task.strip().split(",")
            tasks_list.append(Task(task[0], task[1]))
    return tasks_list

class Crewmate:
    '''Class for crewmate, asks for color
    Creates an empty list (or stack) of tasks and 2 conditionals if they are murdered or if they are an imposter
    '''
    __slots__ = ["__color", "__tasks", "__murdered", "__is_imposter"]

    def __init__(self, color):
        self.__color = color
        self.__tasks = node_stack.Stack()
        self.__murdered = False
        self.__is_imposter = False
    
    def assign_task(self, task):
        self.__tasks.push(task)

    def next_task(self):
        return self.__tasks.pop()

    def get_tasks(self):
        return self.__tasks

    def get_current_task(self):
        return self.__tasks.peek()

    def get_color(self):
        return self.__color

    def is_murdered(self):
        return self.__murdered
    
    def murder(self):
        self.__murdered = True

    def set_imposter(self):
        self.__is_imposter = True
    
    def is_imposter(self):
        return self.__is_imposter

    def __str__(self):
        string = self.__color + " Crewmate"
        if self.__murdered:
            string += " (deceased)"
        return string

    def __repr__(self):
        string = "Crewmate \n"
        string += " color = " + str(self.__color) + "\n"
        string += " murdered = " + str(self.__murdered) + "\n"
        string += " tasks = " + str(self.__tasks) + "\n"
        string += " is imposter? = " + str(self.__is_imposter) + "\n"
        return string

class Ship:
    '''Our ship!
    Asks for tasks
    '''
    __slots__ = ["__locations", "__tasks"]

    def __init__(self, tasks):
        self.__tasks = tasks
        self.__locations = set()

        for task in tasks:
            self.__locations.add(task.get_location())

    def get_locations(self):
        return self.__locations
    
    def get_tasks(self):
        return self.__tasks
    
    ##############################################
    ''' Question 4 implementation
    '''
    
    def create_crewmates(self):
        '''Creates our crewmates
        @return crewmates, creates a list of crewmates with random colors
        '''
        crewmates = []
        color = ["Black", "Blue", "Brown", "Cyan", "Green", "Pink", "Purple", "Red", "White", "Yellow"]
        for _ in range(0,10): # Iteration that creates 10 crewmates
            random_color = color[random.randint(0, len(color)-1)] 
            crewmates.append(Crewmate(random_color)) # Adds a random color to the crewmate
            color.remove(random_color) # Removes that color from the list so that there are no crewmates of the same color
        return crewmates
    
    def add_tasks(self):
        '''Adds tasks to our crewmates
        @return crewmates, creates a list of crewmates with each crewmate having a random number of tasks. Imposters will have tasks but they won't do them
        '''
        crewmates = self.create_crewmates()
        for crew in crewmates:
            for _ in range(1, random.randint(2,5)): # Adds 1-4 tasks for each crew member
                crew.assign_task(self.__tasks[random.randint(0, len(self.__tasks)-1)]) # Adds a random task (duplicates allowed)
        return crewmates

    def create_imposters(self, value):
        '''Adds our imposters
        @return crewmates, creates a list of crewmates with a specified number of imposters
        '''
        crewmates = self.add_tasks()
        random.shuffle(crewmates) # "Randomizer" for adding imposters

        for i in range(0, value):
            crewmates[i].set_imposter() # Randomly sets the imposters

        return crewmates

    def cafeteria(self, value):
        '''Our game!
        @param crewmates, creates our crewmates, imposters and tasks
        @param cafeteria, a "list" where our crewmates will reside in
        @param crewmates_completed_tasks, a "list"/safezone where our crewmates have completed all their tasks!
        
        '''
        crewmates = self.create_imposters(value)
        random.shuffle(crewmates)
        cafeteria = node_queue.Queue()
        crewmates_completed_tasks = node_stack.Stack() # Where the crewmates that completed their tasks will go

        for crewmate in crewmates:
            cafeteria.enqueue(crewmate) # Adds all crewmates to the cafeteria
        
        while cafeteria.size() != 0: # While the cafeteria is not empty
            crewmate = cafeteria.dequeue() # dequeue the crew member so they can complete their task
            try:
                if not crewmate.is_imposter(): # If the crewmate is not an imposter
                    if not crewmate.is_murdered(): # If the crewmate is not murdered
                        task = crewmate.get_current_task() # Get their current task
                        print("The ", crewmate.get_color(), " crewmate begins: ", task, "....", sep="")
                        
                        probability = random.randint(1, 100) 
                        if probability <= 25: # 25% chance that they will be killed by an imposter
                            crewmate.murder() # Oof
                            print("  Oh no! An imposter killed ", crewmate.get_color(), "!", sep = "")
                        else:
                            crewmate.next_task() # Complete the crewmate's task
                            print("  Task complete!")
                            #print("  (Remaining tasks:", crewmate.get_tasks(), ")", sep="")
                            if crewmate.get_tasks().size() == 0: # If the crewmate has no more tasks left
                                crewmates_completed_tasks.push(crewmate) # Add them to a seperate list
                                print(crewmate.get_color(), "completed all tasks!") # And notify everyone that the crewmate has completed all their tasks!
                            else:
                                cafeteria.enqueue(crewmate)
                            #print("**********Crewmates in cafeteria", cafeteria, "******************\n")
            except:
                break

        print("\nThe journey has ended!")
        if crewmates_completed_tasks.size() > 0: # If there is at least one person that completed their tasks
            print("The crew has made it!") # Round won!
        else:
            print("The imposters wiped out the crew!") # Otherwise, the imposters win
        for crew in crewmates:
            if not crew.is_imposter():
                print("  ", crew)
        
        print("\nImposters:")
        for crew in crewmates:
            if crew.is_imposter():
                print("  ", crew)


    ##############################################


    def __str__(self):
        return "A ship with lots of tasks!"

    def __repr__(self):
        string = "Ship with: \n"
        string += "  Tasks: " + str(self.__tasks) + "\n"
        string += "  Locations: " + str(self.__locations)
        return string

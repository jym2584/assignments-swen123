"""This file plots search times with arrays
"""
import plotter
import array_utils as a
import arrays
import time
import searches

def linear_search(an_array, target):
    """Searches for the runs + 1
    """
    #print(an_array)
    #loop over all indexes
    for i in range(len(an_array)):
    #if value at index matches target, return index
        if an_array[i] == target:
            run = i + 1
            return run
    #If not found, return none
    return None

def linear_timer(an_array, target):
    """ Function for linear timer
    """
    start = time.perf_counter()
    linear_search(an_array,target)
    end = time.perf_counter()
    return end - start

def linear_plot(size,runs):
    """ This plots the time it takes to find an element(s) in an array
    an_array = creates the array
    run = verifies that the runs in the array matches up with the user defined
    """
    an_array = a.range_array(0,size+1)
    run = linear_search(an_array, runs)

    plotter.init("Linear Search Times", "Length", "Time")

    for i in range(0,run):
        #print(i)
        #print(an_array[int((size/run)*(run))])
        plotter.add_data_point(linear_timer(an_array, an_array[int((size/run)*i)]))
    
    plotter.plot()


def main():
    #linear_plot(100000,20)

    no_quit = True

    while no_quit == True: # While the program is still active
        try:
            size = input("Enter a size (integer): ")
            if size == "":
                confirm_quit = input("Press enter to quit. Return any value to continue...")
                if confirm_quit == "":
                    break

            runs = input("Enter a run (integer): ")
            if runs == "":
                confirm_quit = input("Press enter to quit. Return any value to continue...")
                if confirm_quit == "":
                    break

            else:
                size = int(size)
                runs = int(runs)
                linear_plot(size,runs)

        except ValueError:
            print("The value you just inputted is not a valid integer!")
            
    #an_array = a.range_array(0,100)
    #print(an_array)
    #print("Linear search:",linear_search(an_array, 0))
main()
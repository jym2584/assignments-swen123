import arrays
import array_utils as a
import time
import sorts as s
import merge_sort as m
import plotter as p
import quicksort as q
import hybridsort as h
def time_sort(sort_function, data):
    '''Calculates the time a specified function sorts with a given array
    '''
    start = time.perf_counter()
    sort_function(data)
    end = time.perf_counter()
    timer = end-start
    return timer

def plot_sort_time(sort, data):
    '''Plots the copied array given a sort function
    '''
    copied = a.copy_array(data)
    p.add_data_point(time_sort(sort,copied))
   
def plot_times(sort, random, sorted2, reverse, double, mostly):
    '''Plots 5 points (random, sorted2, reverse, double, mostly) given a sort function
    '''
    #p.init("Sort Timer (random, sorted, reverse, double, mostly)", "Length", "Time")
    print("   Finished initializing plot for random")
    plot_sort_time(sort, random)
    #p.new_series()

    print("   Finished initializing plot for sorted")
    plot_sort_time(sort, sorted2)
    #p.new_series()

    print("   Finished initializing plot for reverse")
    plot_sort_time(sort, reverse)
    #p.new_series()

    print("   Finished initializing plot for double")
    plot_sort_time(sort, double)
    #p.new_series()

    print("   Finished initializing plot for mostly")
    plot_sort_time(sort, mostly)
    print("   Done!")

def main():
    '''These are my plots!
    '''
    #filename = "data/random.txt"
    #print("Time took to sort ", filename, ": ",time_sort(s.insertion_sort, filename), sep="")\
    random = a.create_array("data/random.txt")
    sorted2 = a.create_array("data/sorted.txt")
    reverse = a.create_array("data/reverse.txt")
    double = a.create_array("data/two_lists.txt")
    mostly = a.create_array("data/mostly_sorted.txt")
    #print("Waiting for plot 'Merge Sort' to print...")


    p.init("Sort Timer using Merge, Insertion, Bubble, Quick, Quickbubble and Mergesertion Sort (random, sorted, reverse, double, mostly)", "Sort Type", "Time")
    print("Plotting Merge Sort...")
    plot_times(m.merge_sort, random, sorted2, reverse, double, mostly)
    p.new_series()


    #print("Waiting for next plot 'Insertion Sort' to print...")
    #p.init("[First 15 values] Sort Timer using Insertion Sort (random, sorted, reverse, double, mostly)", "Length", "Time")
   
   
    print("\nPlotting Insertion Sort...")
    plot_times(s.insertion_sort, random, sorted2, reverse, double, mostly)
    p.new_series()


    #print("Waiting for next plot 'Bubble Sort' to print...")
    #.init("[First 15 values] Sort Timer using Bubble Sort (random, sorted, reverse, double, mostly)", "Length", "Time")
   
   
    print("\nPlotting Bubble Sort...")
    plot_times(s.bubble_sort, random, sorted2, reverse, double, mostly)

    ## Fri, Oct 2
    p.new_series()

    print("\nPlotting Quick Sort...")
    plot_times(q.quicksort, random, sorted2, reverse, double, mostly)
    p.new_series()

    print("\nPlotting Quickbubble Sort...")
    plot_times(h.quickbubble_sort, random, sorted2, reverse, double, mostly)
    p.new_series()

    print("\nPlotting Mergesertion Sort...")
    plot_times(h.mergesertion_sort2, random, sorted2, reverse, double, mostly)

    print("\n***Plot finished. Plotting...***")
    p.plot(log = True)
    input("Press enter to continue...")
    #print("Waiting for next plot 'Shift' to print...")
    #p.init("[First 15 values] Sort Timer using Shift (random, sorted, reverse, double, mostly)", "Length", "Time")
    #plot_times(s.shift, random, sorted2, reverse, double, mostly)

    #Merge and Insertion sorts are better

if __name__ == "__main__":
    main()
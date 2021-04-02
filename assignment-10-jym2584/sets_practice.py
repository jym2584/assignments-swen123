import random

def create_sets():
    # Just creates the four provided sets
    max_set = set()
    min_set = set()
    find_set = set()
    len_set = set()

    for i in range(9):
        max_set.add(random.randint(0,100))
        min_set.add(random.randint(0,100))
        find_set.add(random.randint(0,100))
        len_set.add(random.randint(0,100))

    return max_set, min_set, find_set, len_set

def find_max(max_set):
    # Given the provided set, print out the max number and the set itself
    a_list = []
    for i in max_set:
        a_list.append(i)
    a_list.sort()
    print(a_list)
    print("The largest number is", a_list[-1])
    pass

def find_min(min_set):
    # Given the provided set, print out the least number and the set itself
    a_list = []
    for i in min_set:
        a_list.append(i)
    a_list.sort()
    print(a_list)
    print("The smallest number is", a_list[0])
    pass

def find_num(find_set, target):
    # Given the provided set, print out whether or not the target number is in the set
    print(find_set)
    if target in find_set:
        print("Found", target, "in the set")
    else:
        print("Did not find a value with", target, "in the set")
    pass

def length_set(len_set):
    # Given the provided set, find and print out the length of the set along with the set itself
    counter = 0
    for _ in len_set:
        counter += 1
    print(len_set)
    print("There are", counter, "values in the set")
    pass

def main():
    max_set, min_set, find_set, len_set = create_sets()
    find_max(max_set)
    find_min(min_set)
    find_num(find_set, random.randint(0, 100))
    length_set(len_set)

if __name__ == "__main__":
    main()
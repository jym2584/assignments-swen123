import plotter

def print_lines(filename):
    file = open(filename)
    for line in file:
        print(line.strip())

def word_search(filename):
    search = input("Search the word: ")
    found_it = False
    with open(filename) as file:
        for line in file:
            if line.strip() == search:
                found_it = True
                break
    if found_it:
        print("Found", search)
    else:
        print("Can't find")

def longest_word(line):
    words = line.split()
    longest_word = ""
    #print(find_word)
    for word in words: # word variable is created that is used by words
        if len(word) > len(longest_word):
            longest_word = word     

    if len(longest_word) > 0:
        print("Longest Word:", longest_word)  

def longest_words(filename):
    file = open(filename)
    for line in file:
        longest_word(line)
    file.close()

def print_names(filename):
    file = open(filename)
    next(file)
    for line in file: # reading all the lines in the file
        words = line.split(",")
        print(words[1], words[0])
    file.close()

def average_grade(filename, column):
    with open(filename) as file:
        header = next(file).strip().split(",") # Split
        count = 0
        sum = 0
        for line in file: #for each line in the file
            count += 1
            grades = line.strip().split(",")
            sum += float(grades[column])
    print(header[column], "has an average of",sum/count)


def plot_grades(filename, column):
    with open(filename) as file:
        header = next(file).strip().split(",") # Split
        plotter.init(header[column], "Students", "Grades")
        for line in file: #for each line in the file
            grades = line.strip().split(",")
            plotter.add_data_point (float(grades[column]))
    plotter.plot()

def main():
    #print_lines("data/alice.txt")
    #word_search("data/words.txt")
    #longest_word("Hello I am the longest word")
    #longest_words("data/alice.txt")
    #print_names("data/grades_010.csv")
    average_grade("data/grades_010.csv", 7)
    #plot_grades("data/grades_010.csv", 5)
    input("Press enter to continue...")
main()
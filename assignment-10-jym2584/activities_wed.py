import re
def dict_from_slides():
    a_dict = dict()
    b_dict = {}

    c_dict = {"one":1, "two":2}
    c_dict["three"] = 3
    c_dict["one"] = 1111

def names():
    names = {}
    names ["J"] = "Jin"
    names ["Y"] = "Young"
    names ["M"] = "Moon"
    names ["S"] = "Seong"
    names ["H"] = "Ho"
    names ["M"] = "Moon"

    print(names["J"])
    print(names["Y"])
    print(names["M"])
    print(names["S"])
    print(names["H"])
    print(names["M"])

def print_dict(a_dict):
    for key in a_dict:
        print(key,":",a_dict[key])

def count_words(filename):
    word_dict = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            tokens = line.split()
            for word in tokens:
                word = word.lower()
                words = re.findall("[\w\']+",word) # breaks up the word in alphanumeric
                for word in words:
                    if word not in word_dict:
                        word_dict[word] = 0
                    word_dict[word] +=1
    return word_dict
def main():
    a_dict = {'a':1, 2:'b', 'hello':('world', '!')}
    print_dict(a_dict)

    words = count_words("data/alice.txt")
    max = 0
    max_word = ''
    for key in words:
        if words[key] > max:
            max = words[key]
            max_word = key
    print(max_word, 'appears in allice', max, "times!")

main()
def string_lower(filename):
    ''' Converts strings into lowercase and puts them into a list
    @param words, appends each word into the list
    
    @return words, returns the list
    '''
    words = []
    with open(filename) as file:
        for word in file:
            words.append(word.strip().lower())
    #print(words)
    return words

def sort_string(string):
    ''' Sorts each character in the string into alphabetic order
    @param list, creates a list where we append each character into the list then we sort it
    @param str, for each index in the list, we append the sorted list into the str.

    @return str, returns the string with each character in alphabetic order
    '''
    list = []
    str = ""
    for i in string:
        list.append(i)

    list.sort()

    for i in list:
        str += i

    return str

def build_words(word_list):
    ''' Builds various words given a word
    @param words, set that sorted_word will be appended on

    @returns words, returns the list of words
    '''
    words = {}

    for word in word_list:
        sorted_word = sort_string(word)

        if sorted_word not in words:
            words[sorted_word] = []

        words[sorted_word] += [word]

    return words


def unscramble(letters, words):
    ''' Unscrambles the words and allows the user to choose a matching word based on the index
    @param sorted_word, sorts the strings 
    @param length, grabs the length of the matching word

    @return matching_words, returns a list of possible words
    '''
    sorted_word = sort_string(letters)

    if sorted_word in words:
        matching_words = words[sorted_word]
        length = len(matching_words)

        if length ==1:
            return matching_words[0]
        else:

            for index in range(length):
                print(index,": ", matching_words[index], sep="")

            chosen = int(input("Enter the index of the word: "))

            return matching_words[chosen]

    return None

def prompt_for_word(dictionary):
    '''Prompts the user for a word and index
    @param tokens, splits the responses into 2:
        @param word, accesses the first response
        @param tokens[1: ], accesses index
    @param characters, appends the word

    @return characters, return the characters  
    '''
    clue = input("Enter clue: ")
    tokens = clue.split()
    word = tokens[0]
    characters = ""
    unscrambled_word = unscramble(word, dictionary)
    for index in tokens[1:]:
        characters += unscrambled_word[int(index)]
    
    return unscrambled_word, characters

def main():
    ''' Main bulk of the game, returns the solution of the puzzle given the 'circled' words from the prompt
    @param words, Accesses the text file
    @param dictionary, builds a dictionary from the text file
    @prompt, prompts the user for a clue and index of words
    @solution, grabs first index of the prompt
    '''
    words = string_lower("data/words.txt")
    dictionary = build_words(words)

    prompt = prompt_for_word(dictionary)
    print("word:", prompt[0])
    prompt1 = prompt_for_word(dictionary)
    print("word:", prompt1[0])
    
    prompt2 = prompt_for_word(dictionary)
    print("word:", prompt2[0])
    
    prompt3 = prompt_for_word(dictionary)
    print("word:", prompt3[0])

    solution = str( prompt[1] + prompt1[1] + prompt2[1] + prompt3[1])
    
    print("Solution to the puzzle: " + str(unscramble(solution, dictionary)))



if __name__ == "__main__":    
    main()
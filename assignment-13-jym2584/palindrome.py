from list_stack import *
import re

def palindrome(string):
    ''' Creates a palindrome. Creates conditionals where if the string is a vowel, then there should be no repeats
    @param new_string, where we will append each letter onto the new_string
    @param a_stack, where we will push and pop our letters to create a palindrome
    @param vowel, conditional if the end of the letter contains a vowel
    @param string, lowercases the letters in the string
    
    @return new_string, returns the palindrome in a list
    '''
    new_string = []
    a_stack = Stack()
    vowel = False
    string = string.lower()

    for letter in string:
        ''' For each letter in the string, push the letter onto the stack
                                           append the letter onto the new_string list
        ''' 
        a_stack.push(letter)
        new_string.append(letter)

    # If the last letter contains a vowel
    if a_stack.peek() == 'a' or \
       a_stack.peek() == 'e' or \
       a_stack.peek() == 'i' or \
       a_stack.peek() == 'o' or \
       a_stack.peek() == 'u':
        
        vowel = True

    if vowel: # If it does contain a vowel
        a_stack.pop() # Pop the last letter
        for _ in range(0, len(string) - 1): # Append each letter without the extra vowel
            value = a_stack.pop()
            new_string.append(value)
    else:
        for _ in range(0, len(string)): # Otherwise, append each letter with the extra vowel
            value = a_stack.pop()
            new_string.append(value) 

    print("Your palindrome:", end=" ")
    for letter in new_string: # Iterates through the new_string and prints out the palindrome
        print(letter, end="")  
    
    return new_string


def main():
    ''' Runs our palindrome function, checks for conditionals first if the input contains only letters
    '''
    no_quit = True
    while no_quit:
        string = str(input("Enter any letters for your palindrome: "))
        if re.search('^[a-zA-Z]*$', string):
            palindrome(string)
            no_quit = False
        else:
            print("All characters in the string does not contain only letters, try again.")

if __name__ == "__main__":
    main()
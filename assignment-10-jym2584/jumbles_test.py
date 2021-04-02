from jumbles import *
import io

def test_string_lower():
    '''Testing function for string lower
    Created new file to test with capitalized characters
    '''
    filename = "data/words_test.txt"
    expected = ['ate', 'eat', 'loot', 'tea', 'tool']
    actual = string_lower(filename)
    assert expected == actual

def test_sort_string():
    '''Testing function for comparing da strings
    '''
    expected = "aaccerr"
    string = "racecar"
    actual = sort_string(string)
    assert expected == actual

def test_build_words():
    '''Testing function for building the wordss
    '''
    word_list = string_lower("data/words_small.txt")
    expected = ['loot', 'tool']
    actual = build_words(word_list)
    assert expected == actual['loot']

def test_unscramble(capsys, monkeypatch):
    letters = "aet"
    words = build_words(string_lower("data/words_small.txt"))
    expected = "ate"

    user_input = io.StringIO("0\n")
    monkeypatch.setattr('sys.stdin', user_input)

    actual = unscramble(letters, words)
    print("\n",actual, sep="")

    captured_out = capsys.readouterr().out
    assert expected == captured_out.split("\n")[-2] 

def test_prompt_for_word(capsys, monkeypatch):
    #setup
    word_list = string_lower("data/words.txt")
    diction ary = build_words(word_list) 
    expected = "('balky', 'b')"


    user_input = io.StringIO("klayb 0\n0\n")
    monkeypatch.setattr('sys.stdin', user_input)
    

    actual = prompt_for_word(dictionary)
    print(actual)

    captured_out = capsys.readouterr().out
    grab_last_index = captured_out.strip().split(": ")[-1]
    assert expected == grab_last_index
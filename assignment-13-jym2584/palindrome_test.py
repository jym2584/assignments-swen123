from palindrome import *
import io 

def test_palindrome_no_vowels(capsys):
    '''Tests if the palindrome contains no vowels. Should contain the same letter
    '''
    #setup
    string = "bad"
    #invoke
    palindrome(string)
    #assert
    captured_out = capsys.readouterr().out
    assert captured_out.split()[-1] == "baddab"

def test_palindrome_vowels(capsys):
    '''Tests if the palindrome contains vowels. Should not contain the same letter
    '''
    #setup
    string = "hello"
    #invoke
    palindrome(string)
    #assert
    captured_out = capsys.readouterr().out
    assert captured_out.split()[-1] == "hellolleh"

def test_main(capsys, monkeypatch):
    #setup
    user_input = io.StringIO("hello\n")
    #invoke
    monkeypatch.setattr('sys.stdin', user_input)
    main()
    #assert
    captured_out = capsys.readouterr().out
    assert captured_out.split()[-1] == "hellolleh"
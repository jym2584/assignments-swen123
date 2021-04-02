from activities import *
import io

def test_factorial():
    #setup
    num = 5
    expected = 120
    
    #invoke
    actual = factorial(num)
    
    #analysis
    assert actual == expected

def test_factorial_zero():
    result = factorial(0)
    assert result == 1

def test_factorial_invalid():
    num = -1
    try:
        factorial(num)
        assert False

    except ValueError:
        pass

def test_is_equally_divisible(capsys):
    #Setup
    numerator = 35
    denominator = 7
    expected = "35 Is equally divisble to 7"
    #Invoke
    is_equally_divisable(numerator, denominator)
    #Analysis
    captured = capsys.readouterr()
    actual = captured.out.strip()
    assert actual == expected

def test_is_equally_divisible_false(capsys):
    #Setup
    numerator = 35
    denominator = 8
    expected = "35 Is not equally divisble to 8"
    #Invoke
    is_equally_divisable(numerator, denominator)
    #Analysis
    captured = capsys.readouterr()
    actual = captured.out.strip()
    assert actual == expected

def test_get_move(monkeypatch, capsys):
    #Setup
    userinput = io.StringIO("1\n1\nX\n")
    monkeypatch.setattr("sys.stdin", userinput)
    expected = (1, 1, 'X')

    # Invoke
    actual = get_move()

    #Analysis
    assert expected == actual
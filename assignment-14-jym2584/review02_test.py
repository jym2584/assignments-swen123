from review02 import *
import io

def test_is_power():
    a = 256
    b = 4
    expected = True
    actual = is_power(a,b)
    assert expected == actual

def test_what_power_base():
    a = 1
    b = 1
    expected = 0
    actual = what_power(a,b)
    assert expected == actual

def hat_power_exceptioon():
    a = 15
    b = 3
    #invoke
    try:
        what_power(a,b)
        assert False
    #analysis
    except ValueError:
        assert True

def test_what_power_base_true():
    a = 256
    b = 4
    expected = 4
    actual = what_power(a,b)
    assert expected == actual

def test_tuplify(capsys, monkeypatch):
    #setup
    monkeypatch.setattr('sys.stdin', io.StringIO("Bruce\nLee\nHerring\n"))
    expected = "('Bruce', 'Lee', 'Herring')"
    #invoke
    actual = tuplify()
    print(actual)
    #analysis
    actual = capsys.readouterr().out.strip()
    actual = actual.split(": ")[-1]
    assert expected == actual

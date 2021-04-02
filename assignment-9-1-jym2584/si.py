import io

def ask_name():
    name1 = input("What is your name: ")
    name2 = input("What is your second name: ")
    print("Hello", name1)
    print("Hello", name2)
    return name1, name2

def ask_age():
    age1 = input("What is your age? ")
    print("Your age is", age1)

def test_ask_name(capsys, monkeypatch):
    da_input = io.StringIO("Jackson\nJin\n")
    monkeypatch.setattr('sys.stdin', da_input)

    ask_name()
    captured = capsys.readouterr().out

    assert ("Hello Jackson\nHello Jin" == captured.split(": ")[-1].strip())

def test_ask_age(capsys, monkeypatch):
    #Setup
    THE_INPUT = io.StringIO("10")
    monkeypatch.setattr('sys.stdin', THE_INPUT)
    #Invoke
    ask_age()
    #Analyze
    captured = capsys.readouterr().out
    assert("Your age is 10") == captured.split("? ")[-1].strip()
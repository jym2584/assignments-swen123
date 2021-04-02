from pizza_pizza import *
import io

def test_take_order(monkeypatch):
    '''Tests our ordering system
    '''
    #setup
    user_input = io.StringIO("s\np\np\nb\ncf\na\n")
    #invoke
    monkeypatch.setattr('sys.stdin', user_input)
    pizzas = order_pizza()
    #analyze
    assert 15.9 == pizzas["1"].price
    assert 10.75 == pizzas["2"].price

def test_print_pizzas(monkeypatch, capsys):
    '''Tests the total result of our pizza
    '''
    #setup
    user_input = io.StringIO("s\np\np\nb\ncf\na\n")
    #invoke
    monkeypatch.setattr('sys.stdin', user_input)
    pizzas = order_pizza()
    print_pizzas(pizzas)
    #analyze
    captured_out = capsys.readouterr().out
    assert "26.65 \n\n\n\n" == captured_out.split("Total: ")[-1]
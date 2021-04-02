from food_truck import *
import io
import sys

def test_create_abbreviation():
    '''Tests the returned abbreviation to the actual word
    '''
    #invoke
    food_menu_abbrv = create_abbreviations()
    #analyze
    assert food_menu_abbrv["p"] == "Pepsi"

def test_menu():
    '''Tests if the dictionary works
    '''
    food_menu = menu()
    assert food_menu["drinks"] == ["Pepsi", "Water", "Tea"]

def test_print_menu():
    '''Not sure how to test print statements, do I test part of it?
    '''
    pass

def test_order_combo(capsys, monkeypatch):
    '''Tests ordering the combo. We should get the price of the 3 items!
    '''
    #setup
    user_input = io.StringIO("p\nb\npc\n")
    expected = "4.24\n"
    #invoke
    monkeypatch.setattr('sys.stdin', user_input)
    order_combo()
    #analyze
    captured_out = capsys.readouterr().out
    assert expected == captured_out.split(": ")[-1]

def test_take_order(monkeypatch):
    '''Tests taking an order twice
    '''
    #setup
    user_input = io.StringIO("p\nb\npc\ny\nw\nr\nff\n\n")
    expected = [['Pepsi', 'Burger', 'Potato Chips'], ['Water', 'Rice', 'French Fries']]
    #invoke
    monkeypatch.setattr('sys.stdin', user_input)
    order = take_order()
    #analyze
    assert expected == order



def test_print_order(capsys, monkeypatch):
    '''Tests our entire ordering system
    '''
    #setup
    user_input = io.StringIO("p\nb\npc\ny\nw\nr\nff\n\n")
    expected = ['Total: 15.74', 'Thanks for visiting us! Never leave hungry']
    
    #invoke
    monkeypatch.setattr('sys.stdin', user_input)
    print_order()
    
    #assert
    captured_out = capsys.readouterr().out
    assert expected == captured_out.split("\n")[-3:-1]
    pass

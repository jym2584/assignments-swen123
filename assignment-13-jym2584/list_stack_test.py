from list_stack import *

def test_constructor():
    #setup

    #invoke
    a_stack = Stack()
    #analysis
    assert a_stack.size() == 0
    assert a_stack.is_empty()

def test_print():
    a_stack = Stack()

    actual = repr(a_stack)


    assert actual == '[]'


def test_push():
    a_stack = Stack()

    #invoke
    a_stack.push(5)
    a_stack.push('c')

    actual = repr(a_stack)


    assert actual == "[5, 'c']"
    assert a_stack.size() == 2

def test_peek():
    a_stack = Stack()
    a_stack.push(5)
    a_stack.push('c')

    actual = a_stack.peek()

    assert actual == 'c'
    assert a_stack.size() == 2
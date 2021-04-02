from node import *

def test_constructor():
    value = 5

    a_node = Node(value)

    assert a_node.get_value() == value
    assert a_node.get_next() == None

def test_print(capsys):
    seq = Node('a')
    seq = Node('d', seq)
    seq = Node('x', seq)

    print_node(seq)

    actual = capsys.readouterr().out
    assert actual == 'x, d, a, '


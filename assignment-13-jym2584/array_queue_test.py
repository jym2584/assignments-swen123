from array_queue import *

def test_constructor():
    #setup

    #invoke
    queue = Queue()

    assert queue.size() == 0
    assert queue.is_empty()


def test_repr():
    #setup
    queue = Queue()
    #invoke
    actual = repr(queue)

    assert actual == "[]"
    assert queue.is_empty()
    assert queue.size() == 0

def test_enqueue():
    #setup
    queue = Queue()
    value1 = 'a'
    value2 = 'c'

    #invopke
    queue.enqueue(value1)
    queue.enqueue(value2)

    #assert
    assert not queue.is_empty()
    assert repr(queue) == "[a, c]"
    assert queue.size() == 2

def test_front_and_back():
    #setup
    queue = Queue()
    value1 = 'a'
    value2 = 'c'
    queue.enqueue(value1)
    queue.enqueue(value2)
    #invopke
    actual1 = queue.front()
    actual2 = queue.back()

    #assert
    assert repr(queue) == "[a, c]"
    assert queue.size() == 2
    assert actual1 == value1
    assert actual2 == value2
    assert not queue.is_empty()

def test_dequeue():
    #setup
    queue = Queue()
    value1 = 'a'
    value2 = 'c'
    queue.enqueue(value1)
    queue.enqueue(value2)
    #invopke
    value = queue.dequeue()

    #assert
    assert value == 'a'
    assert repr(queue) == "[c]"
    assert queue.size() == 1
    assert not queue.is_empty()

def test_dequeue_all():
    #setup
    queue = Queue()
    value1 = 'a'
    value2 = 'c'
    queue.enqueue(value1)
    queue.enqueue(value2)
    #invopke
    queue.dequeue()
    queue.dequeue()

    #assert
    assert repr(queue) == "[]"
    assert queue.size() == 0
    assert queue.is_empty()

def test_resize():
    #setup
    queue = Queue(1)
    value1 = 'a'
    value2 = 'c'
    queue.enqueue(value1)
    queue.enqueue(value2)
    #invopke


    #assert
    assert not queue.is_empty()
    assert repr(queue) == "[a, c]"
    assert queue.size() == 2
import node

class Stack:
    ___slots___ = ["__top", "__size"]

    def __init__ (self):
        self.__top = None
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__top == None
    
    def push(self, value):
        new_node = node.Node(value, self.__top)
        self.__top = new_node
        self.__size += 1

    def pop(self):
        value = self.__top.get_value()
        self.__top = self.__top.get_next()
        self.__size -= 1
        return value

    def peek(self):
        return self.__top.get_value()
    
    def __stringify(self, node):
        if node == None:
            return ''
        else:
            tail = self.__stringify(node.get_next())
            head = str(node.get_value()) + ', '
            return tail + head
    

    def __repr__(self):
        string = '[' + self.__stringify(self.__top)[:-2] + ']'
        return string

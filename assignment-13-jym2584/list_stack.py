#import node

class Stack:
    ___slots___ = ["__top", "__size"]

    def __init__ (self):
        self.__top = []
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__top == []
    
    def push(self, value):
        self.__top.append(value)
        self.__size += 1

    def pop(self):
        value = self.__top.pop()
        self.__size -= 1
        return value

    def peek(self):
        return self.__top[-1]

    def __repr__(self):
        return str(self.__top)
'''Assignment 13.2'''

import node

class Queue:
    __slots__ = ["__size", "__front", "__back", "__array"]

    def __init__(self):
        self.__size = 0
        self.__front = None
        self.__back = None

    def is_empty(self):
        return self.__size == 0

    def size(self):
        return self.__size
        
    def front(self):
        '''Grabs the front value of the Queue
        Eg:
        [9[8[7,None]]]
        ---> Grabs 9
        '''
        if self.__size == 0:
            raise IndexError("Queue is empty")
        else:
            return self.__front.get_value()

    def back(self):
        ''' Grabs the back value of the Queue
        [9[8[7,None]]]
        ---> Grabs 7
        '''
        if self.__size == 0:
            raise IndexError("Queue is empty")
        else:
            return self.__front.get_next().get_value()
    
    def enqueue (self, value):
        ''' Appends the value onto the Next Value
            enqueue(9)
                [9,None] 
            enqueue(8)
                [9,[8, None]]
        '''
        if self.__back == None:
            self.__front = node.Node(value)
            self.__back = self.__front
            self.__size += 1
        else:
            self.__back.set_next(node.Node(value))
            self.__back = self.__back.get_next()
            self.__size += 1

    def dequeue(self):
        ''' Gets rid of the front value
            enqueue(9)
                [9,None] 
            enqueue(8)
                [9,[8, None]]
            dequeue()
                [8, None]       
        '''
        if self.__front == None:
            return None
        else:
            value = self.__front.get_value()
            self.__front = self.__front.get_next()
            self.__size -= 1
            return value

    def __repr__(self):
        ''' String representation of the queue
        '''
        string = "["
        node = self.__front
        if node is not None:
            string += str(node.get_value())
            node = node.get_next()
            while node is not None:
                string += ", " + str(node.get_value())
                node = node.get_next()
        string += "]"
        return string
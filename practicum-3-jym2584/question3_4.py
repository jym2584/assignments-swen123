'''
Jin Moon

This is a two part question. You may not elect to do only part 2.

PART 1
Create a new Pair class that will store two entities, first and second. 
The class should use appropriate data encapsualation including private
state, a constructor, and accessor/mutators for all state values.

PART 2
Add the following behavior to the Pair class.
The ability to display a representation of a pair's values using print
    Example: >>>print (a_pair)
             (first, second)
The ability to compare two pairs for equality
The ability to use a pair in a set
The ability to to sort a list of pairs with the first entity
    having priority. I.E. sort by first first and second second.
'''

class Pair:
    '''
    Complete this class based on the above information
    '''
    __slots__ = ["__first", "__second"]

    def __init__(self, first, second):
        self.__first = str(first)
        self.__second = str(second)
    
    def get_first(self):
        return self.__first
    
    def get_second(self):
        return self.__second

    def set_first(self, slot):
        self.__first = slot
    
    def set_second(self, slot):
        self.__second = slot

    def __str__(self):
        return "(" + self.get_first() + ", " + self.get_second() + ")"

    def __eq__(self, other):
        if type(self) == type(other):
            return self.__first == other.__first and self.__second == other.__second
    
    def __hash__(self):
        return hash(self.__first + self.__second)

    def __gt__(self, other):
        if type(self) == type(other):
            if self.__first == other.__first:
                return self.__second > other.__second
            else:
                return self.__first > other.__first


if __name__ == '__main__':
    pair = Pair(5, 'z')
    expected = "(5, z)"
    print(pair)
    pass
    ''' Your non-test code goes here, if you have any '''
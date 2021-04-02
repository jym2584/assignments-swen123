"""
Jin Moon

Write a function, contains_all, that declares parameters for two lists. 
Return True if the first list contains all of the elements in the second list,
and false otherwise.

You are guaranteed that none of the values in either list is repeated.

Your function must run in linear time.
"""
def contains_all(a_list, b_list):
    a_set = set(a_list)
    for item in b_list:
        if item not in a_set:
            return False
    return True

if __name__ == '__main__':
    a_list = [1, 2, 3, 4, 5]
    b_list = [2, 4, 3]
    a_list2 = [1, 2, 3, 4, 5]
    b_list2 = [1, 2, 5, 4, 3, 6]
    print(a_list)
    print(b_list)
    print(contains_all(a_list, b_list))
    print(a_list2)
    print(b_list2)
    print(contains_all(a_list2, b_list2))
    ''' Your non-test code goes here, if you have any '''
'''
Jin Moon

You are not allowed to add any additional functions to the code, use the ones
provided. Use python exam_test.py to run your code. If you must, you can add
calls into the section after if __name__ == "__main__" at the bottom of the file.

Practicum Question #2

An alternative to CSV for storing rows of fields in a file is a Fixed Length Field file.  Like
a CSV file, each line represents a record.  However, unlike a CSV file, fields are not
separated by a comma, but rather each field has a designated start and end column.  If the data
is shorter than the field length it is padded with spaces on the right side.

In the example below, the first field, Name, starts at column 0 and
ends at column 7 (inclusive).  The first 2 rows of column numbers are for
ease of reading and do not exist in the file.

          1111111111222222
01234567890123456789012345
--------------------------
NAME    TYPE  COLOR    AGE
Gilbert dog   brown    11
Herman  bird  green    27
Pokey   turtlebrown    103
Bingo   bird  blue     11
Rascal  snake turquoise5  
Garfieldcat   orange   44 

This data is provided for you in data/sample_pets.txt.  Note that the file does not contain the
column numbers, but does contain the header row.  If you alter the file for your testing purposes,
remember that each line should be exactly 26 characters long.

Part A
Implement function, get_field_data that has parameters for a string representing a record, 
and 2 integers representing a column start and column end.  Both column start and column end 
are inclusive.  The function should return a string containing the field data and all leading 
and trailing whitespace stripped. This function must use slicing.
Add your code to this module.

Examples
record = "Herman  bird  green    27 "
get_field_data(record,0,7) = "Herman"
get_field_data(record,23,25) = "27"

Part B
Implement function, count_pets that has parameters for a string representing the filename
containing fixed field length data, a string representing a field name to search on, and a string
representing a field value.

Using the get_field_data function written for Part A, return the count of pets in which the given
value of the given field matches the data.

If the file cannot be opened for reading, the function should return None.

You can assume the file is in the format of the example above and that fields begin and end
in the same columns.  You can hardcode start and end values of each field in the function.

Examples for above sample data set
count_pets("data/sample_pets.txt","NAME","Rascal") = 1
count_pets("data/sample_pets.txt","TYPE","bird") = 2
count_pets("data/sample_pets.txt","COLOR","yellow") = 0
count_pets("data/sample_pets.txt","AGE","27") = 1
'''

"""
Part A
"""
def get_field_data (record, col_start, col_end):
    with open(record) as file:
        next(file)
        for line in file:
            print(line[col_start:col_end])

"""
Part B
"""
def count_pets(filename,field,value):
    count = 0
    with open(record) as file:
        next(file)
        for line in file:
            line_split = line.split()
            for i in line_split:
                if i == value:
                    count += 1
                    return count
    
            


if __name__ == "__main__":
    '''Use python exam_test.py to test your code.
        If you must add your own test code here. '''
    record = "data/pets.txt"
    #get_field_data(record,0,7)
    print(count_pets("data/sample_pets.txt","NAME","Rascal"))
    print(count_pets("data/sample_pets.txt","TYPE","bird"))
    print(count_pets("data/sample_pets.txt","COLOR","yellow"))
    print(count_pets("data/sample_pets.txt","AGE","27"))
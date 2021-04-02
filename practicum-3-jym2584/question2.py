"""
Jin Moon

Write a function, grade_dict, that takes two list arguments: student_ids and grades.
Each grade element in the grades list corresponds to the student in the student_ids
list with the same index.  That is, student_ids[0] earned grades[0], student_ids[1]
earned grades[1], etc

You may assume the two lists are always the same length

The grades in the grades list are numeric and correspond to letter grades with the following
ranges (inclusive):
    A: >= 90 and <= 100
    B: >= 80 and < 90
    C: >= 70 and < 80
    D: >= 60 and < 70
    F: < 60

It is recommended that you write a helper function to convert a numeric grade to the
corresponding letter grade.

Your function should return a dictionary with each letter grade as a key.  The value for
each key will be a list of students who earned that letter grade.

Note: All student ids and grades in this problem are randomly generated. Any resemblance to real
students or grades, past or present, is purely coincidental.
"""

def calculate_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80 and grade < 90:
        return 'B'
    elif grade >= 70 and grade < 80:
        return 'C'
    elif grade >= 60 and grade < 70:
        return 'D'
    elif grade < 60:
        return 'F'

def grade_dict(student_ids,grades):
    students_dict = dict()
    student_grades = {
    'A': [], 
    'B': [], 
    'C': [],
    'D': [],
    'F': []}

    #for i in range(len(student_ids)):
        #student_grades[calculate_grade[grades[

    print(students_dict)
    return student_grades

if __name__ == '__main__':
    student_ids = ['mza2757', 'msq3092', 'wbk2202', 'oqg0697', 'epu3058', 'qqf9768', 'kqx0405', 'lba4698', 'wcw3792', 'iaw8916', 'lfa0636', 'ijk9199', 'jvl5932', 'yik8289', 'dpv0398', 'mko9759', 'hlt7616', 'iij5419', 'ehv3921', 'smv5704']
    grades = [96, 57, 86, 65, 89, 63, 75, 67, 65, 51, 98, 53, 71, 78, 87, 96, 89, 63, 82, 63]
    print(grade_dict(student_ids,grades))
    ''' Your non-test code goes here, if you have any '''


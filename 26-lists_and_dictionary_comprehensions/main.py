numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
# new_list = [new_item for item in list]
print(new_list)


# you can use this with strings as well
name = 'Audrey'
new_name_list = [letter for letter in name]
print(new_name_list)

# python sequences - list, range, string, tuple
# they have a specific order so we can perform list comprehensions

new_range = [n*2 for n in range(1, 5)]
print(new_range)


# conditional list comprehension - only add new items and perform first code if the test passes
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) <= 4]
print(short_names)
# new_list = [item for item in list if test]

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)

# Dictionary comprehension
# new_dict = {new_key:new_value for item in list}  # creating a new dict from a list
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
# creating a new dictionary from another dict

import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

# using loops with a pandas data frame

student_dict = {
    "student": ["James", "Lily", "Harry"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(key)  # column headers
    print(value)  # data in each columns

# loop through rows of a data frame (method from pandas) - iterrows()
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)  # get specific data in a row
    if row.student == "Harry":
        print(row.score)
## Grading Program

# Instructions

# You have access to a database of `student_scores` in the format of a dictionary. The **keys** in `student_scores` are the **names** of the students and the **values** are their exam **scores**.
#
# Write a program that **converts their scores to grades**. By the end of your program, you should have a new dictionary called `student_grades` that should contain student **names** for **keys** and their **grades** for **values**. T**he final version** of the `student_grades` dictionary will be checked.
#
# **DO NOT** write any print statements.
#
# This is the scoring criteria:
#
# > Scores 91 - 100: Grade = "Outstanding"
#
# > Scores 81 - 90: Grade = "Exceeds Expectations"
#
# > Scores 71 - 80: Grade = "Acceptable"
#
# > Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
  student_score = student_scores[student]
  if student_score > 90:
    student_grades[student] = "Outstanding"
  elif student_score > 80:
    student_grades[student] = "Exceed Expectations"
  elif student_score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"



# 🚨 Don't change the code below 👇
print(student_grades)



## Dictionary in List

# Instructions

# You are going to write a program that adds to a `travel_log`. You can see a travel_log which is a **List** that contains 2 **Dictionaries**.
#
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the `travel_log`.
#
# ```
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# ```

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
  travel_log.append({
    "country" : country,
    "visits" : visits,
    "cities" : cities,
  })




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

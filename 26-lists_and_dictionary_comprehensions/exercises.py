# You are going to write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in numbers]
print(squared_numbers)

#
# You are going to write a List Comprehension to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
# DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

numbers2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers2 if n % 2 == 0]
print(result)


# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.

def read_numbers(file_name):
    with open(file_name) as file:
        numbers = file.readlines()
        final_numbers = []
        for n in numbers:
          final_numbers.append(int(n.strip()))
        return final_numbers

numbers_1 = read_numbers("file1.txt")
numbers_2 = read_numbers("file2.txt")

result = [n for n in numbers_1 if n in numbers_2]

print(result)


# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given
# sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result = {word: len(word) for word in words}
print(result)

# You are going to use Dictionary Comprehension to create a dictionary called weather_f that
# takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

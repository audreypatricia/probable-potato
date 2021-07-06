# You are going to write a program that calculates the average student height from a List of heights.
#
# e.g. `student_heights = [180, 124, 165, 173, 189, 169, 146]`
#
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height

average_height = total_height / len(student_heights)

print(int(round(average_height, 0)))


## Highest Score

# Instructions

# You are going to write a program that calculates the highest score from a List of scores.
#
# e.g. `student_scores = [78, 65, 89, 86, 55, 91, 64, 89]`
#
# **Important** you are not allowed to use the max or min functions. The output words must match the example. i.e
#
# > `The highest score in the class is: x`

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0

for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")

## Adding Evens

# Instructions

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
#
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
#
# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

total = 0
for number in range(1, 101):
  if number % 2 == 0 :
    total += number

print(total)

total2 = 0
for number in range(1, 101, 2):
  total2 += number

print(total2)


## FizzBuzz

# Instructions

# You are going to write a program that automatically prints the solution to the FizzBuzz game.
#
# > `Your program should print each number from 1 to 100 in turn.`
#
# >   `When the number is divisible by 3 then instead of printing the number it should print "Fizz".`
#
# >     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#
# >       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0 :
    print("Buzz")
  else:
    print(number)


####### Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

chosen_letters = []
for number in range(1, nr_letters + 1):
  chosen_letters.append(random.choice(letters))

chosen_symbols = []
for number in range(0, nr_symbols):
  chosen_symbols.append(random.choice(symbols))

chosen_numbers = []
for number in range(1, nr_numbers + 1):
  chosen_numbers.append(random.choice(numbers))

password = chosen_letters + chosen_symbols + chosen_numbers
print(''.join(password))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


random.shuffle(password)
print(''.join(password))

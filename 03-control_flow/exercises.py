# Write a program that works out whether if a given number is an odd or even number.

number = int(input("Which number do you want to check? "))
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")


# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#
# It should tell them the interpretation of their BMI based on the BMI value.
#
# - Under 18.5 they are underweight
# - Over 18.5 but below 25 they have a normal weight
# - Over 25 but below 30 they are slightly overweight
# - Over 30 but below 35 they are obese
# - Above 35 they are clinically obese.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you are normal weight")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese")
else:
  print(f"Your BMI is {bmi}, you are clincally obese")


# Write a program that works out whether if a given year is a leap year.
# This is how you work out whether if a particular year is a leap year.
#
# > `on every year that is evenly divisible by 4
# >   **except** every year that is evenly divisible by 100
# >     **unless** the year is also evenly divisible by 400`

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not a leap year.")
  else:
    print("Leap year.")

else:
  print("Not a leap year.")


# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill.
#
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
#
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
#
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == 'S':
  bill += 15
  if add_pepperoni == 'Y':
    bill += 2
elif size == 'M':
  bill += 20
  if add_pepperoni == 'Y':
    bill += 3
else:
  bill += 25
  if add_pepperoni == 'Y':
    bill += 3

if extra_cheese == 'Y':
  bill += 1

print(f"Your final bill is: ${bill}")


# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# > Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# For Love Scores **less than 10** or **greater than 90**, the message should be:
#
# `"Your score is **x**, you go together like coke and mentos."`
#
# For Love Scores **between 40** and **50**, the message should be:
#
# `"Your score is **y**, you are alright together."`
#
# Otherwise, the message will just be their score. e.g.:
#
# `"Your score is **z**."`

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

num_t = name1.count('t') + name2.count('t')
num_r = name1.count('r') + name2.count('r')
num_u = name1.count('u') + name2.count('u')
num_e = name1.count('e') + name2.count('e')


num_l = name1.count('l') + name2.count('l')
num_o = name1.count('o') + name2.count('o')
num_v = name1.count('v') + name2.count('v')


love_score_left = (num_t + num_r + num_u + num_e)
love_score_right = (num_l + num_o + num_v + num_e)
final_score = int(str(love_score_left) + str(love_score_right))

if (final_score < 20) or (final_score > 90):
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif (final_score >= 40) or (final_score <= 50):
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")


### Make a choose your own adventure story
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


step_1 = input("You have hit a crossroad, will you go right or left? ")

if step_1.lower() == "left":
  step_2= input("The path takes you to a rushing stream of river, at them moment the current seems strong, will you swim or wait? ")
  if step_2.lower() == "wait":
    step_3 = input("Sunddenly something appears behind you, there are three large doors, blue, red, yellow. Which will you choose to enter? ")
    if step_3.lower() == "blue":
      print("You have been eaten by beasts. Game over.")
    elif step_3.lower() == "yellow":
      print("You have escaped the clutches of death, you won!")
    elif step_3.lower() == "red":
      print("You have entered into an eternal inferno and died, good news, free BBQ! Game Over.")
    else:
      print("Game Over.")
  else:
    print("You have been attacked by cannabalistic trout. Game Over.")
else:
  print("You have fallen into a black hole and spend infinity there, Game Over.")

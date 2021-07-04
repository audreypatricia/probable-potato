# Control flow

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!") # this is idented so it lives inside the if statement
else:
  print("Come back when you're taller kid!") # this line lives in the else block

 # the indentation is important to show code block

 # Comparison operators
 # > greater than, >= greater than or equal to, < less than, < less than or equal to
 # == equal to, != not equal to
 # = assignment, == Comparison


 # Nested if and elif statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7")
  else:
    print("Please pay $12")
else:
  print("Come back when you're taller kid!")


# Mutiple if statements in succession  - to check mutiple conditions, and if more than one condition is met, all those will be run

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 5

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7")
  else:
    bill = 12
    print("Adult tickets are $12")

  wants_photo = input("Do you want a photo taken? Y or N ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}")

else:
  print("Come back when you're taller kid!")


# Logical operators
# A and B - need both to be true
# C or D - only need one to be true
# not E - reverses a condition

# incorporate logial operators to give people aged 45-55 who are experiencing a midlife crisis free tickets

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 5

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7")
  elif age >= 45 and age <= 55:
    bill = 0
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12")

  wants_photo = input("Do you want a photo taken? Y or N ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}")

else:
  print("Come back when you're taller kid!")

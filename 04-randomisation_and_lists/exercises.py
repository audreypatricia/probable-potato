import random

# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#
# **Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
#
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

num = random.randint(0,1)

if(num == 1):
  print("Heads")
else:
  print("Tails")


# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random
random_number = random.randint(0, len(names) - 1)

print(f"{names[random_number]} is going to buy the meal today!")

# or you can do this .choice()
person_paying = random.choice(names)
print(person_paying)


# Instructions

# You are going to write a program which will mark a spot with an X.
#
# In the starting code, you will find a variable called ```map```.
#
# This ```map``` contains a nested list.
# When ```map``` is printed this is what the nested list looks like:
# ```
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# ```
# In the starting code, we have used new lines (```\n```) to format the three rows into a square, like this:
# ```
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ```
# This is to try and simulate the coordinates on a real map.

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

positionX = int(position[0])
positionY = int(position[1])

map[positionX - 1][positionY - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")


#### create a rock, paper, scissors game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

choices = ['rock', 'paper', 'scissors']
game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

computer_choice = random.randint(0,2)

# rock beats scissors
# paper beats rock
# scissors beats paper

if player_choice >= 3 or player_choice <= -1:
  print(f"You have entered an invalid choice. Game Over")
else:
  print(f"You chose: {game_images[player_choice]}")
  print(f"Computer chose: {game_images[computer_choice]}")
  if (choices[player_choice] == "rock" and choices[computer_choice] == "scissors") or (choices[player_choice] == "paper" and choices[computer_choice] == "rock") or (choices[player_choice] == "scissors" and choices[computer_choice] == "paper"):
    print("You win!")
  elif choices[player_choice] == choices[computer_choice]:
    print("It's a draw")
  else:
    print("You lose")

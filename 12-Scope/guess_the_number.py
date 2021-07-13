#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import art

print(art.logo)

print("Welcome to the Number Guessing Game")

rand_num = random.randint(1,100)
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard' ")

game_playing = True
if level == 'easy':
  attempts = 10
elif level == 'hard':
  attempts = 5

def make_guess(attempts):
  global game_playing
  print(f"You have {attempts} remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess == rand_num:
    print(f"Correct! The number I was thinking about is {rand_num}")
    game_playing = False
  elif guess > rand_num:
    print("Too High")
    return attempts - 1
  elif guess < rand_num:
    print("Too Low")
    return attempts - 1

while game_playing:
  attempts = make_guess(attempts)
  if attempts == 0:
    game_playing = False
    print(f"You lost, you were not able to guess the number {rand_num}")
  else:
    print("Guess again")

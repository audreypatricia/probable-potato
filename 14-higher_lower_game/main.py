from game_data import data
from art import logo
from art import vs
import random
# from replit import clear

print(logo)
data_length = len(data)
score = 0
game_running = True

def getRandomInt():
  return random.randint(0, data_length - 1)

def playGame(a, b):
  a_name = a["name"]
  a_desc = a["description"]
  a_country = a["country"]
  print(f"Compare A: {a_name}, {a_desc}, from {a_country}.")

  print(vs)

  b_name = b["name"]
  b_desc = b["description"]
  b_country = b["country"]
  print(f"Against B: {b_name}, {b_desc}, from {b_country}.")

  answer = input("Who has more followers? Type 'A' or 'B': ")
  return answer

def most_followers(a,b):
  a_followers = a["follower_count"]
  b_followers = b["follower_count"]
  if(a_followers > b_followers):
    return a, 'a'
  else:
    return b, 'b'

def checkAnswer(a, b, answer):
  correct_answer = most_followers(a,b)[1]

  if answer.lower() == correct_answer:
    return True
  else:
    return False

famous_a = data[getRandomInt()]

while game_running:
  famous_b = data[getRandomInt()]
  # error prevention instead randomInts are the same
  while famous_a == famous_b:
    famous_b = data[getRandomInt()]

  player_answer = playGame(famous_a, famous_b)
  # clear() ## these are used in replit to clear the screen
  # print(logo) ## then print logo again once screen is cleared
  if (checkAnswer(famous_a, famous_b, player_answer)):
    score += 1
    print(f"You're right! Current score: {score}")
    famous_a = most_followers(famous_a, famous_b)[0]
  else:
    game_running = False
    print(f"Sorry that's wrong. Final score: {score}")

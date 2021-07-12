import art
import random


print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 10, 10, 10]
players_cards = []
dealers_cards = []
game_running = True

def print_hand(hand):
  card_string = ""
  for card in hand:
    card_string += str(card)
    card_string += ", "
  return card_string

def current_score(hand):
  sum = 0
  for card in hand:
    sum += card
  return sum

def end_game(players_cards, dealers_cards):
  print(f"Your final hand: [{print_hand(players_cards)}], final score: {current_score(players_cards)}")
  dealer_sum = current_score(dealers_cards)
  print(f"Computer's final hand: [{print_hand(dealers_cards)}], final score: {dealer_sum}")
  player_sum = current_score(players_cards)
  check_win(player_sum, dealer_sum)


def check_win(player_sum, dealer_sum):
  if(player_sum > 21 and dealer_sum > 21):
    print("It's a draw")
  elif(player_sum <= 21 and player_sum > dealer_sum or dealer_sum > 21):
    print("You win 😃")
  elif(dealer_sum <= 21 and dealer_sum > player_sum or player_sum > 21):
    print("You lost 😭")
  else:
    print("It's a draw")


playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if playing == 'n':
    game_running = False
else:
    game_running = True

while game_running:
  players_cards.append(random.choice(cards))
  players_cards.append(random.choice(cards))
  print(f"Your cards are [{players_cards[0]}, {players_cards[1]}], current score: {int(players_cards[0]) + int(players_cards[1])}")

  dealers_cards.append(random.choice(cards))
  print(f"Computer's first card: {dealers_cards[0]}")
  dealers_sum = dealers_cards[0]
  while(dealers_sum < 17):
    random_card = random.choice(cards)
    dealers_cards.append(random_card)
    dealers_sum += random_card

  hit = input(f"Type 'y' to get another card, tpye 'n' to pass ")
  grab_card = False

  if hit == 'y':
    grab_card = True
  else:
    grab_card = False

  while grab_card == True:
    print("hello")
    players_cards.append(random.choice(cards))
    card_string = print_hand(players_cards)
    player_sum = current_score(players_cards)

    if player_sum > 21:
      if 11 in players_cards:
        index_11 = players_cards.index(11)
        players_cards[index_11] = 1
      else:
        grab_card = False
    else:
      print(f"Your cards: [{card_string}], current score: {player_sum} ")
      print(f"Computer's first card: {dealers_cards[0]}")
      hit = input(f"Type 'y' to get another card, type 'n' to pass ")
      if hit == 'y':
        grab_card = True
      elif hit == 'n':
        grab_card = False

  end_game(players_cards, dealers_cards)

  playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if playing == 'n':
    game_running = False
  else:
    game_running = True
    players_cards = []
    dealers_cards = []

import random
from hangman_words import word_list
import hangman_art
# import hangman_art import logo, stages

end_of_game = False
lives = 7
chosen_word = random.choice(word_list)

print(hangman_art.logo)

#Create blanks
display = []
for letter in chosen_word:
    display.append('_')

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    guessed_correct = False

    if guess in display:
      print(f"You have already guessed {guess} before")

    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]
            guessed_correct = True

    print(' '.join(display))

    if guessed_correct == False:
      lives -= 1
      print(f"{guess} was not a letter in the word, you lose a life.")
      print(hangman_art.stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win.")

    if lives == 0:
        end_of_game = True
        print("You lose.")

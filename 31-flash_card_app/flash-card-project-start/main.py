from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
french_words = {}
current_word = ""

try:
    data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    french_words = original_data.to_dict(orient='records')
else:
    french_words = data.to_dict(orient='records')


# --------------------- pick random word -------------------------------------------##


def generate_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(french_words)
    flashcard.itemconfig(canvas_image, image=front)
    flashcard.itemconfig(title, text="French", fill="black")
    flashcard.itemconfig(word, text=current_word['French'], fill="black")
    flip_timer = flashcard.after(3000, show_translation)

# ---------------------- show the english translation ------------------------------##

def show_translation():
    flashcard.itemconfig(canvas_image, image=back)
    flashcard.itemconfig(title, text="English", fill="white")
    flashcard.itemconfig(word, text=current_word["English"], fill="white")


def is_known():
    french_words.remove(current_word)
    new_data = pandas.DataFrame(french_words)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()

# ---------------------- UI setup --------------------------------------------------##


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
flashcard = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file="images/card_front.png")
canvas_image = flashcard.create_image(400, 265, image=front)
flashcard.grid(row=0, column=0, columnspan=2)
title = flashcard.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
word = flashcard.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))

back = PhotoImage(file="images/card_back.png")
flip_timer = flashcard.after(3000, show_translation)

# buttons
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)

generate_word()

window.mainloop()


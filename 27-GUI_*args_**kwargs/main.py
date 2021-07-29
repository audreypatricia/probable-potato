import tkinter
from tkinter import *

def button_clicked():
    input_text = input.get()
    my_label["text"] = input_text

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text='I Am a Label', font=('Arial', 24, "bold"))
my_label["text"] = "New Text"  # you can change it like you do with a dictionary, since it uses kwargs
my_label.config(text="New Text")  # another way to change text, by passing it as a keyword argument in .config()
# my_label.pack()  # this places the label on the screen and as a default, on the center of the screen
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
new_button = Button(text="new button")
new_button.grid(column=2, row=0)

# Entry - input
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop()  # this line of the code will always be on the bottom of the code

from tkinter import *


def convert():
    input_text = input.get()
    my_label_2["text"] = round(float(input_text) * 0.3048, 2)


window = Tk()
window.title("Foot to Meter converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# labels
my_label_1 = Label(text='feet', font=('Arial', 24))
my_label_2 = Label(text='0', font=('Arial', 24))
my_label_3 = Label(text='meters', font=('Arial', 24))
my_label_4 = Label(text='is equal to', font=('Arial', 24))
my_label_1.grid(column=2, row=0)
my_label_2.grid(column=1, row=1)
my_label_3.grid(column=2, row=1)
my_label_4.grid(column=0, row=1)

# input
input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
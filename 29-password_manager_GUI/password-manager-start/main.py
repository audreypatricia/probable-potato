from tkinter import *
from tkinter import messagebox  # message box is not a class but a module so we need to import it again from tkinter
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols +  password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = web_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) > 0 and len(username) > 0 and len(password) > 0:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}"
                                                                f" \nPassword: {password} \nis it okay to save?")
        if is_okay:
            with open('data.txt', mode='a') as file:
                file.write(f"{website} | {username} | {password} \n")

        web_input.delete(0, 'end')
        username_input.delete(0, 'end')
        password_input.delete(0, 'end')
    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)


# labels and inputs
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

web_input = Entry(width=35)
web_input.focus()
web_input.grid(column=1, row=1, columnspan=2)
username_input = Entry(width=35)
username_input.insert(0, 'audreypatricia1101@gmail.com')
username_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# buttons
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
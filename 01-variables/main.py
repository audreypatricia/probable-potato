print('Hello World')
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# print out mulitiple lines
print("Hello World!\nHello World!\nThis is my first day with Python")

# string concatenation
print("Hello" + " Audrey");

# in Python, spaces are important, the spaces you add in the code
# it is important in identation - it is important to start code at the beginning of the line

print("Day 1 - String Manipulation")
# \ backslash will help escape the characters
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

input("hi")
# The python input function - to get data from users
print("Hello " + input("What is your name?") + "!")

# print out the number of characters in a user given name
print(len(input("What is your name?")))

# Python variables - store data to refer to it later
name = input("What is your name?")
length = len(name)
print(length)

# variable naming rules
    # some improtant rules
        # make them readable
        # seperate words using underscore
        # numbers cannot be at the begginning of the variables
        # do not use keywords such as "print"/ "input" etc. as variable names - bad practice, very confusing
        # it has to be consistent, the variable name for data stays the same

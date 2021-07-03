# Data Types

#String

#dissect different characters on the word
print("Hello"[0])

"123"
#still a string because it is in ""

#Integer - numbers with no deciman places

print(123 + 345)

number = 123_456_789
# the computer will remove the underscores, but this helps us read it better

# Float - numbers with decimal places

print(3.1459)

# Boolean - 2 possible values True / False
print(True)
print(False)
print(2 == 2)

# type function - to investigate what data types you are dealing with
num_char = len(input("What is your name?"))
print(type(num_char))
# print("You name has " + num_char + " characters.") #this will cause a type error you cannot concatenate a num to a string

# type will print out the data type of the data
# to turn num_char into a string
new_num_char = str(num_char)
print("You name has " + new_num_char + " characters.")

#change to float
print(70 + float("100.5"))
# result 170.5

#Mathematical operatos

print(7 - 3)
print(3 * 2)
print(6 / 3)
# with division you will always get a Float
print(2 ** 2)
# 2 pow 2 = 4

# These operators for the PEMDAS rule
# the order of priority is
# ()
# **
# * /
# + -


# Rounding numbers
print(round(2.666666))
# floor division
print(8 // 3)
# will result in 2 and an integer data type

result = 4 / 2
result /= 2
print(result)
# result = 1

# using f-String - it will do all the type conversion
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#FileNotFound

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdfsdf"])  # this will be ignored as an error, cause in the except we just create a new file
# except:  # except clause will ignore all errors
#     # if there is an error
#     print("there was an error")
#     # put alternative here
#     open("a_file.txt", mode="w")


# # use specific exceptions to catch specific errors
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("something")
# except KeyError:
#     print("That key does not exist")
#
# # # can also use the error
# # except KeyError as error_message:
# #     print(f"THe key {error_message} does not exist")
#
# else:  # no exceptions thrown the code jumps here
#     content = file.read()
#     print(content)
# finally:  # will run last always
#     file.close()
#     print("file was closed.")
#     # you can raise your own exceptions
#     raise TypeError("This is an error I made up")  # this is what will crash your code

# when to use a "raise" when some things that the users input does not make sense
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 metres")

bmi = weight/ height ** 2
print(bmi)
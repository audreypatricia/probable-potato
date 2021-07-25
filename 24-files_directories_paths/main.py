file = open("my_file.txt")
contents = file.read()
print(contents)

# if there is an open file we need to close it, because it takes up the computer's resources
file.close()

# this way we do not need to remember to close the file, the with keyword will help us close the file when we are no
# longer using it

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(content)

with open("my_file.txt", mode='a') as file2:
    file2.write("\nNew text.")
    # mode 'w' - this will replace all the text in the current text and write this
    # change mode to 'a' for append - to add instead of delete

with open('new_file.txt', mode='w') as file3:
    file3.write("New file.")
    # if we are in the write mde and the file does not exist, the write function creates a new file with the
    # specified name


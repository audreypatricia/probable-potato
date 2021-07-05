import random # Python module - each is responsible for specific bits
import my_module # import contents from this module

random_integer = random.randint(1,10)
print(random_integer)

print(my_module.pi)

random_float = random.random()
print(random_float * 5) # * 5 to print out a number between 0 and 5

# Lists

fruits = ["Apple", "Pear", "Oranges"]
print(fruits[0])
print(fruit[-1]) # this will return "Orange"

# change contents of the list
fruits[0] = "Watermelon"

# adding items to the end
fruits.append("Mango")

# For more look at the python list documentation

fruits.extend("Banana", "Cherries", "Grapes") # extend appends a whole list of items into the list

#Nested Lists
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

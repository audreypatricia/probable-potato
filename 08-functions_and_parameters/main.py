# functions with inputs

# def my_function(something):
#     #Do this with something
#     #then do this
#
# invoke the function
# myfunction(pass_into_something)

def greet():
  print("hello")
  print("world")
  print("bye")

greet()

# function with input
def greet_with_name(name):
  print(f"Hello {name}")

greet_with_name("Audrey")


# functions with more than 1 input

def greet_with(name, location):
  print(f"Hello {name} ")
  print(f"What is it like in {location}")

# positional arguments - give arguments in the order of parameters
greet_with("Audrey", "Sydney")

# Keyword arguments - so you can give arguments in a differen order from parameters
greet_with(location= "Gold Coast", name= "Michelle")

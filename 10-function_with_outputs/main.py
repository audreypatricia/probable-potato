# Functions with outputs

def my_function():
    result = 3 * 2
    return result

# the output of this function is result - when we run this, we get the result (output) = 6
output = my_function() # output will store 6

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return(f"{formated_f_name} {formated_l_name}")

# using the return keyword to output something from a function
# after the return keyword the functions stops and exits
print(format_name("audrey", "patricia"))

def format_name2(f_name, l_name):
    """ Take a first and last name and format it to return the title case version of the name"""
    if format_name = '' or format_l_name = '':
        return("inputs not filled")
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return(f"{formated_f_name} {formated_l_name}")

# use three """ text text """ to create a document string - to document functions and say what your code does

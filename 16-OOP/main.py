# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('coral')
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
# creating a new table object
table = PrettyTable()
# using methods to work with the table object and add columns
table.add_column("Pokemon name", ['Pikachu', 'Squirtle', "Charmander"])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
# changing the table attribute to make it left align
table.align = 'l'
print(table)
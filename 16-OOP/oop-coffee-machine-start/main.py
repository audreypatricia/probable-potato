from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
print(coffee_machine.report())
menu = Menu()
cash_register = MoneyMachine()
machine_on = True

while machine_on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == 'report':
        coffee_machine.report()
        cash_register.report()
    elif order == 'off':
        print("Shutting down now...")
        machine_on = False
    else:
        drink_object = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink_object) and cash_register.make_payment(drink_object.cost):
            coffee_machine.make_coffee(drink_object)







MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    }

}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 10.00
}

money = 0


def show_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def take_order():
    machine_on = True
    order = input("What would you like? (espresso/ latte/ cappuccino): ")

    if order == 'off':
        machine_on = False
        return False
    elif order == 'report':
        show_report()
        return True
    elif order == 'refill':
        refill_resources()
        return True
    else:
        if check_resource_availability(order):
            cost = int(MENU[order]["cost"])
            charge_customer(cost, order)
        else:
            print(f"Sorry there is not enough {check_lacking_resource(order)}. Please wait for them to be refilled.")
        return True


def check_resource_availability(order):
    if 'milk' in MENU[order]['ingredients'].keys():
        if resources['water'] > MENU[order]['ingredients']['water'] and resources['coffee'] > MENU[order]['ingredients']['coffee'] and resources['milk'] > MENU[order]['ingredients']['milk']:
            return True
        else:
            return False
    else:
        if resources['water'] > MENU[order]['ingredients']['water'] and resources['coffee'] > \
                MENU[order]['ingredients']['coffee']:
            return True
        else:
            return False


def charge_customer(cost, order):
    print(f"Cost: ${cost}. Please insert coins.")
    quarters = int(input("How many quarters (0.25c)?: "))
    dimes = int(input("How many dimes (0.10c)?: "))
    nickels = int(input("How many nickels (0.05c)?: "))
    pennies = int(input("How many pennies (0.01c)?: "))
    total_cash = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    change = total_cash - cost
    if change >= 0 and resources['money'] > change:
        resources['money'] -= change
        resources['money'] += cost
        use_resources(order)
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {order}. ☕️ Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def use_resources(order):
    resources['water'] -= MENU[order]['ingredients']['water']
    resources['coffee'] -= MENU[order]['ingredients']['coffee']
    if 'milk' in MENU[order]['ingredients'].keys():
        resources['milk'] -= MENU[order]['ingredients']['milk']



def check_lacking_resource(order):
    if resources['water'] < MENU[order]['ingredients']['water']:
        return "water"
    elif resources['coffee'] < MENU[order]['ingredients']['coffee']:
        return "coffee"
    else:
        return "milk"


def refill_resources():
    if resources['water'] < 250:
        resources['water'] += 250
    if resources['coffee'] < 24:
        resources['coffee'] += 75
    if resources['milk'] < 150:
        resources['milk'] += 250


taking_orders = True

while taking_orders:
    taking_orders = take_order()



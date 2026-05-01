# ===============================================================
# Coffee Machine Project - Procedural Programming
# ===============================================================

# Chat GPT Code
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

profit = 0


def print_report():
    """Display current resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources.get('milk', 0)}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(drink):
    """Check if enough ingredients exist."""
    ingredients = MENU[drink]["ingredients"]

    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False

    return True


def process_coins():
    """Calculate total money inserted."""
    print("Please insert coins.")

    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    return quarters + dimes + nickles + pennies


def process_transaction(money_received, drink_cost):
    """Return True if payment successful."""
    global profit

    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = round(money_received - drink_cost, 2)

    if change > 0:
        print(f"Here is ${change} in change.")

    profit += drink_cost
    return True


def make_coffee(drink):
    """Deduct resources and serve coffee."""
    ingredients = MENU[drink]["ingredients"]

    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {drink}. Enjoy!")


# Main Program Loop
machine_on = True

while machine_on:

    choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        print_report()

    elif choice in MENU:

        if check_resources(choice):

            payment = process_coins()
            cost = MENU[choice]["cost"]

            if process_transaction(payment, cost):
                make_coffee(choice)

    else:
        print("Invalid option.")

# ===============================================================
# Coffee Machine Project
# ===============================================================
# Frank's code with Bugs
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
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
def report(dictionary, profit):
    """Converts dictionary into a status report"""
    print(f"Water: {dictionary["water"]}ml\n"
          f"Milk: {dictionary["milk"]}ml\n"
          f"Coffee: {dictionary["coffee"]}g\n"
          f"Money: {profit}$")


def check_resources(coffee):
    """Check resources for every transactions"""
    if resources["water"] >= MENU[coffee]["ingredients"]["water"]:
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
    else:
        print("Sorry there is not enough water.")
        return False
    if resources["milk"] >= MENU[coffee]["ingredients"]["milk"]:
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    else:
        print("Sorry there is not enough milk.")
        return False
    if resources["coffee"] >= MENU[coffee]["ingredients"]["coffee"]:
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        return True
    else:
        print("Sorry there is not enough coffee.")
        return False

def insert_coin(coffee):
    stop_service = check_resources(coffee)
    if stop_service == False:
        return None
    else:
        print("please insert coins.")
        quarters = int(input("how many quarters? ")) * 0.25
        dimes = int(input("how many dimes? ")) * 0.1
        nickels = int(input("how many nickels? ")) * 0.05
        pennies = int(input("how many pennies? ")) * 0.01
        money = quarters + dimes + nickels + pennies
        coffee_cost = MENU[coffee]["cost"]
        is_transaction_successful(money, coffee_cost, coffee)

def is_transaction_successful(money_received, drink_cost, coffee):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round((money_received - drink_cost ), 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee} ☕️. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

# TODO: 1 Print Report
turn_off = False
while not turn_off:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        report(resources,profit)
    elif user_input == "off":
        turn_off = True
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        insert_coin(user_input)
    else:
        print("Psst.")


# ===============================================================
# Coffee Machine Project
# ===============================================================
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
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])









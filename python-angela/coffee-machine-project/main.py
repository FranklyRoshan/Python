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












# ===============================================================
# Python Pizza Project
# ===============================================================
def python_pizza():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M or L: ")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")


    bill = 0

    # Pizza
    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    elif size == "L":
        bill += 25
    else:
        print("You typed the wrong inputs.")

    # Pepperoni Topping
    if pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3

    # Cheese Topping
    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}.")
python_pizza()

"""
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Interaction
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: L
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: N
Your final bill is: $28.
 Hint 
Don't change any of the starting code and make sure that the final sentence says "Your final bill is: $." including the full stop and the same wording. Otherwise, the tests will not pass.
"""

# ===============================================================
# Optimized version of Python Pizza Project
# ===============================================================
"""
A ternary operator is a one-line conditional expression that returns one value if the 
condition is true and another if it is false.

Normal if-else
---------------
if condition:
    x = a
else:
    x = b

Ternary operator
---------------
x = a if condition else b


Multiple Conditions (Nested Ternary)
------------------------------------
marks = 85

grade = "A" if marks >= 80 else "B" if marks >= 60 else "C"
print(grade)

Multiple Conditions (Nested Ternary)
------------------------------------
if marks >= 80:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C"

"""
def calculate_bill(size, pepperoni, cheese):

    # Base price
    prices = {'S': 15, 'M': 20, 'L': 25,}

    if size not in prices:
        return None

    bill = prices[size]

    #  Pepperoni price
    if pepperoni:
        bill += 2 if size == 'S' else 3

    # Extra Cheese
    if cheese:
        bill += 1

    return bill

def python_pizza():
    print("Welcome to Python Pizza Deliveries!")

    size = input("What size pizza do you want? S, M or L: ").upper()
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
    extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

    bill = calculate_bill(
        size,
        pepperoni == "Y",
        extra_cheese == "Y"
    )

    if bill is None:
        print("Invalid pizza size.")
    else:
        print(f"Your final bill is: ${bill}")

python_pizza()

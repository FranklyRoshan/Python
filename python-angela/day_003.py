# ===============================================================
# If Else
# ===============================================================
def if_else():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    # Comparison operator >= <= == !=
    if height >= 120:
        print("You can ride the rollercoaster.")
    else:
        print("Sorry you have to grow taller before you can ride.")
# Function calling  
if_else()

"""
Condition Check
Learn to use conditionals in Python to check a conditions and tell the computer what to do in each case. e.g.

if <this condition is true>:

    <then execute this line of code>

What if the condition is false?
The else keyword is used to define a block of code that will execute if the condition checked in the if statement is false.

if pigs can fly:

    <Some code that will never execute>

else:

    print("This is real life")

Python Indentation
Understand the importance of indentation in Python as a way to make certain lines of code subsidaries of other lines of code.

e.g.

if 5 > 2: #This is a parent line of code

    print("yes") #this is a child line of code

Comparator Operators
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
== Equal to
!= Not equal to
"""

# ===============================================================
# Modulo
# ===============================================================
def modulo():
    number = int(input("What is the number you want to check? "))

    reminder = number % 2

    if reminder == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
modulo()

"""
The modulo operator gives you the remainder of a division.

6 % 2 #will be 0

6 % 5 #will be 1

6 % 4 #will be 2

PAUSE 1 - What is 10 % 3?
What do you think this will output?

print(10 % 3)

PAUSE 2 - Check Odd or Even
Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".

 Hint 
1. First get the user input using the input() function.
2. Next, convert the input into an int using the int() function.
3. Now store the number in a variable.
4. Use the modulo (%) to check if the user input number can be divided cleanly by 2.
5. Use if/else to check if the result of the modulo check in step 4 is equal to 0 then that input number is even, otherwise it's odd.
"""

# ===============================================================
# Nesting and Elif
# ===============================================================
def nesting_and_elif():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    if height >= 120:
        print("You can ride the rollercoaster")
        age = int(input("What is your age? "))
        if age <= 12:
            bill = 5
            print("Child tickets are $5.")
        elif age <= 18:
            bill = 7
            print("Youth tickets are $7")
        else:
            bill = 12
            print("Adult tickets are $12.")

        wants_photo = str(input("Do you want to have a photo take? Type y for Yes or n for No: "))
        if wants_photo == "y":
            bill +=3

        print(f"Your bill is ${bill}")
    else:
        print("Sorry you have to grow taller before you can ride.")
nesting_and_elif()

"""
You can put if/else statements inside other if/else statements. This is known as nesting. e.g.

if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
if english_score >= 90:
    print("You're good at english)
In this case only when a student has over 90 on maths and english, do they get "You are good at everything".

Note: You can also have if statements that don't have a paired else statement.
"""

# ===============================================================
# Multiple Ifs
# ===============================================================
def multiple_ifs():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    if height >= 120:
        print("You can ride the rollercoaster")
        age = int(input("What is your age? "))
        if age < 12:
            bill = 5
            print("Child tickets are $5.")
        elif age <= 18:
            bill = 7
            print("Youth tickets are $7")
        else:
            bill = 12
            print("Adult tickets are $12.")

        wants_photo = str(input("Do you want to have a photo take? Type y for Yes or n for No: "))
        if wants_photo == "y":
            bill +=3

        print(f"Your bill is ${bill}")
    else:
        print("Sorry you have to grow taller before you can ride.")
multiple_ifs()

"""
You can write as many if statements as you need to check for different conditions that are unrelated to each other. Compare the code blocks below:

# If/elif/else
if <condition 1 is true>
    <do A>
elif <condition 2 is true>
    <do B>
else
    <do C>
# Nested if statements
if <condition 1 is true>
    <do A>
    if <condition 2 is true>
        <do B>
        if <condition 3 is true>
            <do C>
# Multiple if statements
if <condition 1 is true>
    <do A>
if <condition 2 is true>
    <do B>
if <condition 3 is true>
    <do C>
In the if/elif/else block, only one of A, B, or C can happen, because if/elif/else are mutually exclusive. The first condition has to fail to go into the elif and the elif (or multiple elif) have to fail to go into the else. Condition 2 is only checked if condition 1 is false.

In the nested if statements, A, B and C can all happen, but conditions 1, 2 and 3 must all be true. The computer will only check condition 2 if condition 1 is true.

In the multiple if statements, A, B, and C can all happen. But they are completely independent of each other. C can happen even if A and B don't. Every condition is checked, no matter the result of the others.
"""

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

# ===============================================================
# Logical Operator
# ===============================================================
def logical_operator():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))
    bill = 0

    if height >= 120:
        print("You can ride the rollercoaster!")
        age = int(input("What is your age? "))
        if age < 12:
            bill = 5
            print("Child tickets are $5.")
        elif age <= 18:
            bill = 7
            print("Youth tickets are $7.")
        elif age >= 45 and age <= 55:
            print("Everything is going to be ok. Have a free ride on us!")
        else:
            bill = 12
            print("Adult tickets are $12.")

        wants_photo = input("Do you want a photo taken? Y or N. ")
        if wants_photo == "Y":
            bill += 3

        print(f"Your final bill is ${bill}")

    else:
        print("Sorry, you have to grow taller before you can ride.")
logical_operator()

"""
You can combine different conditions using logical operators.

A and B #Both conditions need to be true
C or D #Only one condition needs to be true
not E #The condition must be false

PAUSE 1 - Age 45 to 55 Modifier
Update the code so that people age 45 to 55 (inclusive of both ages) ride for free. Use logical operators to check that the age is greater than 45, and it's also less than 55.

NOTE: The warning for simplification is just a suggestion. You can consider it and chose it, or you can ignore it. In this lesson I wanted to show you the and, or and not logical operators. So I recommend keeping the original code in case you come back to this lesson for review.
"""

# ===============================================================
# Optimized Logical Operator code
# ===============================================================
def logical_operator():
    print("Welcome to the rollercoaster!")

    height = int(input("What is your height in cm? "))
    if height < 120:
        print("Sorry, you have to grow taller before you can ride.")
        return

    print("You can ride the rollercoaster!")

    age = int(input("What is your age? "))
    bill = 0

    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    # Photo option
    wants_photo = input("Do you want a photo taken? Y or N. ").upper()
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

logical_operator()


# ===============================================================
# Treasure Island Project
# ===============================================================
def treasure_island_project():
    print(r'''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    __________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /______________|_______
    |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    choice1 = input('You\'re at a cross road. Where do you want to go?\n'
                'Type "left" or "right":\n').lower()

    if choice1 == "left":
        choice2 = input('You\'ve come to a lake. '
                        'There is an island in the middle of the lake\n'
                        'Type "wait" to wait for a boat or '
                        'Type "swim" to swim across:\n').lower()

        if choice2 == "wait":
            choice3 = input('You arrive at the island unharmed. '
                            'There is a house with three doors.\n'
                            'One red, one yellow and one blue. '
                            'Which color do you choose?\n').lower()

            if choice3 == "red":
                print("It's a room full of fire. Game Over.")
            elif choice3 == "yellow":
                print("You found the treasure! You Win!")
            else:
                print("You enter a room of beasts. Game Over.")

        else:
            print("You get attacked by an angry trout. Game Over.")

    else:
        print("You fell into a hole. Game Over.")
treasure_island_project()

# ===============================================================
# BMI Calculator
# ===============================================================
def BMI_Calculator():
    weight = float(input("How much do you weigh? (in kg) "))
    height = float(input("What's your height? (in feet) "))

    bmi = weight / (height ** 2)

    if bmi <= 18.5:
        print("Underweight")
    elif bmi > 18.5 and bmi <= 24.9:
        print("Normal")
    elif bmi > 25 and bmi < 30:
        print("Overweight")
    else:
        print("Invalid")
BMI_Calculator()

"""
Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.

Use the flow chart linked here to create the game logic.

Once you've completed the project, you can always extend the game and make it more interesting!

 Hint 
Demo
https://appbrewery.github.io/python-day3-demo/
"""
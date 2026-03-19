# ===============================================================
# Namespaces and scope
# ===============================================================

"""
Local Scope
Variables (or functions) declared inside functions have local scope (also called function scope). They are only seen by other code within the same block of code.

e.g.

def my_function():
    my_local_var = 2
    
# This will cause a NameErrorr
print(my_local_var) 
Global Scope
Variables or functions declared at the top level (unindented) of a code file have global scope. It is accessible anywhere in the code file.

e.g.

my_global_var = 3

def my_function():
    # This works no problems
    print(my_global_var)
"""
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Namespace
potion_color = "Red" # Global Scope
def drink_potion():
    potion_strength = 2 # Local Scope
    print(potion_strength)

drink_potion()
# print(potion_strength)

# ===============================================================
# Block scope
# ===============================================================
"""
Python is a bit different from other programming languages in that it does not have block scope.

This means that variables created nested in other blocks of code e.g. for loops, if statements, while loops etc. don't get local scope. They are given function scope if they are within a function or global scope if they are not.

e.g.

# Accessible anywhere
my_global_var = 1

def my_function():
    # Only accessible within my_function()
    my_local_var = 2
    
for _ in range(10):
    # Accessible anywhere
    my_block_var = 3

"""
game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

# ===============================================================
# Gobal Vars
# ===============================================================
"""
You can force the code allow you to modify something with global if you use the global keyword before you use it.

e.g. This will give you an error

a = 1
def my_function():
    a += 1
    print(a)
But this will work

a = 1
def my_function():
    global a
    a += 1
    print(a)
"""
# Modifying Global Scope

# enemies = 1
#
#
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

enemies = 1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

# ===============================================================
# Global Constant
# ===============================================================

"""
You can define global constants in your code file for easy access. Their job is meant to be "set and forget" so you can use their values but never need to mofy them.

Naming Convention
Global constants are normally declared in ALL_CAPS with a underscore in between.

e.g.

PI = 3.14159
GOOGLE_URL = "https://www.google.com"
"""

PI = 3.14159
GOOGLE_URL = "https://www.google.com"

# ===============================================================
# Prime Number
# ===============================================================

import math

def is_prime(num):
    """Checks whether the input argument is prime number or not"""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True

num = input("Enter a Positive integer number: ")
print(is_prime(num))

# ===============================================================
# Number Guessing Project
# ===============================================================

# Angela's Code
from random import randint
from guess_art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")




game()




"""
# Frank's Code

import random
from guess_art import logo

def guesses():
    user_guess = int(input("Make a guess: "))
    if user_guess > actual_answer:
        print("Too high\n"
              "Guess Again")
    elif user_guess < actual_answer:
        print("Too low\n"
              "Guess Again")
    else:
        print(f"You got it! The answer was {actual_answer}.")

print(logo)
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.")

actual_answer = random.randint(1,100)

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty_level[0] == "h":
    attmepts = 5
    for i in range (1, 6):
        print(f"You have {attmepts} attempts remaining to guess the number.")
        guesses()
        attmepts -= 1
    print("You've run out of guesses. Refresh the page to run again.")
elif difficulty_level[0] == "e":
    attempts = 10
    for i in range (1,11):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guesses()
        attempts -= 1
    print("You've run out of guesses. Refresh the page to run again.")
else:
    print("Invalid entry, Refresh the page to run again.")
"""
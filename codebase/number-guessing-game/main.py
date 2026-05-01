
# ===============================================================
# Number Guessing Project
# ===============================================================

# Angela's Code
from random import randint
from art import logo


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
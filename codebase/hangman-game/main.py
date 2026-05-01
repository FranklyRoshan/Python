# ===============================================================
# Hangman Project
# ===============================================================
import random

from words import word_list
from art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])

"""
Your goal is to build a Hangman game using everything you have learnt about Python programming.

Demo Final Project
https://appbrewery.github.io/python-day7-demo/

The project is split into 5 major steps. In each step, there will be multiple TODOs. Your goal is to go through each todo in order and complete them.

You can view all the todos easily in PyCharm by going to View -> Tool Windows -> TODOs

TODO-1
Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

TODO-2
Ask the user to guess a letter and assign their answer to a variable called guess. Make the String stored in guess lowercase.

 Hint 1 
TODO-3
Check if the letter the user guessed guess is one of the letters in the chosen_word. Loop through each of the letters in the chosen_word and print "Right" if the letter is a match, "Wrong" if it's not.

 Hint 2 
You can loop through Strings the same way you can loop through Lists - by using the `for in` loop. Try Googling: "Loop through strings python"
"""
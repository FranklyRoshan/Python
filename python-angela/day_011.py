# ===============================================================
# CAPSTONE PROJECT - BlackJack Card Game
# ===============================================================
import random
from blackjack_art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()


"""
Chose your difficulty
Normal 😎: Use all Hints below to complete the project.
Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
Expert 🤯: Only use Hint 1 to complete the project.
Our Blackjack Game House Rules
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.

 Hint 1 
Go to this website and try out the Blackjack game:
https://games.washingtonpost.com/games/blackjack/

Then try out the completed Blackjack project here:

https://appbrewery.github.io/python-day11-demo/

 Hint 2 
Read this breakdown of program requirements:
http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

Then try to create your own flowchart for the program.

 Hint 3 
Download and read this flow chart I've created:
https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

 Hint 4 
Create a deal_card() function that uses the List below to return a random card.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

Remember that 11 is the Ace.

 Hint 5 
Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []

 Hint 6 
Create a function called calculate_score() that takes a List of cards as input and returns the sum of all the cards in the List as the score. Google the sum() function to help you do this.

 Hint 7 
Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

 Hint 8 
Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to Google to find the documentation on the Python built-in functions append() and remove().
https://developers.google.com/edu/python/lists#list-methods

 Hint 9 
Call the functioncalculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

 Hint 10 
If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

 Hint 11 
The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

 Hint 12 
Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

 Hint 13 
Create a function called compare() and pass in the user_score and computer_score.
If the computer and user both have the same score, then it's a draw.
If the computer has a blackjack (0), then the user loses.
If the user has a blackjack (0), then the user wins.
If the user_score is over 21, then the user loses.
If the computer_score is over 21, then the computer loses.
If none of the above, then the player with the highest score wins.

 Hint 14 
Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
"""


# ===============================================================
# Optimized CAPSTONE PROJECT - BlackJack Card Game
# ===============================================================
import random
from blackjack_art import logo


def deal_card():
    """Return a random card from the deck."""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)


def calculate_score(cards):
    """Calculate the score of a hand."""
    score = sum(cards)

    # Blackjack
    if score == 21 and len(cards) == 2:
        return 0

    # Handle Ace (11 -> 1)
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)

    return score


def compare(user_score, computer_score):
    """Compare final scores and return result message."""
    if user_score == computer_score:
        return "Draw 🙃"
    if computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    if user_score == 0:
        return "Win with a Blackjack 😎"
    if user_score > 21:
        return "You went over. You lose 😭"
    if computer_score > 21:
        return "Opponent went over. You win 😁"
    if user_score > computer_score:
        return "You win 😃"
    return "You lose 😤"


def play_game():
    print(logo)

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer's turn
    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    user_score = calculate_score(user_cards)

    print("\nFinal Results")
    print(f"Your hand: {user_cards}, score: {user_score}")
    print(f"Computer's hand: {computer_cards}, score: {computer_score}")
    print(compare(user_score, computer_score))


# Game loop
while True:
    play = input("\nDo you want to play Blackjack? (y/n): ").lower()
    if play != "y":
        break

    print("\n" * 20)
    play_game()
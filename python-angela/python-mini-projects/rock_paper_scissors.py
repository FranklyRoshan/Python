
# ===============================================================
# RPS (Rock, Paper, Scissors) Project
# ===============================================================
def rock_paper_scissors():
    import random

    rock = '''
        _______
    ---'   ____)
            (_____)
            (_____)
            (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
                _______)
                _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'    ____)____
                 ______)
            __________)
         (____)
    ---.__(___)
    '''

    rps = [rock, paper, scissors]
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n"))

    if user < 0 or user > 2:
        print("Invalid choice")
    else:
        computer = random.randint(0, 2)
        print("You chose: ")
        print(rps[user])
        print("Computer chose: ")
        print(rps[computer])

        if user == computer:
            print("It's a Draw")
        elif (user == 0 and computer == 2) or \
            (user == 1 and computer == 0) or \
            (user == 2 and computer == 1):
            print("You win!")
        else:
            print("You lose")
rock_paper_scissors()


# ===============================================================
# Optimized version of RPS (Rock, Paper, Scissors) Project
# ===============================================================

import random

def rock_paper_scissors():

    rps = [
        '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        ''',

        '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
        ''',

        '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        '''
    ]

    user = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

    if user not in [0, 1, 2]:
        print("Invalid choice")
        return

    computer = random.choice([0, 1, 2])

    print("You chose:")
    print(rps[user])

    print("Computer chose:")
    print(rps[computer])

    if user == computer:
        print("Draw")
    elif (user - computer) % 3 == 1:
        print("You Win!")
    else:
        print("You Lose!")


rock_paper_scissors()
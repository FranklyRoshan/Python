
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
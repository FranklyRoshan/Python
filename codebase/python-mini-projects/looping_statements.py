# Looping Statements (Iteration Statement)

# ===============================================================
# For Loop
# ===============================================================
def for_loop():
    fruits = ["Apple", "Peach", "Pear"]
    for fruit in fruits:
        print(fruit + " pie")
    print(fruits)


# Function calling
for_loop()

"""
Loops allow us to tell the computer to repeat actions without having to write repeated code. If we wanted the computer to print out 1 through to 100, it would very painful to type a print statement for every number, or even just typing out all the numbers 1 through to 100. Loops allow us to create a rule and the computer can follow it to do a repeated action.

Syntax
for <variable name of each item> in <a List>:
    <do something>
    <do something else> 
PAUSE 1 - Be a Computer
Predict what will be printed from the code below:

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
Indentation
Indentation is very important in Python programming. Every time you see the : symbol used, you need to be careful about the indentation that comes afterwards.

e.g. This code will behave very differently

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print("Hello")
from this code:

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello")
"""


# ===============================================================
# For Loop - Counter-based & Action-based loop
# ===============================================================

def for_loop_Counter_and_action_based():
    # Action Based Loop
    # print "Hello!" 3 times
    for _ in range(3):
        print("Hello!")

    # Linter friendly: Using _ prevents "Unused variables" warnings in tools like pylint

    # Counter Based Loop
    for i in range(3):
        print(f"Curren count: {i}")


for_loop_Counter_and_action_based()


# ===============================================================
# Max & Min Functions
# ===============================================================
def highest_score():
    student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
    print(range(1, 10))

    # total_exam_score = sum(student_scores)
    # print(total_exam_score)

    sum = 0
    for score in student_scores:
        sum += score
    print(sum)

    max_score = 0
    for score in student_scores:
        if max_score < score:
            max_score = score
    print(max_score)

    # Max
    print(max(student_scores))
    # Min
    print(min(student_scores))


highest_score()

"""
Sum
Python has lots of built-in functions to help us work with numbers. One of them helps us calculate the sum (the total). e.g.

student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores) 
But how does sum() work behind the scenes? The code is written by the people who developed Python and it might look something like this:

student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score

print(sum)
PAUSE 1 - Max
There are also a built-in Python methods called max() and min(), which allow you to pass in a List of numbers, and it will give you the highest number or the lowest number.

Your job is to figure out how the Python programmers might have built this functionality using loops and conditionals.

COMPLETE THIS CHALLENGE WITHOUT USING max()
You are given a list of exam scores, and you have to print out the highest score from the List. You will need to use what you have learnt about Lists, For Loops and Conditionals to print out the highest score in the list of student_scores. For example, if the scores were:

8 65 89 86 55 91 64 89
Your code should print

91
"""


# ===============================================================
# For Loop with Range
# ===============================================================
def for_loop_with_range():
    # Range Function with For Loop

    for number in range(1, 11, 2):
        print(number)

    total = 0
    for num in range(1, 101):
        total += num
    print(total)


for_loop_with_range()

"""
The combination of the range() function with the Python For Loop allows us to run a loop for as many times as we wish. Instead of looping through each item in a List, we can loop through a range of numbers.

Range Function
range(1, 10)

This code doesn't do anything by itself. For example, if you tried to print it, it would not give you individual numbers.

But it can be used in conjunction with For Loops. e.g.

for number in range(1, 10):
    print(number)
This will print out each of the numbers 1 - 9. So the range can also be expressed like this:

a <= range(a, b) < b

Where the range of numbers is inclusive of the lower bound but not inclusive of the upper bound.

PAUSE 1 - The Gauss Challenge
Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
"""


# ===============================================================
# FizzBuzz Code
# ===============================================================
def fizzbuzz():
    for number in range(1, 101):
        if (number % 3 == 0) and (number % 5 == 0):
            print("FizzBuzz")
        elif (number % 3 == 0):
            print("Fizz")
        elif (number % 5 == 0):
            print("Buzz")
        else:
            print(number)


fizzbuzz()


# ===============================================================
# Password Generator
# ===============================================================
def password_generator():
    import random

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Easy level

    password = ""
    # for char in range(1,nr_letters+1):
    #     random_letters = random.choice(letters)
    #     password += random_letters
    for char in range(0, nr_letters):
        password += random.choice(letters)
    for char in range(0, nr_symbols):
        password += random.choice(symbols)
    for char in range(0, nr_numbers):
        password += random.choice(numbers)
    print(password)

    # Hard level
    password_list = []

    for char in range(0, nr_letters):
        password_list.append(random.choice(letters))
    for char in range(0, nr_symbols):
        password_list.append(random.choice(symbols))
    for char in range(0, nr_numbers):
        password_list.append(random.choice(numbers))

    print(password_list)
    random.shuffle(password_list)
    print(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is {password}")


password_generator()

"""
The program will ask:

How many letters would you like in your password?
How many symbols would you like?
How many numbers would you like?
The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

Demo
https://appbrewery.github.io/python-day5-demo/

Easy Version
Generate the password in sequence. Letters, then symbols, then numbers. If the user wants

4 letters 2 symbols and 3 numbers then the password might look like this:

fgdx$*924

You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

 Hint 1 
Hard Version
When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:

x$d24g*f9

And every time you generate a password, the positions of the symbols, numbers, and letters are different. This will make the password more difficult for hackers to crack.

The essential skill of a good programmer is using Google to find what you need. Your brain is for thinking, not memorising functions! You will need to Google to solve this project on the hard level. If you get stuck, check the hint below for what to Google.

 Hint 2 
Try googling: "How to shuffle items in a List in Python"
"""
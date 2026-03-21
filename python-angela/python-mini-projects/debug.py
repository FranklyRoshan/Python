# ===============================================================
# Describe the problem
# ===============================================================

"""
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")
"""

def my_function():
    for i in range(1, 20 + 1):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?

"""
class range(stop, /)
class range(start, stop, step=1, /)
The arguments to the range constructor must be integers (either built-in int or any object that implements the __index__() special method). If the step argument is omitted, it defaults to 1. If the start argument is omitted, it defaults to 0. If step is zero, ValueError is raised.

For a positive step, the contents of a range r are determined by the formula r[i] = start + step*i where i >= 0 and r[i] < stop.

For a negative step, the contents of the range are still determined by the formula r[i] = start + step*i, but the constraints are i >= 0 and r[i] > stop.

A range object will be empty if r[0] does not meet the value constraint. Ranges do support negative indices, but these are interpreted as indexing from the end of the sequence determined by the positive indices.

Ranges containing absolute values larger than sys.maxsize are permitted but some features (such as len()) may raise OverflowError.

Range examples:

# list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list(range(0, 30, 5))
# [0, 5, 10, 15, 20, 25]
# list(range(0, 10, 3))
# [0, 3, 6, 9]
# list(range(0, -10, -1))
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
# list(range(0))
# []
# list(range(1, 0))
# []
Ranges implement all of the common sequence operations except concatenation and repetition (due to the fact that range objects can only represent sequences that follow a strict pattern and repetition and concatenation will usually violate that pattern).

start
The value of the start parameter (or 0 if the parameter was not supplied)

stop
The value of the stop parameter

step
The value of the step parameter (or 1 if the parameter was not supplied)

The advantage of the range type over a regular list or tuple is that a range object will always take the same (small) amount of memory, no matter the size of the range it represents (as it only stores the start, stop and step values, calculating individual items and subranges as needed).

Range objects implement the collections.abc.Sequence ABC, and provide features such as containment tests, element index lookup, slicing and support for negative indices (see Sequence Types — list, tuple, range):

# r = range(0, 20, 2)
# r
# range(0, 20, 2)
# 11 in r
# False
# 10 in r
# True
# r.index(10)
# 5
# r[5]
# 10
# r[:5]
# range(0, 10, 2)
# r[-1]
# 18
Testing range objects for equality with == and != compares them as sequences. That is, two range objects are considered equal if they represent the same sequence of values. (Note that two range objects that compare equal might have different start, stop and step attributes, for example range(0) == range(2, 1, 3) or range(0, 3, 2) == range(0, 4, 2).)

Changed in version 3.2: Implement the Sequence ABC. Support slicing and negative indices. Test int objects for membership in constant time instead of iterating through all items.

Changed in version 3.3: Define ‘==’ and ‘!=’ to compare range objects based on the sequence of values they define (instead of comparing based on object identity).

Added the start, stop and step attributes.
"""

# ===============================================================
# Reproduce the bug
# ===============================================================

"""
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])
"""

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

# ===============================================================
# Play Computer
# ===============================================================

year = int(input("What's your year of birth? "))

"""
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
"""

if 1928 <= year <= 1945:
    print("You are a The silent generation")
elif 1946 <= year <= 1964:
    print("You are a Baby Boomer")
elif 1965 <= year <+ 1980:
    print("You are a Gen X")
elif 1981 <= year <= 1996:
    print("You are a millennial.")
elif 1997 <= year <= 2012:
    print("You are a Gen Z.")
elif 2013 <= year <= 2025:
    print("You are a Gen Alpha")
elif 2026<= year <= 2035:
    print("You are a Gen Beta")
else:
    print("Error: Year Out of Range")

# ===============================================================
# Fix the error
# ===============================================================

"""
age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")

"""

age = 0
try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have types in a invalid number. \n" 
    "Please try again with a numerical number such as 123.")

if age >= 18:
# print(f"You can drive at age {age}.")
    print(f"You can drive at age {age}.")
elif age != 0 and 1 <= age  <= 18:
    print(f"You can't drive at age {age}.")
else:
    print("Enter a positive integer age value.")


# ===============================================================
# User Print
# ===============================================================

"""
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))

print(f"Total no. of pages: {pages}")
print(f"Total no. of wards per page: {word_per_page}")
total_words = pages * word_per_page
print(total_words)
"""
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))

total_words = pages * word_per_page
print(total_words)

# ===============================================================
# Debugger
# ===============================================================

"""
import random

def maths(a,b):
    return a + b

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
"""


import random

def maths(a,b):
    return a + b

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# Break point
# Run Debug
# Step Over
# Step Into
# Step Into My Code
# Step Out

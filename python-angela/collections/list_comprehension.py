# ===============================================================
# List Comprehension
# ===============================================================

# # For Loop
# numbers = [1, 2, 3, 4, 5]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)


# List Comprehension
# new_list = [new_item for item in  list]

# List Comprehension with "list"
# numbers = [1, 2, 3, 4, 5]
# new_list = [n + 1 for n in  numbers]
# print(new_list)

# List Comprehension with "string"
# name = "Franklyn"
# letters_list = [letter for letter in name]
# print(letters_list)

# List Comprehension with "range"
# new_range = [n * 2 for n in range(1,5)]
# print(new_range)

# Conditional List Comprehension
# names = ["Alex", "Ajax", "Ajay", "Beth", "Caroline", "Dave", "Eleanor", "Freddie", "Franklyn"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# ===============================================================
# List Comprehension Exercises
# ===============================================================

# Exercise 01
import math
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [pow(num, 2) for num in numbers]
# squared_numbers = [num ** 2 for num in numbers]
squared_numbers = [math.pow(num, 2) for num in numbers]
print(squared_numbers)

# Exercise 02
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if (num%2 == 0)]
print(result)


# Exercise 03
with open("file1.txt") as file1:
    list1 =  file1.readlines()

with open("file2.txt") as file2:
    list2 =  file2.readlines()

result = [int(num) for num in list1 if num in list2]

print(result)
# ===============================================================
# Dictionary Comprehension
# ===============================================================

"""
new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key, value) in dict.items()}

Conditional Dictionary Comprehension
new_dict = {new_key:new_value for (key,  value) in dict.items() if condition}
"""
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(0,100) for student in names}
passed_student = {student:score for (student,score) in students_scores.items() if score >= 60}
# print(passed_student)

# Exercise 01
# Dictionary Comprehension
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
# print(result)

# Dictionary Comprehension with regex (regular expression)
import re
# Split the sentence using regex to keep only words
words = re.findall(r'\b\w+\b',sentence)
result = {word:len(word) for word in words}
# print(result)

# Exercise 02
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {key:((temp * 9/5) + 32) for (key,temp) in weather_c.items()}
# print(weather_f)

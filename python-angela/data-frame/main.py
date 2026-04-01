# ===============================================================
# NATO Phonetic Alphabet
# ===============================================================
import pandas
"""
Data Frame comprehension
new_dict = {new_key:new_value for (index, row) in df.iterrows()}

Conditional Data Frame Comprehension
new_dict = {new_key:new_value for (index, row) in df.iterrows() if condition}
"""

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a  word: ").upper()
word_list = [phonetic_dict[letter] for letter in word]
print(word_list)

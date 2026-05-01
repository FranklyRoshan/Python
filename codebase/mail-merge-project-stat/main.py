# ===============================================================
# Mail Merge 
# ===============================================================

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./mail-merge-project-stat/Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

with (open("./mail-merge-project-stat/Input/Letters/starting_letter.txt") as letter_file):
    letter_contents = letter_file.read()
    for name in names:
        stripped_names = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_names)
        with open(f"./mail-merge-project-stat/Output/ReadyToSend/letter_for_{stripped_names}.txt", mode="w") \
            as completed_letter:
            completed_letter.write(new_letter)

"""

Path
Absolute Path: /Python/python-angela/mail-merge-project-stat/Input/Names/invited_names.txt
Relative path: ./mail-merge-project-stat/Input/Names/invited_names.txt

Functions used in this code
The primary difference is that read() reads the entire contents of a file and returns it as a single string, 
whereas readlines() reads the entire file and returns a list of strings, with each element representing a single line. 

1. read(): Returns the whole file content as one string; it can accept an optional argument to read a specific number of 
bytes, but without it, it loads the entire file into memory. 
2. readlines(): Returns a list where each item is a line from the file (including newline characters); like read(), 
it loads the whole file into memory at once, which can be inefficient for very large files. 

3. strip() is a built-in Python string method used to remove unwanted characters from both the beginning and end of a 
string.  By default, it eliminates all leading and trailing whitespace characters, including spaces, tabs (\t), and 
newlines (\n), but you can also specify a set of custom characters to remove. 

4. Python's replace() method returns a copy of the original string with all (or a specified number of) occurrences of a 
substring replaced by a new substring.  It does not modify the original string because Python strings are immutable. 

The syntax is string.replace(old, new[, count]), where:

old: The substring to be replaced (required).
new: The substring to replace old with (required).
count (optional): The maximum number of occurrences to replace; if omitted, all instances are replaced.
"""

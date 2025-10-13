#"Block structuring" or "indenting code"
''' ✅ What is Indentation in Python?
        Indentation in Python refers to the whitespace (usually spaces or tabs) used at the beginning of 
        a line to define blocks of code.

        Unlike many other languages (like C, Java, or JavaScript), Python uses indentation instead of 
        curly braces {} to group statements that belong together.

    🧠 Why Indentation is Important in Python
        It defines the structure of the program.
        It tells Python which statements belong to which block (e.g. inside an if, for, while, def, etc.)
        Incorrect or inconsistent indentation will cause an error.  '''

def if_elif_else():

    score = 80

    if (score >= 90):
        print("Grade A")
    elif (score >= 80):
        print("Grade B")
    elif (score >= 70):
        print("Grade C")
    else:
        print("Grade F")
    
    print ("Evaluation Complete.")

if_elif_else()
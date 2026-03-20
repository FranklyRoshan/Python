# CONTROL FLOW STATEMENT
# Control flow statements decide how the program executes (sequentially, conditionally, or repeatedly).

# Types of Control Flow Statements in Python
'''     1. Conditional Statements (Decision-making)
            Used to make choices in a program.

            if
            if...else
            if...elif...else    '''

# if...elif...else
a = int(input("Enter a number: "))
if(a > 0): 
    print(a , " is Positive")
elif (a == a): 
    print(a, " is Zero")
else:
    print(a, " is Negative")

# match-case (Python’s version of switch)
choice = int(input("Enter a number (1-3): "))

match choice:
    case 1:
        print("You chose one")
    case 2:
        print("You chose two")
    case 3:
        print("You chose three")
    case _:
        print("Invalid choice")

''' 👉 Here,
        match works like switch
        case works like case in C/Java
        _ means "default"'''
    
''''    2. Looping Statements (Iteration)
            Used to repeat code multiple times.

            for loop (definite iteration)
            while loop (indefinite iteration)   '''

# for loop
for i in range(5):
    print(i)

# while loop
n = 3
while n > 0:
    print(n)
    n -= 1

'''     3. Control Transfer Statements
            Used to alter normal flow of loops.

            break → exits loop immediately
            continue → skips current iteration, goes to next
            pass → does nothing (placeholder)   '''

# break
for i in range(5):
    if(i == 3):
        break
    print(i)     # prints 0,1,2

# continue
for i in range(5):
    if(i == 2):
        continue
    print (i)   # skips 2

# pass
for i in range(3):
    pass   # does nothing (placeholder for future code)


''' ✅ Summary Table

        Type	                        Statements	                Purpose
        Conditional	                    if, if-else, if-elif-else	Decision making
        Looping	                        for, while	                Repetition
        Control Transfer (Loop Jump)	break, continue, pass	    Alter loop flow '''
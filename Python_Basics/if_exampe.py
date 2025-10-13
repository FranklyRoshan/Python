x = 5

if x > 3 and x < 6:
    print(f"{x} is between 3 and 6")
    print("This is part of IF")
else:
    print(f"{x} is NOT between 3 and 6")
    print("This is part of ELSE")


# Shortcut in IF Statement
''' >>> number = 5
>>> # Normal IF Statement
>>> if(number%2 == 0):
...     isEven = True
... else:
...     isEven = False
>>> isEven
False
>>> # Shortcut IF Statement in Python
>>> isEven = True if number%2==0 else False
>>> isEven
False
>>> number = 6
>>> isEven = True if number%2==0 else False
>>> isEven
True

>>> # You could be able to do with Boolean
>>> number = 6
>>> isEven = number%2==0
>>> isEven
True
>>> number = 5
>>> isEven = number%2==0
>>> isEven
False
>>> number = 5

>>> # But You can use this to print specific output
>>> isEven = "Yes" if number%2==0 else "No"
>>> isEven
'No'
>>> number = 6
>>> isEven = "Yes" if number%2==0 else "No"
>>> isEven
'Yes'
>>> '''
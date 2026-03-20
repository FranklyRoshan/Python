''' ⚡ What Are Short-Circuit Operators?
    Short-circuit operators are logical operators that stop evaluating as soon as the result is already known.
    In Python, these are:

    Operator	    Meaning	Type
    and	            Logical AND	Short-circuit
    or	            Logical OR	Short-circuit   
    
    🧠 How They Work
    ✅ and Operator

    Stops checking when it finds False
    Because if one condition is False, the whole expression will be False   '''

a = 0
b = 10

if((a != 0) and (b/a > 1 )): # Second part won't run
    print("Condition True")
else:
    print("Condition False")


''' 👉 The second condition (b / a > 1) is not even executed,
    because a != 0 is False — Python knows the whole expression will be False,
    so it short-circuits to save time and prevent an error (like division by zero!).    
    
    ✅ or Operator
    Stops checking when it finds True
    Because if one condition is True, the whole expression will be True '''

x = 5
y = 10

if ((x < y) or (y / 0 == 5)): # Second part won't run
    print("Condition True")
else:
    print("Condition False")

''' 👉 The right side y / 0 == 5 is never evaluated,
    since x < 10 is already True — so Python short-circuits again. 
    
    🧩 Summary Table
    Operator	Stops at	    Example	        Result
    and	        First False	    True and False	False
    or	        First True	    True or False	True

    ⚙️ Why It’s Useful:
    ✅ Saves time (faster execution)
    ✅ Prevents errors (like division by zero)
    ✅ Makes conditional checks efficient'''

''' 
    Operator	    Meaning	Type
    and	            Logical AND	Short-circuit
    or	            Logical OR	Short-circuit   
    
    and
    True and True - True
    True and False - False
    False and True - False
    False and False - False

    or
    True or True - True
    True or False - True
    False or True - True
    False or False - False

    xor (^)
    True ^ True - False
    False ^ False - False
    True ^ False - True
    False ^ True - True

    not

    not True - False
    not False - True    '''

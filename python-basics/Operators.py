# Operators in Python
# Operators are symbols that perform operations on values or variables.

a = 10
b = 5
print(a + b)  # 15
# Here, + is an operator, a and b are operands.

# Types of Operators in Python

# 1. Arithmetic Operators
# Used for mathematical calculations.

a = 10
b = 3

print(a + b)    # Addition → 13
print(a - b)    # Subtraction → 7
print(a * b)    # Multiplication → 30
print(a / b)    # Division (float) → 3.333...
print(a // b)   # Floor Division → 3
print(a % b)    # Modulus (remainder) → 1
print(a ** b)   # Exponentiation → 1000 (10^3)

# 2. Relational (Comparison) Operators
# Compare values and return True/False.

x = 5
y = 10

print(x == y)   # Equal → False
print(x != y)   # Not Equal → True
print(x > y)    # Greater → False
print(x < y)    # Less → True
print(x >= y)   # Greater or Equal → False
print(x <= y)   # Less or Equal → True


# 3. Logical Operators
# Used for combining conditions.

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# 4. Assignment Operators
# Used to assign values.

x = 10
x += 5      # x = x + 5 → 15
x -= 3      # x = x - 5 → 12
x *= 2      # x = x - 3 → 24
x /= 4      # x = x * 4 → 6.0
x %= 4      # x = x / 4 → 2.0
x **=3      # x = x ** 3 → 8.0
x //= 2     # x = x // 2 → 4.0

# 5. Bitwise Operators
# Work at the binary level.

a = 3       # 110 in binary
b = 6       # 011 in binary

print(a & b)    # AND → 2 (010)
print(a | b)    # OR → 7 (111)
print(a ^ b)    # XOR → 5 (101)
print(~a)       # NOT → -7
print(a << 1)   # Left Shift → 12 (1100)
print(a >> 1)   # Right Shift → 3 (011)

''''    a << 1 (Left Shift): Shifts bits of a (110) left by 1 position, filling with 0 on the right → 1100, 
        which is 12. Equivalent to multiplying by 2.    
        a >> 1 (Right Shift): Shifts bits of a (110) right by 1 position, dropping the rightmost bit → 011, 
        which is 3. Equivalent to dividing by 2 (integer division).     ''' 

# 6. Membership Operators
# Check if a value is inside a sequence.

list = [1, 2, 3, 4, 5] # List [Odered, mutable[changeable] collection]

print(2 in list)     # True
print(10 not in list) # True

# 7. Identity Operators
# Check if two objects are the same in memory (not just equal values).

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)      # False (different memory locations)
print(x is z)      # True (same object)
print(x is not y)  # True


''' ✅ Summary

    Operator Type	    Examples
    Arithmetic	        + - * / % ** //
    Comparison	        == != > < >= <=
    Logical	            and or not
    Assignment	        = += -= *= /= %= **= //=
    Bitwise	            `&
    Membership	        in, not in
    Identity	        is, is not  '''
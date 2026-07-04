# --- Rounding Decimals ---

"""
Rounding Decimals
There are primarily five ways of rounding off decimals in NumPy:

truncation
fix
rounding
floor
ceil
"""

"""
Truncation
Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.

Example
Truncate elements of following array:
"""
import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr)

"""
Example
Same example, using fix():
"""
import numpy as np

arr = np.fix([-3.1666, 3.6667])

print(arr)

"""
Rounding
The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

E.g. round off to 1 decimal point, 3.16666 is 3.2

Example
Round off 3.1666 to 2 decimal places:
"""
import numpy as np

arr = np.around(3.1666, 2)

print(arr)

"""
Floor
The floor() function rounds off decimal to nearest lower integer.

E.g. floor of 3.166 is 3.

Example
Floor the elements of following array:
"""
import numpy as np

arr = np.floor([-3.1666, 3.6667])

print(arr)


"""
Ceil
The ceil() function rounds off decimal to nearest upper integer.

E.g. ceil of 3.166 is 4.

Example
Ceil the elements of following array:
"""
import numpy as np

arr = np.ceil([-3.1666, 3.6667])

print(arr)
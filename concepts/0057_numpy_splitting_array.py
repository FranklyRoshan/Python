# --- NumPy Splitting Array ---

"""
Splitting NumPy Arrays
Splitting is reverse operation of Joining.

Joining merges multiple arrays into one and Splitting breaks one array into multiple.

We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
"""
"""
Example
Split the array in 3 parts:
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
# Note: The return value is a list containing three arrays.

"""
If the array has less elements than required, it will adjust from the end accordingly.

Example
Split the array in 4 parts:
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)
# Note: We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above, array_split() worked properly but split() would fail.

"""
Split Into Arrays
The return value of the array_split() method is a list containing each of the split as an array.

If you split an array into 3 arrays, you can access them from the result just like any array element:

Example
Access the splitted arrays:
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

"""
Splitting 2-D Arrays
Use the same syntax when splitting 2-D arrays.

Use the array_split() method, pass in the array you want to split and the number of splits you want to do.

Example
Split the 2-D array into three 2-D arrays.
"""
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)
# The example above returns three 2-D arrays.

"""
Let's look at another example, this time each element in the 2-D arrays contains 3 elements.

Example
Split the 2-D array into three 2-D arrays.
"""
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)
# The example above returns three 2-D arrays.

"""
In addition, you can specify which axis you want to do the split around.

The example below also returns three 2-D arrays, but they are split along the column (axis=1).

Example
Split the 2-D array into three 2-D arrays along columns.
"""
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

"""
An alternate solution is using hsplit() opposite of hstack()

Example
Use the hsplit() method to split the 2-D array into three 2-D arrays along columns.
"""
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)
# Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().


# 1D Array of length 7
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# np.split() will fail if trying to split into 3 equal parts
try:
    np.split(arr, 3)
except ValueError as e:
    print(f"np.split Error: {e}\n")

# np.array_split() works fine, creating sub-arrays of size 2, 2, 3
result = np.array_split(arr, 3)
print("array_split Result:", result)

# 2D Array Splitting
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Split horizontally (by columns)
h_split = np.hsplit(matrix, 3)
print(h_split)

# Split vertically (by rows)
v_split = np.vsplit(matrix, 2)
print(v_split)


"""
numpy.array_split()
This function is more flexible and allows for unequal sub-arrays. 

Flexible Splitting: It adjusts the size of the sub-arrays to accommodate the division, ensuring no error is raised even if the array size is not divisible by the number of sections. 
Syntax: np.array_split(arr, sections, axis=0)
Use Case: Ideal for general-purpose splitting where array sizes may vary or are not multiples of the desired number of splits. 
Specialized Splitting Functions
NumPy also provides convenience functions for specific axes:

np.hsplit(): Splits an array horizontally (column-wise, axis=1). 
np.vsplit(): Splits an array vertically (row-wise, axis=0). 
np.dsplit(): Splits an array depth-wise (axis=2), applicable to 3D or higher arrays
"""

# np.dsplit()
# Create a 3D array: 2 blocks, 3 rows, 4 columns (depth)
arr = np.arange(24).reshape(2, 3, 4)

# Split into 2 equal sub-arrays along the 3rd axis
result = np.dsplit(arr, 2)

# Result contains two arrays of shape (2, 3, 2)
print(result[0].shape)  # Output: (2, 3, 2)
print(result[1].shape)  # Output: (2, 3, 2)

"""
Function	Axis	Dimension Requirement	Description
np.vsplit()	axis=0	    2D+	                Splits vertically (rows)
np.hsplit()	axis=1	    1D+	                Splits horizontally (columns)
np.dsplit()	axis=2	    3D+	                Splits depth-wise (layers)
"""
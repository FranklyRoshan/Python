
for i in range(1,10):
    print(i)
print("Done")

for i in range(1,10): print(i*i)

print("Test")


""" The Python range() function is a built-in function that generates a sequence of integers, commonly used to control loops and iterate over specific ranges of numbers.
 It returns a range object, which is an immutable sequence type that represents a range of integers, but it is not a list itself.
 This object can be iterated over using a for loop or converted into a list using the list() function.

The function can be called in three different ways, depending on the number of arguments provided:

range(stop): Creates a sequence starting from 0, up to (but not including) the specified stop value. For example, range(5) generates the numbers 0, 1, 2, 3, 4.
range(start, stop): Creates a sequence starting from the specified start value, up to (but not including) the stop value. For example, range(2, 6) generates the numbers 2, 3, 4, 5.
range(start, stop, step): Creates a sequence starting from start, up to (but not including) stop, with each subsequent number incremented by the step value. The step parameter is optional and defaults to 1. For example, range(0, 10, 2) generates 0, 2, 4, 6, 8.

A negative step value can be used to create a decreasing sequence, such as range(10, 5, -1) which produces 10, 9, 8, 7, 6.
The range() function is designed to work exclusively with integers; it does not accept floating-point numbers or other data types.
 The stop value is always exclusive, meaning the sequence will not include this number.
 This behavior is consistent across all forms of the function.
 The range object is memory-efficient because it generates numbers on-demand during iteration rather than storing the entire sequence in memory."""
# --- Python Classes and Objects ---

"""
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
"""

"""
Create a Class
To create a class, use the keyword class:

Example
Create a class named MyClass, with a property named x:
"""
class MyClass:
  x = 5

"""
Create Object
Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:
"""
p1 = MyClass()
print(p1.x)

"""
The line p1 = MyClass() instantiates the class, creating a new object (or instance) named p1 based on the MyClass blueprint.

Instantiation: The process of creating a specific copy of a class.
p1: The variable holding the reference to this new object in memory.
MyClass(): The call to the class constructor (which defaults to creating the instance if no __init__ requires arguments).
"""

"""
Delete Objects
You can delete objects by using the del keyword:

Example
Delete the p1 object:
"""
del p1

"""
Multiple Objects
You can create multiple objects from the same class:

Example
Create three objects from the MyClass class:
"""
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# Note: Each object is independent and has its own copy of the class properties.

"""
The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

Example
"""
class Person:
  pass
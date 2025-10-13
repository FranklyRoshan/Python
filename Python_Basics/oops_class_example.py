# Name of the file is module in python 

class Book: # Defines a new class named Book.
    pass
''' The pass statement is a placeholder. It does nothing but allows 
    the class to be syntactically valid even though it's empty. '''

book1 = Book(); # Creates the first instance of the Book class and assigns it to the variable book1.
book2 = Book(); # Creates a second, independent instance of the Book class and assigns it to book2.

print(book1)
print(book2)

''' Prints the string representation of book1. Since no custom __str__ or __repr__ method is defined, 
    Python outputs something like <__main__.Book object at 0x...>, showing the class and memory address.    '''


""" The characteristic language naming convention flexibility or simply a difference in module/class naming rules.

    In Java, if a class is public, the file name must match the class name (e.g., MyClass.java).
    In Python, there is no such requirement — file names and class names are independent.

    Python relies on modules (files) and packages (directories), and while PEP 8 recommends descriptive, lowercase file names (e.g., my_module.py), the class inside can be named anything (e.g., MyClass).

    This reflects Python’s flexible and pragmatic design, unlike Java’s stricter compile-time rules.    """
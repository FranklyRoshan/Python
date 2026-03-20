class Book: # Defines a new class named Book.

    # __init__ is called when an object is created to initialize its attributes.
    def __init__(self, name,copies): 
        ''' Constructor: Defines the initializer method (__init__) that runs when a 
            new Book instance is created. It takes name as a parameter. '''
        self.name = name
        self.copies = copies
    
    
    # __repr__ is called when a string representation of the object is needed for debugging
    def __repr__(self): 
        ''' toString: Defines the __repr__ method, which returns a string representation 
            of the object (used for debugging and print). '''
        return repr((self.name,self.copies))
    
    ''' tuple
        return repr((self.name, self.copies)) returns a string representation of a tuple containing the book's name and copies.

        (self.name, self.copies) creates a tuple with two values.
        repr(...) converts that tuple into a string like ('Advanced Python', 5) — useful for debugging.
        This makes the object’s output clear and unambiguous when printed.  '''

    # set
    # get

book1 = Book("Advance level Program in Data Science"); # Creates the first instance of the Book class and assigns it to the variable book1.
book2 = Book("Advance level Program in Python"); # Creates a second, independent instance of the Book class and assigns it to book2.

print(book1)
print(book2)

''' Prints the string representation of book1. Since no custom __str__ or __repr__ method is defined, 
    Python outputs something like <__main__.Book object at 0x...>, showing the class and memory address.    '''


""" Tuple
    A tuple is an ordered, immutable collection of elements in programming.

    Ordered: Elements have a fixed position (e.g., first, second).
    Immutable: Once created, its contents cannot be changed.
    Syntax: Written with parentheses, e.g., (1, "hello", 3.5).
    Useful for: Grouping related data that shouldn’t change (e.g., coordinates, database records).
    In Python, repr((self.name, self.copies)) returns a string like ('Python Book', 5) — showing the tuple’s contents clearly."""
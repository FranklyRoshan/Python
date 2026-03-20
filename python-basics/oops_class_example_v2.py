class Book: 

    def __init__(self, name,copies): 
        self.name = name
        self.copies = copies

    
    def __repr__(self): 
        return repr((self.name,self.copies))


    # instance methods.
    def increase_no_of_copies(self, how_much):
        self.copies += how_much


    def decrease_no_of_copies(self, how_much):
        self.copies -= how_much
        

book1 = Book("Advance level Program in Data Science", 200); 
book1.increase_no_of_copies(50)

book2 = Book("Advance level Program in Python", 500); 
book2.decrease_no_of_copies(50)

print(book1)
print(book2)

''' The code defines instance methods.

    Specifically:

    increase_no_of_copies and decrease_no_of_copies are mutator methods (or setters) that modify the object's state.
    They take self (the instance) and a parameter, then update the instance attribute copies.
    Calling book2.decrease_no_of_copies(50) invokes the method on the book2 instance, reducing its copies by 50.'''
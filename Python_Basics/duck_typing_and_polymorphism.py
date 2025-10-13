# Duck Typing
class MarioGame:

    def up(self): print("Jump Up")

    def down(self): print("Goes into the hole")

    def left(self): pass

    def right(self): print("Go Forward")

class ChessGame:

    def up(self): print("Move Forward")

    def down(self): print("Move Backward")

    def left(self): print("Move Left")

    def right(self): print("Move Right")

games = [ChessGame(), MarioGame()]

for game in games:
    game.up()
    game.down()
    game.right()
    game.left()


# Duck Typing Simple Example:
class Test1:
    def method(self): print("Test1")

class Test2:
    def method(self): print("Test2")

tests = [Test1(), Test2()]

for test in tests:
    test.method()

''' 🦆 Duck Typing

        Definition:

        “If it walks like a duck and quacks like a duck, it’s a duck.”

        In Python, duck typing means that the type or class of an object is less important than the methods it defines.
        You don’t care what the object is, only that it behaves like what you expect.

        In simpler words:

        You can pass any object to a function — as long as it has the required methods or attributes, it will work.'''

class Duck:
    def quack(self):
        print("Quack! Quack!")

class Dog:
    def quack(self):
        print("I'm pretending to be a duck — Woof!")

def make_it_quack(thing):
    thing.quack()

duck = Duck()
dog = Dog()

make_it_quack(duck)  # Quack! Quack!
make_it_quack(dog)   # I'm pretending to be a duck — Woof!

''' Explanation:
    The function make_it_quack() doesn’t care if the object is a Duck or a Dog.
    It only expects the object to have a method called quack().
    That’s duck typing — “if it quacks like a duck…”    '''

""" # Polymorphism
    from abc import ABC, abstractmethod

    class GamingConsole(ABC):
        
        @abstractmethod
        def up(self):   pass

        @abstractmethod
        def down(self): pass

        @abstractmethod
        def left(self): pass

        @abstractmethod
        def right(self): pass

    class MarioGame(GamingConsole):

        def up(self): print("Jump Up")

        def down(self): print("Goes into the hole")

        def left(self): pass

        def right(self): print("Go Forward")

    class ChessGame(GamingConsole):

        def up(self): print("Move Forward")

        def down(self): print("Move Backward")

        def left(self): print("Move Left")

        def right(self): print("Move Right")

    # Polymorphism 
    games = [ChessGame(), MarioGame()]

    for game in games:
        game.up()
        game.down()
        game.right()
        game.left() """

''' ⚖️ Difference Between Duck Typing and Polymorphism
        Feature	        Duck Typing	                                                                        Polymorphism
        Meaning	        Focuses on behavior (methods) rather than the type of object.	                    Allows the same method name to behave differently for different classes.
        Key Idea	    “If it walks like a duck and quacks like a duck, it’s a duck.”	                    “One interface, many implementations.”
        Type Checking	Type of object is not checked; only the presence of method matters.	                Usually involves objects from different classes implementing the same method name.
        Example         Use	You can pass any object to a function as long as it has the required methods.	You can call the same method (speak(), move(), etc.) on different class objects.
        Depends On	    Dynamic typing — method existence at runtime.	                                    Inheritance or method overriding, though not always required.
        Error Handling	Raises an error only if the expected method/attribute is missing at runtime.	    The compiler/interpreter expects consistent method names across related classes.    '''




''' 🧠 In Short

    Duck Typing → Focus on behavior, not type.  
    “I don’t care who you are, just quack!”

    Polymorphism → Focus on common interface.  
    “Different species, same action — speak differently.”   '''
        
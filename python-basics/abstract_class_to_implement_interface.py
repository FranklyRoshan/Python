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

print("Mario Game Implemenation")
mario = MarioGame()
mario.up()
mario.down()
mario.left()
mario.right()

print("\nChess Game Implementation")
chess = ChessGame()
chess.up()
chess.down()
chess.left()
chess.right()


''' ⚙️ 3. Key Differences
        Feature	                Abstract Class	                                Interface
        Purpose	                For code reusability and base behavior	        For defining a contract that classes must follow
        Methods	                Can have both abstract and concrete methods	    Has only abstract methods (in Java; in Python, abstract-only class simulates this)
        Variables	            Can have instance variables	                    Only constants (in Java)
        Access Modifiers	    Can have public, protected, private methods	    All methods are public (in Java)
        Multiple inheritance	A class can extend only one abstract class	    A class can implement multiple interfaces
        Object creation	        Cannot be instantiated	                        Cannot be instantiated
        Python equivalent	    ABC class with abstract + normal methods	    ABC class with only abstract methods
        
        💬 In Simple Words:
        🧩 Abstract class → “Base class with partial implementation.”
        🧩 Interface → “Blueprint — only method declarations, no implementation.”'''

''' 🧠 1. Abstract Class

        An abstract class is a class that can have both abstract and concrete methods.

        Abstract method → declared but not defined (no body)

        Concrete method → has a full implementation

        You cannot create an object of an abstract class.
        It is meant to be inherited by child classes.   '''

""" from abc import ABC, abstractmethod

    class Animal(ABC):  # Abstract class
        @abstractmethod
        def make_sound(self):  # Abstract method
            pass

        def breathe(self):  # Concrete method
            print("All animals breathe.")

    class Dog(Animal):
        def make_sound(self):
            print("Bark!")

    dog = Dog()
    dog.make_sound()
    dog.breathe()   """


''' 🧩 2. Interface

        Python doesn’t have a keyword interface like Java,
        but we can simulate interfaces using abstract classes that contain only abstract methods.

        In Java, however:

        An interface is a contract — it contains only abstract methods (and constants).

        A class implements an interface to provide functionality for those methods. '''

""" from abc import ABC, abstractmethod

    class Shape(ABC):  # behaves like an interface
        @abstractmethod
        def area(self):
            pass

        @abstractmethod
        def perimeter(self):
            pass

    class Circle(Shape):
        def area(self):
            print("Calculating area...")

        def perimeter(self):
            print("Calculating perimeter...")

    circle = Circle()
    circle.area()
    circle.perimeter()    """


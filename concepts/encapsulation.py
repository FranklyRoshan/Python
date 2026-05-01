class BookEnhanced:
    def __init__(self, name, copies):
        self.name = name
        self.copies = copies

    @property
    def copies(self):
        print('getter called')
        return self.__copies
    
    @copies.setter
    def copies(self, copies):
        print('setter called')
        if (copies > 0):
            self.__copies = copies

microservices = BookEnhanced('Microservice', 5)
print(microservices.copies)

microservices.copies = 10
print(microservices.copies)


class Person:
    def __init__(self, name):
        self.name = name  # public attribute

p = Person("Frank")
print(p.name)     # Access directly
p.name = "Richards" # Modify directly
print(p.name)


''' 🐍 In Python

    Python doesn’t force you to write getters/setters because:

    All attributes are public by default.

    Python trusts developers — it follows a philosophy called
    “We are all consenting adults here.”
    (You’re expected to use attributes responsibly.)'''

''' ⚙️ So, Is Encapsulation Missing?
    ❌ No — encapsulation exists in Python, but it’s implemented differently.
    You can make an attribute private by prefixing it with two underscores (__):    '''

""" class Person:
        def __init__(self, name):
            self.__name = name   # private variable

    p = Person("Frank")
    print(p.__name)   # ❌ Error: AttributeError    """

''' ✅ Proper Encapsulation in Python (using @property)

Python provides a modern, elegant way — the @property decorator.

Example:

class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):          # acts as getter
        return self.__name

    @name.setter
    def name(self, new_name): # acts as setter
        if len(new_name) < 3:
            raise ValueError("Name too short!")
        self.__name = new_name

p = Person("Frank")
print(p.name)     # calls getter
p.name = "Richards" # calls setter
print(p.name)


✅ So Python achieves encapsulation but in a cleaner and more Pythonic way, without cluttering the class with get_ and set_ methods.

 '''

''' 📘 Summary Table
    Feature	        Java	                                Python
    Encapsulation	Uses private + getters/setters	        Uses name mangling __var and @property
    Getter/Setter	Must define manually (getX, setX)	    Done using @property
    Access Control	Compiler enforced	                    Convention-based (“we trust you”)
    Philosophy	    Strict OOP enforcement	                Simplicity & readability    '''
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return repr((self.name))
    
# Inheritance
class Student (Person):
    def __init__(self, name, college_name):
        super().__init__(name)
        self.college_name  = college_name
    
    def __repr__(self):
        return repr((super().__repr__(), self.college_name))
    

person = Person("Frank")
student = Student("Frank", "Francis Xavier Eng. College.")

print(person)
print(student)

# IS A Relationship
""" Inheritance in programming is a mechanism that allows one class (called the child class or subclass) 
    to acquire the properties and behaviors (fields and methods) of another class (called the parent class or superclass).

    The “IS-A” relationship in programming refers to the relationship established through inheritance — 
    it means one class is a type of another class.

    🧠 In simple words:
        If class B inherits from class A, we say:

        B IS-A A
        That means B is a specialized version of A — it inherits all of A’s behavior and can add its own.

    It’s one of the core concepts of Object-Oriented Programming (OOP) — along with encapsulation, 
    polymorphism, and abstraction.

    🧠 In simple terms:
    Inheritance means “reusing code” — you create a new class based on an existing one. 
    
    🔍 Types of Inheritance (in Java):

    Single Inheritance – One class inherits another.
    (e.g., Dog extends Animal)

    Multilevel Inheritance – A class inherits a class that itself inherits another.
    (e.g., Puppy → Dog → Animal)

    Hierarchical Inheritance – Multiple classes inherit the same base class.
    (e.g., Dog, Cat, Cow all inherit Animal)

    ⚠️ Java does not support multiple inheritance using classes (to avoid ambiguity),
    but it can be achieved using interfaces.    """
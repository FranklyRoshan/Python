class TerrestrialOrganism:
    def walk(self):
        print("walk")

class AquaticOrganism:
    def swim(self):
        print("swim")

class Amphibian(TerrestrialOrganism, AquaticOrganism):
    pass

frog = Amphibian()

frog.walk()
frog.swim()

''' ✅ Every class in Python inherits from the object class.
    This concept is called Classical Inheritance or more precisely Single Root Inheritance. 
    
    🧠 Explanation:
    In Python 3, all classes (whether you specify it or not) automatically inherit from the built-in base 
    class called object.    
    
    You’ll see methods like:

    '__class__', '__init__', '__str__', '__repr__', '__eq__', ...


    👉 All these come from the object class — the root of all classes.

    🧾 So to complete your sentence:

    Every class in Python inherits from the object class.
    This is called Single Root Inheritance (or sometimes Universal Base Class Inheritance). '''
class Player:
    count = 0   # <-- Class variable (shared by all instances)

    def __init__(self, name):
        self.name = name
        Player.count += 1   # Increment shared count
    
    @staticmethod
    def get_count():
        return Player.count

messi = Player('Messi')
ronaldo = Player('Ronaldo') 

print(messi.get_count())
print(ronaldo.get_count())
print(Player.get_count())


''' 🧩 What is a Static Method in Python?

    A static method is a method that belongs to the class, not to any particular object (instance).
    It doesn’t depend on instance-specific data (like self) or class-specific data (like cls).

    It’s defined using the @staticmethod decorator. '''


''' ⚖️ Comparison: Static vs Class vs Instance Methods
    Type	            Decorator	    First Parameter	    Can Access	                            Called Using
    Instance Method	    none	        self	            Instance & Class variables	            Object
    Class Method	    @classmethod	cls	                Class variables only	                Class or Object
    Static Method	    @staticmethod	None	            Neither (unless accessed explicitly)	Class or Object'''


""""    class Example:
        class_var = 10

        def instance_method(self):
            print("Instance method", self.class_var)

        @classmethod
        def class_method(cls):
            print("Class method", cls.class_var)

        @staticmethod
        def static_method():
            print("Static method", Example.class_var)

    Example().instance_method()
    Example.class_method()
    Example.static_method() """
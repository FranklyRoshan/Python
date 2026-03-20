class Country:

    def __init__(self): # self/this  "def __init__(self):"
        print("Constructor")

    # In Python, Overloading of Method or Constructor will cause error
    # def __init__ (self, name):
    #     self.name = name
    #     print("Overloading Constructor")
    # TypeError: Country.__init__() missing 1 required positional argument: 'name'
    
    def instance_method(self):  # self/this "def instance_method(self):"
        print("Instance Method")


india = Country()
india.instance_method(); # self

''' In Python, defining multiple methods or constructors with the same name (like __init__) 
    causes the last one to overwrite the previous ones — this is called method overriding, 
    not overloading.

    Python does not support method overloading (having multiple methods with the same name but 
    different parameters) in the way languages like Java do. Instead, you handle different cases 
    using default arguments or variable-length arguments (*args, **kwargs).'''


"""  # Default keyword
    def  __init__ (self, name="Default"):
        self.name = name
        print()

default_country = Country()
india = Country("India")

    The __init__ method is a constructor that initializes object attributes.

    def __init__(self, name="Default"): Defines a constructor with a default parameter name. If no name is provided, it uses "Default".
    self.name = name: Assigns the passed or default name to the instance.
    print() : Prints an empty line (does nothing visible).
    When creating objects:

    default_country = Country(): Uses the default name "Default".
    india = Country("India"): Uses the provided name "India".
    Each object gets its own name value.    """
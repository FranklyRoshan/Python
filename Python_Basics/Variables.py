#Conceptual Types of Variables (by usage)

# Global variable
name = "python"

def greet():
    # Local Variable
    message = "Hello"
    print(message + " " + name)

greet()

def data_type():
    ''''    Python Data Types
            In Python, data types are classes, and variables are objects (instances of these classes).  '''

    # 1. Numeric Type
    a = 10      # int (whole number)
    b = 3.14    # float (decimal number)
    c = 2 + 2j  # complex number (real part + imaginary part)

    # 2. Sequence Types
    name = "Frank"                  # String (text inside quotes)
    numbers =  [0, 1, 2, 3, 4, 5]   # List [Odered, mutable[changeable] collection]
    coords = (10, 20)               # tuple (Odered, immutable (Unchageable) collection)

    # 3. set Types
    s = {0, 1, 2, 3, 3}         # {1, 2, 3} # set → Unordered, no duplicate values
    fs = {[ 1, 2, 3]}           # frozenset → Immutable set

    # 4. Mapping Type
    students = {"name": "Frank", "age": 24}     # dict → Key-value pairs

    # 5. Boolean Type
    is_valid = True     # bool → True or False

    # 6. Binary Types
    b = b"hello"                    # bytes → Immutable sequence of bytes
    ba = bytearray([66, 69, 96])    # bytearray → Mutable sequence of bytes
    mv = memoryview(b"hello")       # memoryview → Memory view object of another binary object


    # ✅ Python is dynamically typed, so you don’t need to declare data types explicitly:
    x = 5        # int
    x = "hello"  # str (type changes automatically)  

    ''' Type Casting in Python
        Type casting means converting one data type into another.
        There are two types:    '''
    
    ''' 1. Implicit Type Casting (Type Promotion)
        Done automatically by Python.
        When you combine two different numeric types, Python converts the smaller type → larger type to prevent data loss.  '''

    x = 10          # int
    y = 3.5         # float

    z = x + y       # int + float → float
    print(z)        # 13.5
    print(type(z))  # <class 'float'>
    #  Python promoted int to float automatically.

    ''' 2. Explicit Type Casting (Type Conversion)
        Done manually by the programmer using built-in functions:
            int() → converts to integer
            float() → converts to float
            str() → converts to string
            list(), tuple(), set() → converts to collection types'''
    
    # int → float
    a = 5
    b = float(a)
    print(b)        # 5.0
    print(type(b))  # <class 'float'>

    # float → int
    c = 3.14
    d = int(c)
    print(c)        # 3 decimal part is truncated

    # int → str
    e  = str(100)
    print(e)        # "100"
    print(type(e))  # <class 'str'

    # string → int
    f = int("50")
    print(f + 10)   # 60    

    #  ⚠️ Note: Not all conversions are valid.
    x = int("hello")  # ❌ Error (invalid literal for int)

    ''' ✅ Quick Difference
        Casting Type	Who Does It?	        Example
        Implicit	    Python automatically	int + float → float
        Explicit	    Programmer manually	    int("5"), float("3.14")'''


    ''' What is a Literal in Python?
        A literal is a fixed value that you write directly in your code to represent data.
        It’s the actual value assigned to a variable, not the variable itself.

        Think of it as:
        👉 Variable = Name
        👉 Literal = Value  '''  
    
    x = 10          # 10 is an integer literal
    name = "Frank"  # "Frank" is a string literal
    pi = 3.14       # 3.14 is a float literal

data_type()

def data_types_examples():
    # Types of Data Type
    # 1. Integer type 
    number_of_lessons = 1
    print(f"Today is lesson number: {number_of_lessons}")

    # 2. String type
    topic_name =  "Variables"
    print(f"The topic is: {topic_name}")

    # 3. Floating-point type
    completion_rate = 0.55
    print(f"My progress is: {completion_rate * 100}%")

    # You can check the type using the built-in type() function
    print(f"The type of 'topic_name' is: {type(topic_name)}")


    # Example code
    # 1. Variable Assignment
    # Assign a string (text) to the 'name' vairable
    my_name = "Frank"

    # Assign an integer (whole number) to the 'age' variable
    my_age = 23

    # Assign another integer to the 'favorite_number' variable 
    favorite_number = 7

    # 2. Printing the output
    # We use an f-string (formatted string literal) for clean and easy insertion of variable into text .
    # The variables  inside the curly braces {} are automatically converted to strings.
    output_Sentence = f"Hello! My name is {my_name}, I'm {my_age} years old, and my favorite number is {favorite_number}."

    # Print the final sentence
    print(output_Sentence)

data_types_examples()



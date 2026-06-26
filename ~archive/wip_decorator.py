""" 🧩 What is a Decorator in Python?

A decorator is a special function that modifies or enhances another function or method —
without changing its actual code.

It’s applied using the @ symbol above the function definition.

🧠 In simple words:

A decorator is like wrapping a gift 🎁 —
You add extra features (logging, checking, formatting) around an existing function,
without touching what’s inside the box.

🧮 Basic Example
def greet():
    print("Hello, Frank!")

greet()  # Output: Hello, Frank!


Now let’s add a decorator that prints something before and after greeting.

def my_decorator(func):
    def wrapper():
        print("Before greeting 👋")
        func()
        print("After greeting 👋")
    return wrapper

@my_decorator
def greet():
    print("Hello, Frank!")

greet()

🧾 Output:
Before greeting 👋
Hello, Frank!
After greeting 👋


Here:

@my_decorator → tells Python to pass the function greet into my_decorator()

The decorator returns a new function (wrapper) that adds extra behavior

⚙️ Equivalent Without @ Syntax
greet = my_decorator(greet)
greet()


✅ Works the same — the @ symbol is just a shortcut.

🧱 Decorators with Arguments

If your function has parameters, your wrapper should also accept them:

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        func(*args, **kwargs)
        print("After call")
    return wrapper

@my_decorator
def add(a, b):
    print(a + b)

add(5, 7)


Output:

Before call
12
After call

🧰 Built-in Decorators

Python has some built-in decorators, especially for classes:

Decorator	Description
@staticmethod	Defines a static method (no self or cls)
@classmethod	Defines a class method (uses cls)
@property	Converts a method into a read-only attribute
⚡ Real-World Example

Let’s say you want to log every time a function runs:

def logger(func):
    def wrapper():
        print(f"Running {func.__name__}()...")
        func()
    return wrapper

@logger
def say_hi():
    print("Hi, Frank!")

say_hi()


Output:

Running say_hi()...
Hi, Frank!

🧠 Summary
Concept	Meaning
Decorator	Function that modifies another function’s behavior
@ symbol	Shortcut for applying a decorator
Wrapper	Inner function that adds new logic
Common uses	Logging, authentication, timing, validation, etc.   """
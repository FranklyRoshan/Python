# Python Decorator Function
import time

def delay_decorator(function):
    """
    A Python decorator is a design pattern that allows you to modify or extend the behavior of
    a function without permanently changing its actual source code.

    The Core ConceptIn Python, functions are first-class objects.
    This means functions can be:
        1. Assigned to variables.
        2. Passed as arguments to other functions.
        3. Returned from other functions.
    A decorator takes advantage of this by accepting a target function, wrapping it inside
    a new helper function, and returning that new wrapper.
    """
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after
    return wrapper_function

def say_hello():
    print("Hello!")

@delay_decorator
def say_bye():
    print("Bye!")

# decorator_function = delay_decorator(say_bye)
# decorator_function()

say_hello()
say_bye()


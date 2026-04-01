# ===============================================================
# Optional Arguments - *args and **kwargs
# ===============================================================
# Positional Arguments with default value
def series(a, b=2, c=5):
    print(a, b, c)

# series(1)

# ===============================================================
# *args - Unlimited Positional Arguments
# ===============================================================
def args_type(*args):
    print(args)
    print(type(args))

# args_type(1, 2, 3, 4, 5) #return type tuple

def add(*args):
    num_sum = 0
    for n in args:
        num_sum += n
    return num_sum

# print(add(12, 23, 45, 56))

# ===============================================================
# **kwargs - Unlimited keyword Arguments
# ===============================================================

def kwargs_type(**kwargs):
    print(kwargs)
    print(type(kwargs))

# kwargs_type()

def calculate(n, **kwargs):
    print(kwargs)
    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]

        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Tesla")
print(my_car.make)
print(my_car.model)


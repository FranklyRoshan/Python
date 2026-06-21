# Functions can have inputs/functionality/output
# def add(n1,n2):
#     return n1 + n2
#
# def subtract (n1, n2):
#     if n1 > n2:
#         return n1 - n2
#     else:
#         return n2 - n1
#
# def multiply (n1, n2):
#     return n1 * n2
#
# def divide (n1, n2):
#     if n2 == 0:
#         return "Indefinite"
#     else:
#         return n1/n2

# First class objects can be passed around as arguments
# e.g. int/string/float etc.
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
# result = calculate(multiply, 2, 3)
# print(result)

# Nested Function
# def outer_function():
#     print("I'm Outer")
#
#     def nested_function():
#         print("I'm Inner")
#
#     nested_function()
#
# outer_function()

# Function can be returned from another functions
def outer_function():
    print("I'm Outer")

    def nested_function():
        print("I'm Inner")

    return nested_function

inner_function = outer_function()
inner_function()

if __name__ == "__main__":
    print(__name__)


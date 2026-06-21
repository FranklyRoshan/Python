def method_1():
    print("method 1")

class ClassA:
    def class_method_1(self):
        print("class_method_1_method_1")

print(__name__)
if __name__ == '__main__':
    method_1()
    ClassA().class_method_1()


''' 🧠 What is a Module in Python?
    A module in Python is simply a file that contains 
    Python code — such as functions, classes, or variables — that you can reuse in other programs.
    It helps you organize your code and avoid repetition.   '''


'''
🧩 Types of Modules
Type	                Description
Built-in modules	    Predefined in Python (e.g., math, os, sys)
User-defined modules	Created by programmers (like math_tools.py)
External modules	    Installed using pip (e.g., numpy, pandas)
'''
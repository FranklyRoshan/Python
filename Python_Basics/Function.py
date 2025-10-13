''' Functions and Methods
        Functions (or Methods in Object-Oriented Programming like Java/C++) are named blocks of code that 
        perform a specific, reusable task. 
        They are the single most important concept for writing clean, efficient, and manageable programs.

        1. Why Use Functions?
        * Reusability: Write a block of code once, and use it multiple times throughout your program.
        * Modularity: Break a large, complex problem into smaller, simpler, independent tasks.
        * Readability: Give a complex piece of logic a simple, descriptive name (e.g., calculateTax()). '''

# Function Definition with one parameter and a return value

def calculate_area(length, width):
    """"    Calculate the area of a rectangle.   """
    area = length * width
    return area

# Function Call
room_area = calculate_area(10, 5)
print(f"The area is: {room_area}")
    

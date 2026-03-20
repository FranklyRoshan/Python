# While loop: condition checked before execution
def while_loop_type_1():
    number = 0 # condition returns true
    print("To end the loop, enter a negative number.")
    while (number >= 0):
        number = int(input("Enter a number: "))
        print(f"Cube is {number ** 3}")
        
while_loop_type_1()


# Emulate do-while loop: body executes at least once
# "emulating a do-while loop" or "simulating a do-while loop" in Python.
def  while_loop_type_2():
    number = int(input("Enter a number: "))
    number = 0;  
    while (number >= 0):
        print(f"cube is {number ** 3}")
        number = int(input("Enter a number: "))

while_loop_type_2


def while_loop_type_3():
    while True:
        number = int(input("Enter a number: "))
        if number < 0:
            break
        print(f"Cube is {number ** 3}")

while_loop_type_3()


        


a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))

print("Available Choices are: ")
print("1 - Add")
print("2 - Subtract")
print("3 - Divide")
print("4 - Multiply")
print("5 - Remainder")
choice = int(input("Enter choice: "))

if(choice == 1):
    print(f"Result = {a + b}")
elif(choice == 2):
    print(f"Result = {a - b}")
elif(choice == 3):
    print(f"Result = {a / b}")
elif(choice == 4):
    print(f"Result = {a * b}")
elif(choice == 5):
    print(f"Result = {a % b}")
else: 
    print("Invalid choice.")
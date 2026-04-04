# ===============================================================
# catching Exception Error
# ===============================================================
# ----- Types of Errors ------ #
# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key" : "Value"}
# value = a_dictionary{"non_existent_key"}

# IndexError
# fruit_list = ["Apple","Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# ----- try, catch, except, finally Pattern ----- # 

try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "a")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

# ------ Raise your own exception ----- #
print("")
print("BMI Calculation:")
height = float(input("Height (in m): "))
weight = int(input("weight (in kg): "))

if height > 4:
    raise ValueError("Average Human Height should not be over 4 meters")

bmi = weight / height ** 2
print(f"BMI is {bmi}")
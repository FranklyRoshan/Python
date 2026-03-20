# List
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print("List:", fruits)  # ['apple', 'banana', 'cherry', 'date']

# Tuple
coordinates = (10, 20)
# coordinates[0] = 15  # ❌ Error (immutable)
print("Tuple:", coordinates)

# Set
unique_numbers = {1, 2, 3, 2, 1}
unique_numbers.add(4)
print("Set:", unique_numbers)  # {1, 2, 3, 4}

# Dictionary
student = {"name": "Frank", "age": 22, "city": "Chennai"}
student["age"] = 23
print("Dictionary:", student)


''' Feature             List                         Tuple                         Set                              Dictionary
---------------------------------------------------------------------------------------------------------------------------------------------
Definition          Ordered, mutable collection   Ordered, immutable collection  Unordered, unique items          Key-value pair collection
Syntax              [ ]                          ( )                            { }                              {key: value}
Order Maintained    ✅ Yes                        ✅ Yes (Python 3.7+)            ❌ No                            ✅ Yes (Python 3.7+)
Mutability          ✅ Mutable                    ❌ Immutable                    ✅ Mutable                       ✅ Mutable (keys immutable)
Duplicates Allowed  ✅ Yes                        ✅ Yes                          ❌ No                            ❌ No (keys must be unique)
Indexing/Slicing    ✅ Yes                        ✅ Yes                          ❌ No                            ✅ By keys
Access Type         Index-based                   Index-based                    Value-based                      Key-based
Example             [1, 2, 3]                     (1, 2, 3)                      {1, 2, 3}                        {"a": 1, "b": 2}
Use Case            Ordered data storage          Fixed data (constants)          Unique items, fast lookup        Mapped relationships '''
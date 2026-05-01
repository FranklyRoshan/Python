
# ===============================================================
# List of States
# ===============================================================
def list_of_states():
    states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                        "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                        "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana",
                        "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
                        "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
                        "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
                        "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona",
                        "Alaska", "Hawaii"]
    print(states_of_america[0])

    states_of_america[1] = "Pencilvania"

    states_of_america.append("Frankland")

    # states_of_america.extend("")
    print(states_of_america)
list_of_states()

"""
You can create a simple collection of ordered items using a Python list. e.g.

fruits = ["Cherry", "Apple", "Pear"]

or

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

Accessing Items in Lists
You can provide the name of the list then a square bracket and then the item index that you want. e.g.

states_of_america[0]

will give you "Delaware".

Remember that everything computer related, the first number we count with is 0 and never 1. 0, 1, 2, 3 instead of 1, 2, 3 4.

Negative Indices
You can access items in the list counting from the end of the list by using negative whole numbers. e.g.

fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] #this will be "Pear"
Modifying Items
You can use the same syntax to get hold of items in a List to modify it. e.g.

fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"
# fruits will now become ["Orange", "Apple", "Pear"]
Adding Items
You can add items to the end of a List using the append() function. e.g.

fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
# fruits will now become ["Cherry", "Apple", "Pear", "Orange"]
Lists Documentation
You can find the documentation for Python Lists and other List related functions here: https://docs.python.org/3/tutorial/datastructures.html
"""

# ===============================================================
# List Funtions extend() and append()
# ===============================================================

"""
In Python, append() and extend() are both used to add elements to a list, 
but they handle the input differently. 

1. append() - Adds a Single Object 
The append() method adds its argument as a single new element at the end of the list. 

Argument: Any object (number, string, list, etc.).
Result: The list length increases by exactly 1.
Nesting: If you append a list, it becomes a nested list inside the original. 
"""

x = [1, 2, 3]
x.append([4, 5])
# Result: [1, 2, 3, [4, 5]]
# Use code with caution.

"""
2. extend() - Adds Multiple Elements 
The extend() method iterates over its argument and adds each item individually to the end of the list. 

Argument: Must be an iterable (list, tuple, string, set).
Result: The list length increases by the number of items in the iterable.
Nesting: It "flattens" the input, merging the elements into the original list
"""
x = [1, 2, 3]
x.extend([4, 5])
# Result: [1, 2, 3, 4, 5]

# Similarly (+= Operator (In-place Extend))
# y = [4, 5]
# x =+ y
# Result: [1, 2, 3, 4, 5]


# ===============================================================
# Index Error (Array Out of Bound Error)
# ===============================================================
def index_error():
    # states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
    #                      "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
    #                      "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    #                      "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
    #                      "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    #                      "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
    #                      "New Mexico", "Arizona", "Alaska", "Hawaii"]
    #
    # print(states_of_america)
    #
    # list_len = len(states_of_america) # 50 -> 49
    # print(states_of_america[len(states_of_america) - 1])

    # dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Tomatoes", "Peaches",
    #                "Celery", "Cherries", "Potatoes", "Pears"]

    fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
    vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

    # Nested list
    dirty_dozen = [fruits, vegetables]
    print(dirty_dozen)
index_error()

"""
Length of List
You can get the length of a list (number of items in the list) or the length of a string (number characters in the string) by using the len() function. https://docs.python.org/3/library/functions.html#len

IndexError
When you try to access an item that is not in the range of the List, you will get an IndexError. e.g.

fruits = ["Cherry", "Apple", "Pear"]
print(fruits[3]) #This will be an IndexError
Nested Lists
You can put Lists inside other Lists, this becomes something called a "Nested List" or a "2D List". e.g.

fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
You could also represent the list in 2D format like this:

["Cherry", "Apple", "Pear"]
["Cucumber", "Kale", "Spinnach"]
"""

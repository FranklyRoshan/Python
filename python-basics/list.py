
# Example: List Operations in Python

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Initial List:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding elements
fruits.append("orange")      # Add at end
fruits.insert(1, "grape")    # Add at specific position
print("After Adding:", fruits)

# Removing elements
fruits.remove("banana")      # Remove by value
popped_item = fruits.pop()   # Remove last element
print("After Removing:", fruits)
print("Popped Item:", popped_item)

# Updating elements
fruits[0] = "mango"
print("After Updating:", fruits)

# Iterating through list
print("List of Fruits:")
for fruit in fruits:
    print("-", fruit)

# List length
print("Total fruits:", len(fruits))

# Checking membership
print("Is 'cherry' in list?", "cherry" in fruits)
print("Is 'mango' in list?", "mango" in fruits)

# Sorting list
fruits.sort()
print("Sorted List:", fruits)

# Copying list
new_list = fruits.copy()
print("Copied List:", new_list)

''' 🧠 Quick Summary Table
        Operation	            Method / Syntax	                Description
        Create List	            list_name = [ ]	                Define a list
        Access Element	        list[index]	                    Access by index
        Add Element	            append(), insert()	            Add to end or position
        Remove Element	        remove(), pop(), del	            Remove elements
        Update Element	        list[index] = value	            Modify existing value
        Iterate	                for item in list	                Loop through list
        Sort	                sort(), reverse()	            Sort or reverse list
        Copy	                copy(), list()	                Clone a list
        Check Membership	    in, not in	                    Check existence of element
        Length	                len(list)	                    Get number of elements  '''


''' 🧩 1. List as a Stack (LIFO – Last In, First Out)

    In a stack, the last element added is the first one removed,
    like a stack of plates 🍽️.

    🧠 Methods used:

    append() → to push (add) an element

    pop() → to pop (remove) the last element    '''


stack = []

# Pushing elements
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushes:", stack)

# Popping elements
stack.pop()
print("Stack after one pop:", stack)


''' 🧩 2. List as a Queue (FIFO – First In, First Out)

    In a queue, the first element added is the first one removed,
    like people standing in a line 🎫.

    🧠 Methods used:

    append() → to enqueue (add) an element at the end

    pop(0) → to dequeue (remove) from the front '''

queue = []

# Enqueue elements
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueues:", queue)

# Dequeue elements
queue.pop(0)
print("Queue after one dequeue:", queue)

''' ⚡ Note:
    Using list for queues is not efficient because pop(0) is O(n) (slow for large data).
    For efficient queues, use the collections.deque class instead.  '''

''' 🧠 Quick Summary Table
    Feature	             Stack (LIFO)	                    Queue (FIFO)
    Add Element	         append(item)	                    append(item)
    Remove Element	     pop()	                            pop(0) or popleft() if using deque
    Behavior	         Last In → First Out	                First In → First Out
    Efficient Version	 Using list is fine	                Use collections.deque
    Example Use	         Undo operations, back button	    Task scheduling, print queue    '''

from operator import attrgetter
class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__ (self):
        return repr((self.name, self.population, self.area))
    
countries = [Country("India", 12000, 100),
             Country("China", 14000, 200),
             Country("USA", 5000, 300)]

countries.append(Country("Russia", 3000, 750))
countries.sort(key=attrgetter("population"), reverse=True)
print(countries)
print(max(countries, key=attrgetter("population")))
print(min(countries, key=attrgetter("population")))
print(max(countries, key=attrgetter("area")))
print(min(countries, key=attrgetter("area")))

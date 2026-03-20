class Player:
    count = 0   # <-- Class variable (shared by all instances)

    def __init__(self, name):
        self.name = name
        Player.count += 1   # Increment shared count

messi = Player('Messi')
ronaldo = Player('Ronaldo') 

print(Player.count)

print(messi.count)  # (accessing shared variable)
print(ronaldo.count)

# Never use Instance to set/modify value for the Static variable
# messi.count = 100 # creates a new variable for 'messi' only
# print(messi.count) # 100  -> instance variable
# print(ronaldo.count)  # 2   -> still reads class variable
# print(Player.count)   # 2   -> class variable 

''' 🚫 What happens if you modify it using an instance?
        If you do this: 
        You’re not updating the class variable anymore.
        Instead, you’re creating a new instance variable named count for that object only. 
        
        Now:
        messi has its own copy of count (instance variable)
        ronaldo and Player still see the original class variable    
        
        ⚠️ Why it’s a bad practice

        It breaks the shared behavior of class variables.
        It causes confusion and inconsistent data across instances.
        Future code reading becomes harder — because it looks like you updated the class variable but didn’t.'''


''' ✅ Correct way to modify a class (static) variable
    Always modify via the class name, not via the object:'''
Player.count = 100
print(Player.count)

print(messi.count)
print(ronaldo.count)


''' 🧩 Overview
    Type	            Defined Where	                        Belongs To	                Shared Between Objects	                  Accessed Using
    Instance Variable	Inside methods using self	            Specific object (instance)	❌ No — each object has its own copy	    self.variable_name
    Class Variable	    Inside class but outside methods	    The class itself	        ✅ Yes — shared by all objects	        ClassName.variable_name or self.variable_name
    Static Variable	    (In Python, same as class variable)     (not instance)	            ✅ Yes	                                ClassName.variable_name
                        Defined using @staticmethod or 
                        directly under class	Class '''


''' ⚠️ In Python, class variables and static variables are conceptually the same —
        both are shared variables defined at the class level.
        Some other languages (like Java or C++) treat them differently, but Python doesn’t separate them.   '''

class Player:
    team_name = "FC Barcelona"   # Class / Static variable (shared)
    
    def __init__(self, name, goals):
        self.name = name        # Instance variable (unique for each object)
        self.goals = goals      # Instance variable

messi = Player("Messi", 30)
ronaldo = Player("Ronaldo", 35)

print(messi.team_name)     # FC Barcelona
print(ronaldo.team_name)   # FC Barcelona
print(Player.team_name)    # FC Barcelona

# Change team name (class variable)
Player.team_name = "Real Madrid"

print(messi.team_name)     # Real Madrid (updated for all)
print(ronaldo.team_name)   # Real Madrid (updated for all)

# Instance variable is unique
messi.goals = 40
print(messi.goals)         # 40
print(ronaldo.goals)       # 35


''' 🧮 Memory Concept
    Variable Type	            Stored In	                Shared?	    Example
    Instance Variable	        Inside each object	        ❌	       self.name, self.age
    Class / Static Variable	    Inside class memory area	✅	       Player.team_name'''

''' 🧠 Quick Summary Table
    Feature	        Instance Variable	                Class Variable	                        Static Variable
    Declared	    Inside constructor (__init__)	    Inside class (outside methods)	        Same as class variable
    Shared	        No	                                Yes	                                    Yes
    Accessed By	    self.variable	                    ClassName.variable or self.variable	    ClassName.variable
    Example Use	    Player name, goals	                Team name, count of players	            Same as class variable  '''
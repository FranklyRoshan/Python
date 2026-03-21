# ===============================================================
# Namespaces and scope
# ===============================================================

"""
Local Scope
Variables (or functions) declared inside functions have local scope (also called function scope). They are only seen by other code within the same block of code.

e.g.

def my_function():
    my_local_var = 2

# This will cause a NameErrorr
print(my_local_var)
Global Scope
Variables or functions declared at the top level (unindented) of a code file have global scope. It is accessible anywhere in the code file.

e.g.

my_global_var = 3

def my_function():
    # This works no problems
    print(my_global_var)
"""
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Namespace
potion_color = "Red"  # Global Scope


def drink_potion():
    potion_strength = 2  # Local Scope
    print(potion_strength)


drink_potion()
# print(potion_strength)

# ===============================================================
# Block scope
# ===============================================================
"""
Python is a bit different from other programming languages in that it does not have block scope.

This means that variables created nested in other blocks of code e.g. for loops, if statements, while loops etc. don't get local scope. They are given function scope if they are within a function or global scope if they are not.

e.g.

# Accessible anywhere
my_global_var = 1

def my_function():
    # Only accessible within my_function()
    my_local_var = 2

for _ in range(10):
    # Accessible anywhere
    my_block_var = 3

"""
game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# ===============================================================
# Gobal Vars
# ===============================================================
"""
You can force the code allow you to modify something with global if you use the global keyword before you use it.

e.g. This will give you an error

a = 1
def my_function():
    a += 1
    print(a)
But this will work

a = 1
def my_function():
    global a
    a += 1
    print(a)
"""
# Modifying Global Scope

# enemies = 1
#
#
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

enemies = 1


def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

# ===============================================================
# Global Constant
# ===============================================================

"""
You can define global constants in your code file for easy access. Their job is meant to be "set and forget" so you can use their values but never need to mofy them.

Naming Convention
Global constants are normally declared in ALL_CAPS with a underscore in between.

e.g.

PI = 3.14159
GOOGLE_URL = "https://www.google.com"
"""

PI = 3.14159
GOOGLE_URL = "https://www.google.com"


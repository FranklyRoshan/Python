
# ===============================================================
# OOPS Concepts - Class, Constructor, Object Initiatlization, Attributes
# ===============================================================

class User:
    """
    A simple representation of a social media user.

    Attributes:
        user_id (str): Unique identifier for the user.
        username (str): Name of the user.
        followers (int): Number of people following this user.
        following (int): Number of people this user follows.
    """

    def __init__(self, user_id: str, username: str):
        """
        Constructor method that initializes a User object.

        Parameters:
            user_id (str): Unique ID assigned to the user.
            username (str): Name of the user.

        Default Values:
            followers → starts at 0
            following → starts at 0
        """

        # Unique identifier for the user
        self.user_id = user_id

        # Username of the user
        self.username = username

        # Number of followers this user has
        self.followers = 0

        # Number of people this user follows
        self.following = 0

    def follow(self, other_user):
        """
        Allows the current user to follow another user.

        Parameters:
            other_user (User): The user that will be followed.

        Behaviour:
            - The other user's follower count increases by 1
            - The current user's following count increases by 1
        """

        other_user.followers += 1
        self.following += 1


# Creating User Objects (Object Initialization)
user_1 = User("001", "angela")
user_2 = User("002", "frank")

# Accessing attributes
print(user_1.user_id)
print(user_1.username)

# user_1 follows user_2
user_1.follow(user_2)

# Printing follower statistics
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)

"""
Key Components of the Process

* Instantiation: This is the act of creating a unique "instance" (an object) from a class blueprint. In your example, 
Turtle is the class (the blueprint), and tim is the specific instance (the individual turtle).
* Initialization: Immediately after the object is created, Python automatically runs the init() method to set the 
object's starting state, such as its initial position and color.
* Constructor: The call Turtle() acts as a constructor, which is a special function that handles both the creation and 
setup of the new object. [1, 2, 3, 4, 5]

Code  Role
Turtle  - The Class (the template for all turtles).
Turtle()  - The Constructor call that triggers instantiation.
timmy - The Instance or Object (the specific entity you can control).

====================================================================================================================

In the world of Object-Oriented Programming (OOP), these represent the two ways you interact with an object:
1. object.method() (The Action)
A method is a function that belongs to an object. It represents what the object can do.

* Syntax: Always followed by parentheses (), even if empty.
* Example: tim.forward(100) or tim.right(90).
* Purpose: To perform an operation or change the state of the object.

2. object.attribute (The Data)
An attribute is a variable that belongs to an object. It represents what the object is (its characteristics).

* Syntax: No parentheses.
* Example: tim.color or tim.pensize.
* Purpose: To store or retrieve information about the object's current state.

Feature         object.method()     object.attribute
Analogy         A Verb (Action)     A Noun (Trait)
Notation        Uses ()             No ()
Turtle Example  tim.pendown()       tim.heading
Result          Triggers behavior   Accesses data
"""

# ===============================================================
# Class, Constructor, Object Initialization, Attributes
# ===============================================================

# # PascalCase --> for Class
# class User:
#     pass
# # snake_case --> for variables and methods
# user_1 = User()
# user_1.id = "001"
# user_1.username = "angela"
#
# user_2 = User()
# user_1.id = "002"
# user_2.username = "frank"
#
# def function():
#     pass
#
# print("Hello")

# Class
# class User:
#
#     # Constructor
#     def __init__(self, user_id, username):
#         self.user_id = user_id # attributes
#         self.username = username
#         self.followers = 0 # default attribute
#         self.following = 0 # default attribute
#
#     # method
#     def follow(self, other_user):
#         other_user.followers += 1
#         self.following += 1
#
# # object initialization
# user_1 = User("001", "angela")
# user_2 = User("002", "frank")
# print(user_1.user_id)
# print(user_1.username)
#
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)






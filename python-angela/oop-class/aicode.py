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
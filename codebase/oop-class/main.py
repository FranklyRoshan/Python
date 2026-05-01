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
class User:

    # Constructor
    def __init__(self, user_id, username):
        self.user_id = user_id # attributes
        self.username = username
        self.followers = 0 # default attribute
        self.following = 0 # default attribute

    # method
    def follow(self, other_user):
        other_user.followers += 1
        self.following += 1

# object initialization
user_1 = User("001", "angela")
user_2 = User("002", "frank")
print(user_1.user_id)
print(user_1.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)








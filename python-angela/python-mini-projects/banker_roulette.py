
# ===============================================================
# Banker Roulette
# ===============================================================
def banker_roulette():
    import random
    friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

    # random.randint
    list_len = len(friends)
    rand = random.randint(0,list_len)
    print(friends[rand])

    # random.choice
    print(random.choice(friends))
banker_roulette()

"""
Figure out how to pick a random name from the list of friends.

 Hint 1 
There are two ways of doing this and they are equally valid.
 Hint 2 
Think about how you can generate random number to use an index to pick out items from the List.
 Hint 3 
Alternatively think about using the documentation to figure out how to get a random item from a List in Python.
"""

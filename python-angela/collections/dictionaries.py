#=====================================================================
# Dictionaries
#=====================================================================
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The Action of doing something over and over again",

}

print(programming_dictionary["Function"])
programming_dictionary["Data types"] = "An Attribute that tells the computer how to interpret and manipulate a specific piece of data."
print(programming_dictionary)

empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "An moth in your computer."
print(programming_dictionary)

# loop through the dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

"""
A dictionary in Python functions similarly to a dictionary in real life. It's a data structure that allows us to associate a key to a value and pair the two pieces of data together.

This is how you create a dictionary in Python:

# An example dictionary
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}

This is how you retrieve items from a dictionary:

print(colours["pear"])
#Will print "green"
This is how to create an empty dictionary:

my_empty_dictionary = {}
This is how you can add new items to an existing dictionary:

colours["peach"] = "pink"
This is also how you can edit an existing value in a dictionary:

colours["apple"] = "green"
This is how to loop through a dictionary and print all the keys:

for key in colours:
    print(key)
This is how to loop through a dictionary and print all the values:

for key in colours:
    print(colours[key])
"""

#=====================================================================
# Nesting lists and dictionaries
#=====================================================================

capitals = {
    "Frances": "Paris",
    "Germany": "Berlin",

}

# Nested List in Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
#
# }
#
# # print Lille
# print(travel_log["France"][1])

# print "D"
nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

travel_log = {
    "France": {
        "Cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,

    },
    "Germany": {
        "Cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,

    },

}

print(travel_log["Germany"]["Cities_visited"][2])

"""
You can mix and match various data types to achieve your desired structure.

Nesting a List inside a Dictionary
Instead of a String value assigned to a key, we can replace it with a List. You can nest a List in a Dictionary like this:

my_dictionary = {
    key1: [List],
    key2: Value,
}
PAUSE 1
See if you can figure out how to print out "Lille" from the nested List called travel_log.

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
 Hint 1 
Nesting Lists inside other Lists
We've previously seen Nested Lists:

nested_list = ["A", "B", ["C", "D"]]
PAUSE 2
Do you remember how to get items that are nested deeply in a list? Try to print "D" from the list nested_list.

 Hint 2 
Nesting a Dictionary inside a Dictionary
You can also nest a dictionary in a dictionary:

my_dictionary = {
    key1: Value,
    key2: {Key: Value, Key: Value},
}
PAUSE 3
Figure out how to print out "Stuttgart" from the following list:

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}
"""

#=====================================================================
# Blind Auction Project
#=====================================================================

from bid_art import logo
print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)

"""
You can mix and match various data types to achieve your desired structure.

Nesting a List inside a Dictionary
Instead of a String value assigned to a key, we can replace it with a List. You can nest a List in a Dictionary like this:

my_dictionary = {
    key1: [List],
    key2: Value,
}
PAUSE 1
See if you can figure out how to print out "Lille" from the nested List called travel_log.

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
 Hint 1 
Nesting Lists inside other Lists
We've previously seen Nested Lists:

nested_list = ["A", "B", ["C", "D"]]
PAUSE 2
Do you remember how to get items that are nested deeply in a list? Try to print "D" from the list nested_list.

 Hint 2 
Nesting a Dictionary inside a Dictionary
You can also nest a dictionary in a dictionary:

my_dictionary = {
    key1: Value,
    key2: {Key: Value, Key: Value},
}
PAUSE 3
Figure out how to print out "Stuttgart" from the following list:

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}
"""
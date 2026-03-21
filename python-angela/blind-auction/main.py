# =====================================================================
# Blind Auction Project
# =====================================================================

from art import logo

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

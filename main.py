import os
clear = lambda: os.system('cls')


clear()

#variables and dictionaries
should_continue = True

all_bids = {}

#start of user experience
from art import logo
print(logo)
print("Welcome to the secret auction program.")

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for name in all_bids:
        bid_amount = bidding_record[name]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while should_continue:
    new_name = input("What is your name?: ")
    new_bid = int(input("What's your bid?: $"))
    all_bids[new_name] = new_bid
    more_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bid == "no":
        should_continue = False
        highest_bidder(all_bids)
    clear()


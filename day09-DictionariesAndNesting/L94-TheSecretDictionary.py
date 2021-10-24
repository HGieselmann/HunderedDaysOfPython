# My Solution using global
def find_highest_bid():
    global highest_bid, highest_bidder
    for key in bids:
        highest_bid = 0
        highest_bidder = ""
        if bids[key] > highest_bid:
            highest_bid = bids[key]
            highest_bidder = key


print("Welcome to the secret bid auction program!")
taking_bids = True
bids = {}
while taking_bids:
    name = input("Please enter the bidders name: ")
    bid = int(input("Please enter your bid: "))
    bids[name] = bid
    bidding_active = input("Do you want to add another bid? (yes/no):  ").lower()
    if bidding_active == "no":
        taking_bids = False

find_highest_bid()

print(f"The hightes bidder was {highest_bidder} with a bid of {highest_bid}.")
print("Congratulations!")

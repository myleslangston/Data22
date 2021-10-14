from replit import clear

print("Welcome to the Silent Auction. Shhhh!")
bidders = {}
another_bid = True


def find_highest_bid(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of £{highest_bid}!!")


while another_bid:
    player_name = input("What is your name?\n")
    player_bid = int(input("How much do you want to bid?\n£"))
    bidders[player_name] = player_bid
    another_round = input("Is there another bidder\n")
    if another_round == "no":
        another_bid = False
        find_highest_bid(bidders)
    else:
        clear()


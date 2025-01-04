def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


all_bidders = {}
continue_bidding = True
while continue_bidding: 
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    all_bidders[name] = bid
    other_bidders_check =input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders_check == "yes":
        print("\n" * 20)
    else: 
        continue_bidding = False
        find_highest_bidder(all_bidders)
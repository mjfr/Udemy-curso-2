import art
from os import system
def main():
    
    print(art.logo)
    print("Welcome to the Secret Auction Program.")

    new_bidder = "yes"
    bidding_list = []
    value_comparison = 0

    while new_bidder == "yes":
        bidder = input("What is your name?\nAnswer: ")
        bid = int(input("What is your bid?\nAnswer: $"))
        bidding_list.append({"bidder" : bidder, "bid" : bid})
        new_bidder = input("Are there any other bidder? (yes / no)\nAnswer: ")
        system("cls")

    for bidder in bidding_list:
        if bidder["bid"] > value_comparison:
            value_comparison = bidder["bid"]
            winner = bidder
    print(f"The winner is {winner['bidder']} with a bid of ${winner['bid']}")

if __name__ == '__main__':
    main()
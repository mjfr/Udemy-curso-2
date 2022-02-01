############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import art
from os import system
import random

def main():

    # Ás, 2, [...], 9, 10, J, Q, K
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_dealer_score = {"player_score" : 0, "dealer_score" : 0}
    player_dealer_deck = {"player_deck" : [], "dealer_deck" : []}

    def first_card_assignment():
        if player_dealer_deck["dealer_deck"] == [] and player_dealer_deck["player_deck"] == []:
            while len(player_dealer_deck["dealer_deck"]) < 2 and len(player_dealer_deck["player_deck"]) < 2:
                player_dealer_deck["dealer_deck"].append(random.choice(card_deck))
                player_dealer_deck["player_deck"].append(random.choice(card_deck))
    
    def score_assignment():
        player_dealer_score["player_score"] = 0
        player_dealer_score["dealer_score"] = 0
        card_position_player = 0
        card_position_dealer = 0
        for card in player_dealer_deck["player_deck"]:
            if card == 11 and (player_dealer_score["player_score"] + card) > 21:
                card = 1
                player_dealer_deck["player_deck"][card_position_player] = 1
            player_dealer_score["player_score"] += card
            card_position_player += 1

        for card in player_dealer_deck["dealer_deck"]:
            if card == 11 and (player_dealer_score["dealer_score"] + card) > 21:
                card = 1
                player_dealer_deck["dealer_deck"][card_position_dealer] = 1
            player_dealer_score["dealer_score"] += card
            card_position_dealer += 1

    def verify_score():
        '''
        Returns 0 if the player loses\n
        Returns 1 if the player wins by blackjack\n
        Returns 2 if the player wins by higher score than dealer's\n
        Returns 3 if it is a draw\n
        Returns 4 if dealer goes over 21
        Returns -1 if it is not a known condition
        '''
        if player_dealer_score["player_score"] == 21:
            return 1
        elif player_dealer_score["player_score"] > 21:
            return 0
        elif player_dealer_score["dealer_score"] == player_dealer_score["player_score"]:
            return 3
        elif player_dealer_score["player_score"] < player_dealer_score["dealer_score"] and player_dealer_score["dealer_score"] > 21:
            return 4
        elif player_dealer_score["dealer_score"] == 21 and player_dealer_score["player_score"] < 21:
            return 0
        elif player_dealer_score["player_score"] > player_dealer_score["dealer_score"]:
            return 2
        elif player_dealer_score["dealer_score"] > player_dealer_score["player_score"]:
            return 0
        else:
            return -1

    def blackjack():
        play_blackjack = input("Start Blackjack game? Type 'y' to play or 'n' to exit.\nAnswer: ")
        system("cls")
        while play_blackjack == "y":
            print(art.logo)
            first_card_assignment()
            score_assignment()
            print(f"Your cards are: {player_dealer_deck['player_deck']} and your current score is {player_dealer_score['player_score']}\nDealer's first card is [{player_dealer_deck['dealer_deck'][0]}]")
            hit_pass = input("\nType 'y' to get another card (hit) or type 'n' to pass\nAnswer: ").lower()
            if hit_pass == "y":
                system("cls")
                while hit_pass == "y":
                    player_dealer_deck["player_deck"].append(random.choice(card_deck))
                    score_assignment()
                    print(f"Your cards are: {player_dealer_deck['player_deck']} and your current score is {player_dealer_score['player_score']}\nDealer's first card is [{player_dealer_deck['dealer_deck'][0]}]")
                    if player_dealer_score["player_score"] > 21:
                        break
                    hit_pass = input("Hit again? Type 'y' to hit or 'n' to stop hitting.\nAnswer: ")
                system("cls")

            while player_dealer_score["dealer_score"] < 17:
                player_dealer_deck["dealer_deck"].append(random.choice(card_deck))
                score_assignment()
            
            if verify_score() == 0:
                print("\n>>>Player loses!<<<\n")
            elif verify_score() == 1:
                print("\n>>>Player wins by blackjack!<<<\n")
            elif verify_score() == 2:
                print("\n>>>Player wins by surpassing dealer's score!<<<\n")
            elif verify_score() == 3:
                print("\n>>>It's a draw!<<<\n")
            elif verify_score() == 4:
                print("\n>>>You win! Dealer went above 21.<<<\n")
            elif verify_score == -1:
                print("\n>>>Unknown condition yet<<<\n")

            print(f"\nFinal results:\n{player_dealer_deck}\n{player_dealer_score}\n")
            
            play_blackjack = input("Start another round? Type 'y' to play again or 'n' to exit.\nAnswer: ").lower()
            if play_blackjack == 'y':
                player_dealer_deck["player_deck"] = []
                player_dealer_score["player_score"] = 0
                player_dealer_deck["dealer_deck"] = []
                player_dealer_score["dealer_score"] = 0
                system("cls")

    blackjack()
            

if __name__ == '__main__':
    main()
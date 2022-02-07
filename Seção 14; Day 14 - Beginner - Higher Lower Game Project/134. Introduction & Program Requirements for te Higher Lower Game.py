def main():
    import art
    import game_data
    import random
    from os import system

    play = True
    while play:
        err = False
        score = 0
        a = random.choice(game_data.data)
        b = random.choice(game_data.data)
        while err == False:
            if a == b:
                b = random.choice(game_data.data)
            system("cls")
            print(art.logo)
            if score != 0:
                print(f"You're right! Current score: {score}")
            print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.\n{a['name']} has {a['follower_count']}M followers on Instagram.")
            print(f"\n{art.vs}\n")
            print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
            
            answer = input("\nWho has the highest amount of followers on Instagram?\nAnswer: ").upper()

            if answer == "A":
                if a["follower_count"] >= b["follower_count"]:
                    print()
                    score += 1
                    a = b
                    b = random.choice(game_data.data)
                else:
                    err = True
            elif answer == "B":
                if b["follower_count"] >= a["follower_count"]:
                    print()
                    score += 1
                    a = b
                    b = random.choice(game_data.data)
                else:
                    err = True
            else:
                print("Wrong input!!!")
            
        print(f"\nWrong!!! You got {score} points.\n{a['name']} has {a['follower_count']}M followers and {b['name']} has {b['follower_count']}M followers.")
        play = input("\nWould you like to play again? Type 'y' to play again or 'n' to exit.\nAnswer: ").lower()
        while (play != "y") and (play != "n"):
            play = input("Wrong input!\nType 'y' to play again, 'n' to exit.\nAnswer: ")
        if play == "y":
            play = True
        else: 
            play = False

if __name__ == "__main__":
    main()
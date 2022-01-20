#Write your code below this line 👇
def main():
    import random

    print("Welcome to the most special Rock Paper Scissors ever created\n\n\nby me...\n\n")

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
             _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)
    '''

    player_decision = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\nI choose: "))
    computer_decision = random.randint(0, 2)
    plays_list_name = ["Rock", "Paper", "Scissors"]
    plays_list_figures = [rock, paper, scissors]

    if player_decision >= 3 or player_decision < 0:
        print("... Invalid choice, try again.")
    elif player_decision == computer_decision:
        print(f"You: {plays_list_figures[player_decision]}\nComputer: {plays_list_figures[computer_decision]}")
        print(f"It's a draw! You both chose {plays_list_name[player_decision]}")
    elif player_decision == 0 and computer_decision == 2:
        print(f"You: {plays_list_figures[player_decision]}\nComputer: {plays_list_figures[computer_decision]}")
        print(f"You won! {plays_list_name[player_decision]} wins against {plays_list_name[computer_decision]}.")
    elif player_decision == 1 and computer_decision == 0:
        print(f"You: {plays_list_figures[player_decision]}\nComputer: {plays_list_figures[computer_decision]}")
        print(f"You won! {plays_list_name[player_decision]} wins against {plays_list_name[computer_decision]}.")
    elif player_decision == 2 and computer_decision == 1:
        print(f"You: {plays_list_figures[player_decision]}\nComputer: {plays_list_figures[computer_decision]}")
        print(f"You won! {plays_list_name[player_decision]} wins against {plays_list_name[computer_decision]}.")
    else:
        print(f"You: {plays_list_figures[player_decision]}\nComputer: {plays_list_figures[computer_decision]}")
        print(f"You lost! {plays_list_name[player_decision]} loses against {plays_list_name[computer_decision]}.")
        

if __name__ == '__main__':
    main()

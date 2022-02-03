#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def main():
    import art
    import random
    from os import system

    def generate_random_number():
        """
        Cria uma lista vazia e extende a mesma a partir de um range\n
        Retorna um número aleatório escolhido a partir da lista
        """
        number_list = []
        number_list.extend(range(1, 101))
        return random.choice(number_list)

    def dificulty_selection():
        """
        Recebe um input do usuário e retorna 9 para o input 'easy' e 4 para o input 'hard'
        """
        dificulty_mode = input("\nYou can type 'easy' to only help me (you will get 10 tries) or if you are feeling lucky, you can help me and spread your glorious deed choosing to type 'hard' (you will get 5 tries)\nWhat is your answer? ")
        while dificulty_mode != "easy" and dificulty_mode != "hard":
            dificulty_mode = input("Wrong input. Type 'easy' to get 10 tries or 'hard' to get 5 tries.\nAnswer: ")
            print(dificulty_mode)
        if dificulty_mode == 'easy':
            return 9
        else:
            return 4

    def guess_comparison(number, dificulty):
        """
        Recebe como parâmetro o número aleatório e a dificuldade\n
        Realiza a contagem regressiva para a dificuldade a cada erro do usuário\n
        Retorna um texto sobre o resultado (sucesso/falha)
        """
        print(f"Guessing tries left: x{dificulty+1}")
        guess = int(input("What number did you find?\nAnswer: "))
        while dificulty != 0 and guess != number:
            print(f"Guessing tries left: x{dificulty}")
            if guess > number:
                guess = int(input("The number I lost is lower than this. Try again.\nAnswer: "))
                dificulty -= 1
            elif guess < number:
                guess = int(input("The number I lost is higher than this. Try again.\nAnswer: "))
                dificulty -= 1
        if dificulty == 0 and number != guess:
            system("cls")
            return f"No more guessing for you! Loser!\nI found it myself, humph... You want to know which one was it?\nOkay, I shall tell you...\nIt was {number}, there. Are you happy now?"
        return f"Thank you! You really found my lost {guess}!!!"
        
    def game():
        """
        Função para dar início ao jogo.
        Recebe um input do usuário para repetir ou não o jogo.
        """
        play_again = 'y'
        print(f"Welcome to:\n{art.logo}\nI need you to use that big brain of yours to help me find my lost number.\nIt is somewhere between 1 and 100.\nBut before you help me find my precious lost number, I need to ask you: Do you want to only help me or bask in glory while helping me?")
        while play_again == 'y':
            hidden_number = generate_random_number()
            dificulty = dificulty_selection()
            print(guess_comparison(hidden_number, dificulty))
            play_again = input("Would you like to play again?\nType 'y' to play again or type 'n' to exit.\nAnswer: ")
            system("cls")

    game()

if __name__ == "__main__":
    main()
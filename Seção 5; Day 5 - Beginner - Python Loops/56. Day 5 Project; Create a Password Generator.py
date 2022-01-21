def main():
    #Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    password_letters = ""
    password_symbols = ""
    password_numbers = ""
    for _ in range(0, nr_letters):
        password_letters += letters[random.randint(0, len(letters)-1)]
    for _ in range(0, nr_symbols):
        password_symbols += numbers[random.randint(0, len(numbers)-1)]
    for _ in range(0, nr_numbers):
        password_numbers += symbols[random.randint(0, len(symbols)-1)]
    
    ordered_password = password_letters + password_symbols + password_numbers

    print("Not randomized order")
    print(f"Your new not so cool password is: {ordered_password}")



    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    ordered_password_as_list = []
    for char in ordered_password:
        ordered_password_as_list.append(char)

    aux_password = ""
    position_to_be_poped = int
    for _ in range(0, len(ordered_password_as_list)):
        position_to_be_poped = random.randint(0, len(ordered_password_as_list)-1)
        aux_password += ordered_password_as_list[position_to_be_poped]
        ordered_password_as_list.pop(position_to_be_poped)

    print("Randomized order")
    print(f"Your new cool password is: {aux_password}")

if __name__ == '__main__':
    main()
def main():
    number = int(input("Which number do you want to check? "))

    # if number % 2 = 0:  --> O sinal de igual está sendo usado como atribuição não comparação. Basta adicionar mais um sinal de igual.
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")


if __name__ == "__main__":
    main()
def main():
    for number in range(1, 101):
        # if number % 3 == 0 or number % 5 == 0: --> OR considera que com tanto que uma expressão seja verdadeira, a condição será True, independente se houver uma ou mais condições falsas antes ou depois da verdadeira.
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        # if number % 3 == 0: # Se esta condição for verdadeira, independentemente da condição acima passar ou não, esta seria executada. Alteramos o if para elif, assim, apenas se a condição acima for falsa, esta será executada, assim, evitamos duplicidade.
        elif number % 3 == 0:
            print("Fizz")
        # if number % 5 == 0: # Mesma explicação acima
        elif number % 5 == 0:
            print("Buzz")
        else:
            # print([number]) # Pelas instruções, devemos printar apenas o número e não uma lista de um número único
            print(number)

if __name__ == "__main__":
    main()
'''
Começando pela seção 4, pois a seção 1, 2 e 3, respectivamente: "Working with Variables in Python to Manage Data", "Understanding Data Types and How to Manipulate Strings" e "Control Flow and Logical Operators"
são conteúdos que já foram passados no primeiro curso que fiz e ao assistir as aulas, não percebi acréscimo algum.
'''

def main():
    # Curiosidade: Python utiliza um pseudo gerador de números aleatórios chamado de "Mersenne Twister"
    import random
    
    # Atribuíndo à uma variável um número aleatório dentro do intervalo de 1 a 10 (ambos inclusos)
    random_integer = random.randint(1, 10)
    print(random_integer)

    # Atribuíndo à uma variável um número aleatório dentro do intervalo de 0 a 1 (1 não está incluso)
    random_float = random.random()
    print(random_float)

    # Podemos gerar um float aleatório com um intervalo diferente apenas por multiplicar o float
    print(random_float * 7)

if __name__ == '__main__':
    main()
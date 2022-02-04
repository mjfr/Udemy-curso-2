############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])


##############################################################################################################
def main():
    # Describe Problem
    # def my_function():
    #     for i in range(1, 20):
    #         if i == 20:
    #             print("You got it")
    # my_function()

    # Supostamente a pessoa gostaria que a função executasse o print, porém, range começa de x e termina em y-1

    # Debugged --> Aumentamos o término do range para que ao invés de terminar em 20-1 = 19, termine em 21-1 = 20
    def my_function():
        for i in range(1, 21):
            if i == 20:
                print("You got it")
    my_function()

##############################################################################################################

    # Reproduce the Bug
    # from random import randint
    # dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
    # dice_num = randint(1, 6)
    # print(dice_imgs[dice_num])

    # Supostamente a pessoa esperava receber resultados do dado de 1 a 6, porém, randint é diferente do range.
    # Randint não exclui o último valor. No caso, randint pega ambos os valores passados

    # Debugged --> Basta lembrar que listas começam a partir do zero, como a lista possui 6 elementos, basta alterar o início e fim do randint para 0, 5 (0, 1, 2, 3, 4, 5) = 6 elementos
    from random import randint
    dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
    dice_num = randint(0, 5)
    print(dice_imgs[dice_num])

##############################################################################################################

    # Play Computer
    # year = int(input("What's your year of birth?"))
    # if year > 1980 and year < 1994:
    #     print("You are a millenial.")
    # elif year > 1994:
    #     print("You are a Gen Z.")

    # Ao passarmos o ano de 1994 não recebemos resposta alguma pois 1994 não é maior nem menor que 1994.

    # Debugged --> Basta decidirmos onde queremos incluir o ano de 1994 (na geração millenial ou Z) com o comparador maior igual ou menor igual
    year = int(input("What's your year of birth?"))
    if year > 1980 and year < 1994:
        print("You are a millenial.")
    elif year >= 1994:
        print("You are a Gen Z.")

##############################################################################################################

    # Fix the Errors
    # age = input("How old are you?")
    # if age > 18:
    # print("You can drive at age {age}.")

    # O primeiro erro é a indentação do código.
    # O segundo erro é a questão que não é possível comparar str com int.
    # O terceiro erro, é a falta do 'f' antes da string do print.

    # Debugged --> Basta indentar corretamente o código e fazer um cast int no input (retorna str). Por fim, basta utilizar 'f' para transformar a string em fstring
    age = int(input("How old are you?"))
    if age > 18:
        print(f"You can drive at age {age}.")

##############################################################################################################

    # #Print is Your Friend
    # pages = 0
    # word_per_page = 0
    # pages = int(input("Number of pages: "))
    # word_per_page == int(input("Number of words per page: "))
    # total_words = pages * word_per_page
    # print(total_words)

    # O erro que está presente é o sinal de igual duplicado para a variável word_per_page, que ao invés de atribuir valor a variável, apenas serve de comparação

    # Debugged --> Ao printar todas as variáveis, percebemos que apenas a variável word_per_page continua com o valor 0 inicial. Basta apagar um sinal de igual para que possamos atribuir valor a variável
    pages = 0
    word_per_page = 0
    pages = int(input("Number of pages: "))
    word_per_page = int(input("Number of words per page: "))
    total_words = pages * word_per_page
    print(total_words)

    print(f"PAGES --> {pages}")
    print(f"WORD_PER_PAGE --> {word_per_page}")

##############################################################################################################

    # #Use a Debugger
    # def mutate(a_list):
    #   b_list = []
    #   for item in a_list:
    #     new_item = item * 2
    #   b_list.append(new_item)
    #   print(b_list)

    # mutate([1,2,3,5,8,13])

    # O problema é novamenta a indentação do código. "b_list.append(new_item)" está fora do bloco for, logo, o append só irá adicionar o último resultado obtido pelo laço for.

    # Debugged --> https://pythontutor.com/visualize.html#mode=edit debugger online. Basta simplesmente indentar a linha "b_list.append(new_item)" para que esteja dentro do for e toda vez que um loop ocorrer, um novo item seja adicionado ao final da lista.
    def mutate(a_list):
      b_list = []
      for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
      print(b_list)

    mutate([1,2,3,5,8,13])


if __name__ == '__main__':
    main()
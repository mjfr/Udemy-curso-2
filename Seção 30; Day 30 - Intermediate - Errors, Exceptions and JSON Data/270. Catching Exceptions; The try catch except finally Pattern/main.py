# O bloco try except else finally trabalham da seguinte forma:
# Try --> Tenta realizar algo que está propenso a gerar erros
# Except --> Recebe uma exceção que pode ser gerada e dentro de seu bloco teremos o tratamento da mesma.
# Else --> Caso não gere exceções no bloco try, o bloco else será executado
# Finally --> Independente de qualquer resultado, este bloco será executado

# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit_list = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["keyy"])
# except FileNotFoundError:  # Segundo a convenção PEP 8: E722, não deve ser usado "except" sem especificar o erro,
#     # visto que ele aceita todos os erros, logo, um FileNotFoundError e um KeyError seriam tratados da mesma maneira
#     # print("There was an error")
#     file = open("a_file.txt", "w")
#     file.write("Writing something")
# except KeyError as error_message:  # Também podemos pegar a exceção como texto
#     print(f"The key {error_message} does not exist.")
# else:  # Este bloco else não será executado caso o bloco try não passe de primeira.
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     # Também podemos levantar nossas próprias exceções com a kew word "raise"
#     raise TypeError("This is an error that I made up.")

# Um exemplo de quando queremos levantar nossas próprias exceções:
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)





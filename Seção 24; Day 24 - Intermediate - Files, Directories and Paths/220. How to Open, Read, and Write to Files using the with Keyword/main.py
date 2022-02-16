# file = open("my_file.txt")
# Através da keyword with, o Python entende que o arquivo será trabalhado dentro do bloco de código no qual o arquivo
# foi indentado. Assim ele abre o arquivo no início do bloco e fecha o arquivo no final do bloco
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
# file.close()

# Quando queremos escrever em um arquivo, utilizamos o método write(), porém ele só funciona quando o arquivo pode ser
# editado. Para isso podemos passar atributos no parâmetro "mode" que devem transformar um arquivo de apenas leitura
# para um arquivo de escrita. Podemos utilizar "w" como write para apagar tudo no arquivo e escrever o novo texto ou
# podemos utilizar "a" como append para apenas adicionar ao arquivo existente sem apagar nenhum dado
with open("my_file.txt", mode="w") as file2:
    file2.write("New text.")

with open("my_file.txt", mode="a") as file3:
    file3.write("\nNew text.")

# Ao tentarmos abrir um arquivo inexistente no modo de escrita "w", o arquivo será criado e o conteúdo será criado
with open("new_file.txt", mode="w") as file4:
    file4.write("\nNew text, new file.")

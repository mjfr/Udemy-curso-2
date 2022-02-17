import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

# Data neste caso é um tipo DataFrame, isto é: uma estrutura bidimensional, uma tabela com linhas e colunas
print(type(data))

# Data["temp"] neste caso é um tipo Series, isto é: uma estrutura unidimensional, apenas uma lista
print(type(data["temp"]))

# Uma tabela é um DataFrame enquanto cada uma de suas colunas é um tipo Series
# Recuperando um objeto DataFrame em formato de dicionário padrão do Python
data_dict = data.to_dict()
print(data_dict)

# Recuperando um objeto Series em formato de lista padrão do Python
data_list = data["temp"].to_list()
print(data_list)


average = 0
for temp in data_list:
    average += temp
average = average/len(data_list)
print(average)

print(data["temp"].mean())
print(data["temp"].max())

print(data["condition"])
# Por trás das cortinas, Pandas consegue pegar o rótulo de cada coluna e transforma-lo em atributo
print(data.condition)

# Retorna a linha
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print(f"From Celsius to Fahrenheit {monday.temp[0] * 1.8 + 32}°F")


# Criando um DataFrame do zero:
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
print(data_dict)
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")

print_csv = pandas.read_csv("new_data.csv")
print(print_csv)

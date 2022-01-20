import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Lembrando que listas começam com o primeiro elemento no índice 0 e terminam com o tamanho da lista -1 (pois começa no zero)
name = random.randint(0, len(names)-1)
print(f"{names[name]} is going to buy the meal today!")
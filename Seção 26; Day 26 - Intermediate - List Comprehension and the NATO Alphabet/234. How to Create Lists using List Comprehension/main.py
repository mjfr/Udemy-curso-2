# Maneira extensa
numbers = [1, 2, 3]
new_list = []
for item in numbers:
    add_1 = item + 1
    new_list.append(add_1)
print(new_list)

# List Comprehension
# Variável = [novo_item for item in lista]
new_list2 = [item + 1 for item in numbers]
print(new_list2)

name = "Matheus"
new_list3 = [letter for letter in name]
print(new_list3)

new_list4 = [number * 2 for number in range(1, 5)]
print(new_list4)

# Conditional List Comprehension
# Variável = [novo_item for item in lista if condição]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

all_caps = [name.upper() for name in names if len(name) > 5]
print(all_caps)




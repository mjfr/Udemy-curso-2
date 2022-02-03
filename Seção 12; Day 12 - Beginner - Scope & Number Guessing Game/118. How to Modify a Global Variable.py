enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

# Não conseguimos modificar uma variável de escopo global dentro de uma função se não utilizarmos do prefixo 'global' + variável


def increase_enemies():
    global enemies
    enemies += 3
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

# Geralmente não queremos modificar variáveis de escopo globais pois isso aumenta as chances de erros e falhas no código
# Porém, podemos fazer de uma maneira diferente, sem utilizar o prefixo 'global' mas sim utilizando o return e atribuíndo o novo valor a variável


def increase_enemies():
    print(f"Enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")

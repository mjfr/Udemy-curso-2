# Argumentos ilimitados em funções: usamos *args por convenção para indicar a possibilidade de infinitos argumentos
def print_many(*args):
    for n in args:
        print(n)


print_many(1, 2, 3, 4, 5, 6, 7, 8, 9)


def add(*num_to_add):
    total = 0
    for n in num_to_add:
        total += n
    # *args são tuplas
    print(type(num_to_add))
    return total


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


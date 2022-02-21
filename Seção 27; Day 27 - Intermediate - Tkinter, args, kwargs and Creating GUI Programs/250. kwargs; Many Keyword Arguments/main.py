# 2 * para criar kwargs ilimitados. (Funcionam basicamente como dicionários)
# Não são obrigatórios ao chamar uma função, mas se os argumentos forem declarados, eles serão usados
def calculate(n, **kwargs):
    # print(type(kwargs))
    # print(kwargs)
    # for key, value in kwargs.items():
        # print(key)
        # print(value)
        # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        # self.model = kw["model"]
        # Ao usar .get(), caso o atributo não seja passado, mesmo ao chamar o atributo, não obteremos erros, apenas None
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


# my_car = Car(make="Nissan")
my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)

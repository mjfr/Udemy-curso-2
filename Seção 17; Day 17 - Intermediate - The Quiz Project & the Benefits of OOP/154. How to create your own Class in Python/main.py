# Para criar uma classe, utilizamos a keyword 'class' NomeDaClasse (nome da classe em Pascal Case)
class User:
    pass  # Simplesmente passa para a próxima linha/bloco de código


user_1 = User()
# É possível adicionar atributos a objetos dessa forma
user_1.id = "001"
user_1.username = "Matheus"

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.name = "James"  # <-- Adicionar atributos desta forma é algo que não é prático e também está propenso a erros


class UserTwo:
    def __init__(self, user_id, username):  # A função __init__(self) é onde iniciamos (criamos os valores iniciais
        #  para os atributos) self é o objeto sendo criado/inicializado
        # Toda vez que um objeto é instanciado (objeto = Classe()), executa-se o que está dentro do __init__(self)
        print("Executing from inside UserTwo class")
        self.id = user_id
        self.username = username  # Por convenção, utiliza-se o nome do parâmetro igual ao nome do atributo
        # Mas não é completamente necessário seguir essa convenção
        self.followers = 0  # É possível deixar valores pré-definidos (não é necessário atribuir valores no construtor)
        self.following = 0

    def follow(self, user):  # Diferente de funções normais, métodos de classes precisam ter o self como parâmetro,
        # uma vez que é assim que a função sabe qual objeto está chamando ela
        user.followers += 1
        self.following += 1


user_3 = UserTwo("003", "Laura")
user_4 = UserTwo("004", "Martin")

user_3.follow(user_4)
print(user_3.followers)
print(user_3.following)
print(user_4.followers)
print(user_4.following)


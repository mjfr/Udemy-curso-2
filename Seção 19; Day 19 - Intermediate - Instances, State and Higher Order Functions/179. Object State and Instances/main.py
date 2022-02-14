from turtle import Turtle
# Objetos provenientes da mesma classe são independentes entre si, logo, dizemos que são diferentes instâncias

# Timmy e larry são instâncias de Turtle(). Ambos possuem mesma origem, porém atuam de forma independente.
# Ambos são exemplos do objeto Turtle()
timmy = Turtle()
larry = Turtle()

# Estados são diferentes valores de atributos ou funções. O estado de timmy é 'green' e o estado de larry é 'purple'
timmy.color("green")
larry.color("purple")

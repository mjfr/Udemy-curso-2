def main():
    # import another_module
    # print(another_module.another_variable)
    # Para acessar atributos ou métodos dentro de objetos, utiliza-se do ponto

    # import turtle
    # timmy = turtle.Turtle()
    from turtle import Turtle, Screen

    # Atribuindo um construtor com a variável timmy
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color("DarkGoldenrod1")
    timmy.forward(100)

    print(timmy)
    my_screen = Screen()

    # Deve printar o tamanho atual da altura
    print(my_screen.canvheight)

    # Faz o programa abrir a tela e manter ela existindo até o momento em que clicamos nela.
    my_screen.exitonclick()



if __name__ == '__main__':
    main()
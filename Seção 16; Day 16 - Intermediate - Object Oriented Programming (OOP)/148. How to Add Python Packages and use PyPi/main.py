def main():
    from prettytable import PrettyTable
    # Novo objeto criado: 'table' a partir da PrettyTable
    table = PrettyTable()
    print(table)
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], "l")
    table.add_column("Type", ["Electric", "Water", "Fire"], "l")
    # Também podemos mudar o alinhamento da tabela diretamente pelo atributo ao invés de usar o parâmetro
    # do método .add_column()
    # table.align("l")
    print(table)


if __name__ == "__main__":
    main()


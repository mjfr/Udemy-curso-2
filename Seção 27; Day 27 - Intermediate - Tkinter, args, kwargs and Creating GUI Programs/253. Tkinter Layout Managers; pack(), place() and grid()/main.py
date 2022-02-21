import tkinter


def button_clicked():
    print("I got clicked")
    my_label.config(text="I got clicked")
    my_label.config(text=entry_input.get())


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # Adicionando padding em TODOS os widgets

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# Podemos configurar, atualizar ou alterar as propriedades de um componente que criamos
my_label["text"] = "New Text"
my_label.config(text="New Text 2")
# my_label.pack()
# my_label.place(x=100, y=200)  # É um método muito específico de expor componentes no aplicativo.
my_label.grid(column=0, row=0)  # É relativo a outros componentes. Não se altera se não houver outros componentes.
# Em um programa, NÃO PODEMOS misturar pack() e grid()
my_label.config(padx=50, pady=50)  # Adicionando padding em um widget específico

# Button
button = tkinter.Button(text="Click Me!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry (basicamente um input)
entry_input = tkinter.Entry(width=50)
# print(entry_input.get())
# entry_input.pack()
entry_input.grid(column=3, row=2)


window.mainloop()

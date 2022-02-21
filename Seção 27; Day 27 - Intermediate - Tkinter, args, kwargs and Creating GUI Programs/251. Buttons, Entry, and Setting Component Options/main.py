import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# Podemos configurar, atualizar ou alterar as propriedades de um componente que criamos
my_label["text"] = "New Text"
my_label.config(text="New Text 2")


# Button
def button_clicked():
    # my_label.config(text="I got clicked")
    my_label.config(text=entry_input.get())


button = tkinter.Button(text="Click Me!", command=button_clicked)
button.pack()


# Entry (basicamente um input)
entry_input = tkinter.Entry(width=50)
entry_input.pack()
print(entry_input.get())


window.mainloop()

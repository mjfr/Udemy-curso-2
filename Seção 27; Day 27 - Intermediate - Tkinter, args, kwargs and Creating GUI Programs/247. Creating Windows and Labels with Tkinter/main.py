import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
# A janela escala automaticamente conforme o conteúdo. Porém, podemos definir um tamanho mínimo para a janela
window.minsize(width=500, height=300)

# Label é um dos possíveis componentes que podemos usar no Tkinter
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold italic"))

# O componente não irá aparecer automaticamente na tela, para isso, podemos usar o método .pack() que centralizará o
# componente na tela criada
my_label.pack(side="bottom")

window.mainloop()

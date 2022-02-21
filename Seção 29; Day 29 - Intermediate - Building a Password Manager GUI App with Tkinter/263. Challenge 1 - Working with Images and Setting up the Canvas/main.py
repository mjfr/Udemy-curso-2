import tkinter
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
image_path = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_path)
canvas.grid(column=0, row=0)

window.mainloop()

import tkinter as tk
FONT = ("Segoe UI", 12, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
image_path = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_path)
canvas.grid(column=1, row=0)

website_label = tk.Label()
website_label.config(text="Website:", font=FONT, bg="white")
website_label.grid(column=0, row=1)
username_label = tk.Label()
username_label.config(text="E-mail/Username:", font=FONT, bg="white")
username_label.grid(column=0, row=2)
password_label = tk.Label()
password_label.config(text="Password:", font=FONT, bg="white")
password_label.grid(column=0, row=3)

add_button = tk.Button()
add_button.config(text="Add", command="FUNC", width=43, bg="white")
add_button.grid(column=1, row=4, columnspan=2)
generate_password_button = tk.Button()
generate_password_button.config(text="Generate Password", command="FUNC", bg="white")
generate_password_button.grid(column=2, row=3)

website_entry = tk.Entry()
website_entry.config(width=50, borderwidth=2)
website_entry.grid(column=1, row=1, columnspan=2)
username_entry = tk.Entry()
username_entry.config(width=50, borderwidth=2)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry = tk.Entry()
password_entry.config(width=32, borderwidth=2)
password_entry.grid(column=1, row=3)

window.mainloop()

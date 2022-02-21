import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
FONT = ("Segoe UI", 12, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(0, randint(8, 10))]
    password_list += [choice(symbols) for _ in range(0, randint(2, 4))]
    password_list += [choice(numbers) for _ in range(0, randint(2, 4))]

    shuffle(password_list)

    random_password = "".join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    login = username_entry.get()
    password = password_entry.get()

    if website == "" or login == "" or password == "":
        messagebox.showinfo(title="Empty Field Warning",
                            message="One or more fields are empty.\nPlease fill all fields")
    else:

        is_ok = messagebox.askokcancel(title="Save?", message=f"These are the details entered:"
                                                              f"\nWebsite: {website}\nLogin{login}"
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            pyperclip.copy(password)
            with open("data.txt", mode="a") as data:
                data.write(f"Website: {website}\t\t|\tLogin: {login}\t|\tPassword: {password}\n")
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)


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
add_button.config(text="Add", command=save, width=43, bg="white")
add_button.grid(column=1, row=4, columnspan=2)
generate_password_button = tk.Button()
generate_password_button.config(text="Generate Password", command=generate_password, bg="white")
generate_password_button.grid(column=2, row=3)

website_entry = tk.Entry()
website_entry.config(width=50, borderwidth=2)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
username_entry = tk.Entry()
username_entry.config(width=50, borderwidth=2)
username_entry.insert(0, "exemple@email.com")
username_entry.grid(column=1, row=2, columnspan=2)
password_entry = tk.Entry()
password_entry.config(width=32, borderwidth=2)
password_entry.grid(column=1, row=3)

window.mainloop()

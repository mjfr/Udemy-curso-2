import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT = ("Segoe UI", 12, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    new_data = {
        website: {
            "email": login,
            "password": password
        }
    }

    if website == "" or login == "" or password == "":
        messagebox.showinfo(title="Empty Field Warning",
                            message="One or more fields are empty.\nPlease fill all fields")
    else:

        is_ok = messagebox.askokcancel(title="Save?", message=f"These are the details entered:"
                                                              f"\nWebsite: {website}\nLogin: {login}"
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            pyperclip.copy(password)
            try:
                with open("data.json", mode="r") as data:
                    loaded_data = json.load(data)  # Lendo os dados desatualizados

            except FileNotFoundError:
                with open("data.json", mode="w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                loaded_data.update(new_data)  # Atualizando os dados que estavam desatualizados
                with open("data.json", "w") as updated_data:
                    json.dump(loaded_data, updated_data, indent=4)  # Salvando os dados atualizados
            finally:
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)


# ------------------------ Search  Registry --------------------------- #
def search():
    try:
        with open("data.json", mode="r") as data:
            json_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Save file not found", message="If you are seeing this message is because you "
                                                                 "probably have not saved any data yet.\n"
                                                                 "Try saving a website registry first, then you "
                                                                 "can search for the website.")
    else:
        try:
            searched_data = json_data[website_entry.get()]
            messagebox.showinfo(title="Search Result", message=f"Register found!\nWebsite: {website_entry.get()}\n"
                                                               f"E-mail/Username: {searched_data['email']}\n"
                                                               f"Password: {searched_data['password']}\n"
                                                               f"Your password is now in your clipboard.")
            pyperclip.copy(searched_data['password'])
        except KeyError as message_error:
            messagebox.showinfo(title="Search Result", message=f"There is no {message_error} in records, try saving it"
                                                               f" first.")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="white")

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
search_button = tk.Button()
search_button.config(text="Search", command=search, bg="white", width=14)
search_button.grid(column=2, row=1)

website_entry = tk.Entry()
website_entry.config(width=32, borderwidth=2)
website_entry.focus()
website_entry.grid(column=1, row=1)
username_entry = tk.Entry()
username_entry.config(width=51, borderwidth=2)
username_entry.insert(0, "exemple@email.com")
username_entry.grid(column=1, row=2, columnspan=2)
password_entry = tk.Entry()
password_entry.config(width=32, borderwidth=2)
password_entry.grid(column=1, row=3)

window.mainloop()

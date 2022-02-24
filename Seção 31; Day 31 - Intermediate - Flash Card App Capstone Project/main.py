import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_COLOR = "#91C2AF"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
current_card = {}


def generate_random_word(data_from_file):
    try:
        word = random.choice(data_from_file)
    except IndexError as message_error:
        print(f"When all words are removed, trying to get a item from a list will throw an IndexError exception: "
              f"{message_error}")
        language_label.config(text="You've done it!")
        word_label.config(text="You know all\nof the words!", bg="white", fg="black")
    else:
        print(word)
        return word


def next_card():
    global current_card, time_to_flip
    window.after_cancel(time_to_flip)
    try:
        current_card = generate_random_word(words_to_learn)
    except NameError:
        print("Running without words_to_learn.csv file thus NameError was generated because words_to_learn variable "
              "was not created.")
        current_card = generate_random_word(data_to_dict)
    show_card_front()
    try:
        word_label.config(text=current_card["French"], bg="white", fg="black")
    except TypeError as error_message:
        window.after_cancel(time_to_flip)
        language_label.config(text="You've done it!")
        word_label.config(text="You know all\nof the words!", bg="white", fg="black")
        print(f"After all words are seen and removed from words_to_learn.csv, next time current_card['French']"
              f" tries to recover it's word, a NoneType would be recovered thus it throws a TypeError exception: "
              f"{error_message}")
    else:
        time_to_flip = window.after(3000, func=flip_card)


def show_card_back():
    canvas.itemconfig(flash_card, image=card_back_image_path)
    language_label.config(text="English", bg=CARD_BACK_COLOR, fg="white")


def show_card_front():
    canvas.itemconfig(flash_card, image=card_front_image_path)
    language_label.config(text="French", bg="white", fg="black")


# --------------------- Using data from .csv ---------------------#
data = pandas.read_csv(filepath_or_buffer="./data/french_words.csv")
data_to_dict = data.to_dict(orient="records")

try:
    words_to_learn_data = pandas.read_csv(filepath_or_buffer="./data/words_to_learn.csv")
except FileNotFoundError:
    print("There is no words_to_learn.csv file yet")
except pandas.errors.EmptyDataError:
    print("Data resets here")
else:
    words_to_learn = words_to_learn_data.to_dict(orient="records")


# ------------------------ Button actions ------------------------#
def right():
    try:
        words_to_learn.remove(current_card)
        pandas.DataFrame(words_to_learn).to_csv(index=False, path_or_buf="./data/words_to_learn.csv")
    except ValueError:
        print("There is no cards to remove anymore")
    except NameError:
        try:
            data_to_dict.remove(current_card)
            pandas.DataFrame(data_to_dict).to_csv(index=False, path_or_buf="./data/words_to_learn.csv")
        except ValueError:
            print("There is no cards to remove anymore")
    next_card()


def wrong():
    next_card()


# ---------------------- Timer to Flip Card ----------------------#
def flip_card():
    show_card_back()
    try:
        word_label.config(text=current_card["English"], bg=CARD_BACK_COLOR, fg="white")
    except TypeError:
        print("No more words to show")


# --------------------------- UI Setup ---------------------------#
# Window setup
window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
time_to_flip = window.after(3000, func=flip_card)

# Images setup
card_back_image_path = tk.PhotoImage(file="./images/card_back.png")
card_front_image_path = tk.PhotoImage(file="./images/card_front.png")
right_button_image_path = tk.PhotoImage(file="./images/right.png")
wrong_button_image_path = tk.PhotoImage(file="./images/wrong.png")

# Canvas setup
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card = canvas.create_image(400, 263, image=card_front_image_path)
canvas.grid(column=0, row=0, columnspan=2, rowspan=5)

# Buttons setup
right_button = tk.Button(image=right_button_image_path, borderwidth=0, highlightthickness=0, command=right)
right_button.grid(column=1, row=5)
wrong_button = tk.Button(image=wrong_button_image_path, borderwidth=0, highlightthickness=0, command=wrong)
wrong_button.grid(column=0, row=5)

# Labels setup
language_label = tk.Label()
language_label.config(text="", font=LANGUAGE_FONT, bg="white")
language_label.grid(column=0, row=1, columnspan=2)
word_label = tk.Label()
word_label.config(text="", font=WORD_FONT, bg="white")
word_label.grid(column=0, row=2, columnspan=2)

next_card()

window.mainloop()

# TODO 1 - Build a Typing Speed Test GUI software.
import tkinter as tk
from essential_generators import DocumentGenerator

window = tk.Tk()
window.title("Furious Fingers")
# window.config()

FONT = ("Segoe UI", 12, "normal")
data = {
    "time": 60,
    "typed_entries": 0,
    "total_characters": 0,
    "total_errors": 0,
    "uncorrected_errors": 0
}


def calc_gross_wpm(characters: int, seconds: int):
    return (characters / 5) / (seconds / 60)


def calc_net_wpm(gross_wpm: int, errors: int, seconds: int):
    return gross_wpm - (errors / (seconds / 60))


def calc_correct_characters(total: int, errors: int):
    return total - errors


def calc_accuracy(correct: int, total: int):
    return correct / total * 100


def gen_random_sentence():
    global data
    dg = DocumentGenerator()
    sentence = dg.sentence().replace("\n", " ")
    while len(sentence) < 300:
        sentence += f" {dg.sentence()}"
    sentence_list = [character for character in sentence]
    data["total_characters"] = len(sentence)
    return sentence, sentence_list


sentence_letters = gen_random_sentence()


def match_word(event):
    print(event)
    try:
        last_typed = text_entry.get()[-1]
    except IndexError:
        pass
    if event.char and event.char != "\t" and event.char != "\r" and event.char != "\n":
        # print(event.state)
        data["typed_entries"] += 1
        last_character = sentence_letters[1][0]
        if last_character == last_typed:
            current_character = sentence_letters[1].pop(sentence_letters[1].index(last_character))
            print(last_character)
            print(sentence_letters[1])
            print("Match")
        else:
            print("Não deu match")
            data["total_errors"] += 1
    # print(text_entry.get())
    # print(event)


text_label = tk.Label()
text_label.config(text=sentence_letters[0], font=FONT, wraplength=500)
text_label.grid(column=0, row=0, pady=15)

text_entry = tk.Entry(width=100)
text_entry.grid(column=0, row=1, pady=15, padx=30)
text_entry.bind("<KeyRelease>", match_word)

window.mainloop()

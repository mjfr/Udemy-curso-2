# TODO 1 - Build a Typing Speed Test GUI software.
import tkinter as tk
from essential_generators import DocumentGenerator


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Furious Fingers")
        self.resizable(False, False)
        self.text_entry = None
        self.text_label = None
        self.timer = None
        self.start_timer_btn = None
        self.reset_btn = None
        self.after_aux = None
        self.time = 63
        self.typed_entries = 0
        self.total_characters = 0
        self.total_errors = 0
        self.uncorrected_errors = 0
        self.sentence = self.gen_random_sentence()
        self.create_widgets()
        self.gross_wps = 0
        self.net_wps = 0
        self.correct_characters = 0
        self.accuracy = 0

    def place_text(self):
        self.text_label = tk.Label(text="", font=("Segoe UI", 12, "normal"), wraplength=500)
        self.text_label.grid(column=0, row=1, pady=15, columnspan=3)

    def place_entry(self):
        self.text_entry = tk.Entry(width=100)
        self.text_entry.grid(column=0, row=2, pady=15, padx=30, columnspan=3)
        self.text_entry["state"] = "disabled"
        self.text_entry.bind("<KeyPress>", self.match_words)

    def place_timer(self):
        self.timer = tk.Label(text="Remaining time: 60 seconds", justify="center", foreground="red")
        self.timer.grid(column=1, row=0, pady=20)

    def place_buttons(self):
        self.start_timer_btn = tk.Button(text="Start", command=self.start_timer)
        self.start_timer_btn.grid(column=0, row=0)
        self.reset_btn = tk.Button(text="Reset", command=self.reset)
        self.reset_btn.grid(column=2, row=0)

    def start_timer(self):
        self.after_aux = self.after(500, self.update_timer)

    def update_timer(self):
        if self.time > 0:
            if self.time > 60:
                self.text_label.configure(text=f"Get prepared! Text appearing in {self.time - 60} seconds")
            else:
                # self.text_label.configure(text=self.sentence["sentence"])
                self.text_label.configure(text=self.sentence)
                self.text_entry["state"] = "normal"
                self.text_entry.focus_set()
            self.after_aux = self.after(500, self.start_timer)
            self.time -= 1
            if self.time <= 60:
                self.timer.configure(text=f"Remaining time: {self.time} seconds")
        else:
            self.text_entry["state"] = "disabled"
            self.gross_wps = self.calc_gross_wpm()
            self.net_wps = self.calc_net_wpm()
            self.correct_characters = self.calc_correct_characters()
            self.accuracy = self.calc_accuracy()
            self.text_label.configure(text=f"Your stats are:\n"
                                           f"Gross Words per Second: {self.gross_wps:.4};\n"
                                           f"Net Words per Second: {self.net_wps:.4};\n"
                                           f"Correct Characters: {self.correct_characters}/{self.typed_entries};\n"
                                           f"Correct Characters: {self.correct_characters}/{len(self.sentence)};\n"
                                           f"With an accuracy of: {self.accuracy:.4}%")

    def reset(self):
        self.after_cancel(self.after_aux)
        self.time = 63
        self.timer.configure(text="Remaining time: 60 seconds")
        self.sentence = self.gen_random_sentence()
        self.text_label.configure(text="")
        self.text_entry["state"] = "normal"
        self.text_entry.delete(0, "end")
        self.text_entry["state"] = "disabled"
        self.typed_entries = 0
        self.total_characters = 0
        self.total_errors = 0
        self.uncorrected_errors = 0

    def create_widgets(self):
        self.place_timer()
        self.place_text()
        self.place_entry()
        self.place_buttons()

    def gen_random_sentence(self):
        dg = DocumentGenerator()
        sentence = dg.sentence()
        while len(sentence) < 300:
            sentence += f" {dg.sentence()}"
        sentence = sentence.replace("\n", " ").replace("–", "-").replace("—", "-")
        # sentence_list = [character for character in sentence]
        self.total_characters = len(sentence)
        # return {"sentence": sentence, "letters": sentence_list}
        return sentence

    def match_words(self, event):
        # if last_typed is None or last_typed == "":
        #     last_typed = self.text_entry.get()
        # else:
        #     last_typed = self.text_entry.get()

        # try:
        #     last_typed = self.text_entry.get()
        #     print(repr(last_typed))
        #     # last_typed = self.text_entry.get()[-1]
        # except IndexError:
        #     pass

        if event.char and event.char != "\t" and event.char != "\r" and event.char != "\n" and event.char != "\x1b" \
                and event.char != "\x08":
            last_typed = self.text_entry.get()
            if last_typed is None or last_typed == "":
                last_typed = event.char
            self.typed_entries += 1
            # print(event)
            err_index = [self.add_error(i, letter1 != letter2) for i, (letter1, letter2) in enumerate(zip(self.sentence, last_typed)) if letter1 != letter2]
            self.uncorrected_errors = len(err_index)
            print(self.total_errors)
            print(last_typed)
            print(err_index)
            # Gera erro quando acaba, talvez fazer um try exception para levar à contagem dos acertos, etc.
            # last_character = self.sentence["letters"][0]
            # if last_character == last_typed:
            #     current_character = self.sentence["letters"].pop(self.sentence["letters"].index(last_character))
            #     print(last_character)
            #     print(self.sentence["letters"])
            # else:
            #     print("Não deu match")
            #     self.total_errors += 1

    def add_error(self, index: int, condition: bool):
        if condition:
            self.total_errors += 1
        return index

    def calc_gross_wpm(self):
        return (self.typed_entries / 5) / abs(self.time - 60)

    def calc_net_wpm(self):
        return self.gross_wps - (self.uncorrected_errors / abs(self.time - 60))

    def calc_correct_characters(self):
        return self.typed_entries - self.total_errors

    def calc_accuracy(self):
        return self.correct_characters / self.typed_entries * 100


app = App()
app.mainloop()

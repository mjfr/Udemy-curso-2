# TODO 1 - Build a Typing Speed Test GUI software.
import tkinter as tk
from essential_generators import DocumentGenerator


def gen_random_sentence():
    dg = DocumentGenerator()
    sentence = dg.sentence()
    while len(sentence) < 150:
        sentence += f" {dg.sentence()}"
    sentence = sentence.replace("\n", " ").replace("–", "-").replace("—", "-")
    return sentence


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Furious Fingers")
        self.resizable(False, False)
        self.text = None
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
        self.create_widgets()
        self.sentence = gen_random_sentence()
        self.gross_wps = 0
        self.net_wps = 0
        self.correct_characters = 0
        self.current_correct_characters = 0
        self.accuracy = 0
        self.err_index = []

    def place_text(self):
        self.text_label = tk.Label(text="", font=("Segoe UI", 12, "normal"), wraplength=500)
        self.text_label.grid(column=0, row=1, pady=15, columnspan=3)

    def place_textbox(self):
        self.text = tk.Text(width=70, height=5)
        self.text.grid(column=0, row=2, pady=15, padx=30, columnspan=3)
        self.text["state"] = "disabled"
        self.text.bind("<Return>", lambda e: "break")
        self.text.bind("<KeyRelease>", self.match_words)

    def place_timer(self):
        self.timer = tk.Label(text="Remaining time: 60 seconds", justify="center", foreground="red")
        self.timer.grid(column=1, row=0, pady=20)

    def place_buttons(self):
        self.start_timer_btn = tk.Button(text="Start", command=self.start_timer)
        self.start_timer_btn.grid(column=0, row=0)
        self.reset_btn = tk.Button(text="Reset", command=self.reset)
        self.reset_btn.bind("<Button-1>", lambda e: self.text_label.configure(text="Generating new text, please wait."))
        self.reset_btn.grid(column=2, row=0)

    def start_timer(self):
        self.after_aux = self.after(500, self.update_timer)

    def update_timer(self):
        if self.sentence == self.text.get("1.0", "end-1c"):
            self.after_cancel(self.after_aux)
            self.show_statistics()
        elif self.time > 0:
            if self.time > 60:
                self.text_label.configure(text=f"Get prepared! Text appearing in {self.time - 60} seconds")
            else:
                self.text_label.configure(text=self.sentence)
                self.text["state"] = "normal"
                self.text.focus_set()
            self.after_aux = self.after(500, self.start_timer)
            self.time -= 1
            if self.time <= 60:
                self.timer.configure(text=f"Remaining time: {self.time} seconds")
        else:
            self.show_statistics()

    def show_statistics(self):
        self.text["state"] = "disabled"
        self.gross_wps = self.calc_gross_wpm()
        self.net_wps = self.calc_net_wpm()
        self.correct_characters = self.calc_correct_characters()
        self.accuracy = self.calc_accuracy()
        self.current_correct_characters = self.calc_current_correct_characters()
        self.total_characters = len(self.sentence)
        self.text_label.configure(
            text=f"Your stats are:\n"
                 f"Gross Words per Second: {self.gross_wps:.4}\n"
                 f"Net Words per Second: {self.net_wps:.4}\n"
                 f"Gross Words per Minute: {self.gross_wps * 60:.4}\n"
                 f"Net Words per Minute: {self.net_wps * 60:.4}\n"
                 f"Correct/Typed Characters: {self.correct_characters}/{self.typed_entries}\n"
                 f"Correct/Total Characters: {self.current_correct_characters}/{self.total_characters}\n"
                 f"With an accuracy of: {self.accuracy:.4}%"
        )

    def reset(self):
        try:
            self.after_cancel(self.after_aux)
        except ValueError:
            pass
        self.time = 63
        self.timer.configure(text="Remaining time: 60 seconds")
        self.sentence = gen_random_sentence()
        self.text_label.configure(text="")
        self.text["state"] = "normal"
        self.text.delete("1.0", "end-1c")
        self.text["state"] = "disabled"
        self.typed_entries = 0
        self.total_characters = 0
        self.total_errors = 0
        self.uncorrected_errors = 0
        self.current_correct_characters = 0

    def create_widgets(self):
        self.place_timer()
        self.place_text()
        self.place_textbox()
        self.place_buttons()

    def match_words(self, event):
        if event.char and event.char != "\t" and event.char != "\x1b" and event.char != "\x08" \
                and self.text["state"] == "normal":
            last_typed = self.text.get("1.0", "end-1c")
            if last_typed is None or last_typed == "":
                last_typed = event.char
            self.typed_entries += 1
            self.err_index = [self.add_error(i) for i, (letter1, letter2) in
                              enumerate(zip(self.sentence, last_typed)) if letter1 != letter2]
            self.uncorrected_errors = len(self.err_index)

    def add_error(self, index: int):
        self.text.tag_config("error", foreground="red")
        self.text.tag_add("error", f"1.{index}", f"1.{index+1}")
        if not self.err_index.count(index):
            self.total_errors += 1
        return index

    def calc_gross_wpm(self):
        return (self.typed_entries / 5) / abs(self.time - 60)

    def calc_net_wpm(self):
        return self.gross_wps - (self.uncorrected_errors / abs(self.time - 60))

    def calc_correct_characters(self):
        return self.typed_entries - self.total_errors

    def calc_current_correct_characters(self):
        self.text["state"] = "normal"
        correct_characters_count = len(self.text.get("1.0", "end-1c")) - self.uncorrected_errors
        self.text["state"] = "disabled"
        return correct_characters_count

    def calc_accuracy(self):
        return self.correct_characters / self.typed_entries * 100


app = App()
app.mainloop()

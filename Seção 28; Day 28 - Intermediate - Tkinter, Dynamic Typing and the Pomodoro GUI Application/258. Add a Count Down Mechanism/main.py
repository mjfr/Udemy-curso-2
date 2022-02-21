import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)  # Pega uma quantidade de tempo que o método
    # deve esperar e depois executa uma função


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img_path = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img_path)
# Atribuindo o texto do canvas a uma variável para usar na função da contagem regressiva
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button()
start_button.config(text="Start", bg=GREEN, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = tkinter.Button()
reset_button.config(text="Reset", bg=RED, highlightthickness=0)
reset_button.grid(column=2, row=2)

title_label = tkinter.Label()
title_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 60, "normal"))
title_label.grid(column=1, row=0)
check_label = tkinter.Label()
check_label.config(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=4)

window.mainloop()

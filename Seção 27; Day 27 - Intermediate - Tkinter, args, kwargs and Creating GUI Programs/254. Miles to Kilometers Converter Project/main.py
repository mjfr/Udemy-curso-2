import tkinter
FONT = ("Segoe UI", 18, "normal")


def calculate():
    miles = miles_input.get()
    miles_to_km = round(float(miles) * 1.60934, 2)
    converted_label.config(text=miles_to_km)


window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=400, height=150)
window.config(padx=20, pady=15)

miles_input = tkinter.Entry()
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
equal_to_label = tkinter.Label(text="is equal to", font=FONT)
equal_to_label.grid(column=0, row=1)
converted_label = tkinter.Label(text=0, font=FONT)
converted_label.grid(column=1, row=1)
kilometers_label = tkinter.Label(text="Kilometers", font=FONT)
kilometers_label.grid(column=2, row=1)

calculate_button = tkinter.Button()
calculate_button.config(text="Calculate", font=FONT, command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()

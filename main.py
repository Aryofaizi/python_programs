import tkinter as tk

window = tk.Tk()

fahrenheit_lable = tk.Label(
    master=window,
    text="Fahrenheit:",
)
fahrenheit_entry = tk.Entry(
    master=window,
)
calc_button = tk.Button(
    master=window,
    text="Calc",
)
celsius_label = tk.Label(
    master=window,
    text="Celsius",
)
result_label = tk.Label(
    master=window,
    text="info",
)

window.mainloop()





import tkinter as tk
from tkinter import E,W,N,S
window = tk.Tk()

window.wm_title("This is my app")

fahrenheit_lable = tk.Label(
    master=window,
    text="Fahrenheit:",
    width=12,
    height=2,
)
fahrenheit_entry = tk.Entry(
    master=window,
    width=55,
)
calc_button = tk.Button(
    master=window,
    text="Calc",
    width=9,
)
celsius_label = tk.Label(
    master=window,
    text="Celsius",
    height=2,
)
result_label = tk.Label(
    master=window,
    text="Result will be shown here...",
)
fahrenheit_lable.grid(row=0,column=0)
fahrenheit_entry.grid(row=0,column=1)
calc_button.grid(row=0,column=2)
celsius_label.grid(row=1,column=0)
result_label.grid(row=1,column=1)
window.mainloop()





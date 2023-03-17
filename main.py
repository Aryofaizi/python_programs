import tkinter as tk
from tkinter import E,W,N,S
window = tk.Tk()

window.wm_title("This is my app")

lbl_fahrenheit = tk.Label(
    master=window,
    text="Fahrenheit:",
    width=12,
    height=2,
)
ent_fahrenheit = tk.Entry(
    master=window,
    width=55,
)
btn_calc = tk.Button(
    master=window,
    text="Calc",
    width=9,
)
lbl_celsius = tk.Label(
    master=window,
    text="Celsius",
    height=2,
)
lbl_result = tk.Label(
    master=window,
    text="Result will be shown here...",
)
lbl_fahrenheit.grid(row=0,column=0)
ent_fahrenheit.grid(row=0,column=1)
btn_calc.grid(row=0,column=2)
lbl_celsius.grid(row=1,column=0)
lbl_result.grid(row=1,column=1)
window.mainloop()





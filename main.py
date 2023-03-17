import tkinter as tk
from tkinter import E,W,N,S
window = tk.Tk()

window.title("This is my app")


def fahrenheit_to_celcius(faren):
    return (5/9) * (faren-32)

lbl_fahrenheit = tk.Label(
    master=window,
    text="Fahrenheit:",
)
ent_fahrenheit = tk.Entry(
    master=window,
    width=55,
)

def btn_command():
    try:
        assert not len(ent_fahrenheit.get()) == 0
    except AssertionError:
        lbl_result["text"] = "input empty..."
    else:
        try:
            faren_value = float(ent_fahrenheit.get())
            celcius = fahrenheit_to_celcius(faren_value)
        except ValueError:
            lbl_result["text"] = "you should enter number"
        else:
            lbl_result["text"] = celcius

btn_calc = tk.Button(
    master=window,
    text="Calc",
    width=9,
    command=btn_command
)
lbl_celsius = tk.Label(
    master=window,
    text="Celsius",
)
lbl_result = tk.Label(
    master=window,
    text="Result will be shown here...",
)
lbl_fahrenheit.grid(row=0,column=0,padx=10,pady=(10,5))
ent_fahrenheit.grid(row=0,column=1,padx=10,pady=(10,5))
btn_calc.grid(row=0,column=2,padx=10,pady=(10,5))
lbl_celsius.grid(row=1,column=0,padx=10,pady=(10,20))
lbl_result.grid(row=1,column=1,padx=10,pady=(10,20))
window.mainloop()





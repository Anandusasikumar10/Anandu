import tkinter as tk
import math

def calculate_expression(expr):
    try:
        expr = expr.replace("^", "**")
        expr = expr.replace("√", "math.sqrt")
        expr = expr.replace("log", "math.log10")
        expr = expr.replace("sin", "math.sin(math.radians")
        expr = expr.replace("cos", "math.cos(math.radians")
        expr = expr.replace("tan", "math.tan(math.radians")

        open_count = expr.count("math.sin(math.radians") + expr.count("math.cos(math.radians") + expr.count("math.tan(math.radians")
        expr += ")" * open_count

        return eval(expr)
    except:
        return "Error"

def click(event):
    button_text = event.widget["text"]
    current = entry.get()

    if button_text == "=":
        result = calculate_expression(current)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# GUI
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="#1e1e2f")

entry = tk.Entry(root, font=("Consolas", 24), borderwidth=0, relief=tk.FLAT, justify="right", bg="#282c34", fg="white")
entry.grid(row=0, column=0, columnspan=6, pady=20, padx=10, ipadx=10, ipady=10, sticky="we")

buttons = [
    ["7", "8", "9", "/", "C", "√("],
    ["4", "5", "6", "*", "(", ")"],
    ["1", "2", "3", "-", "^", "log("],
    ["0", ".", "=", "+", "sin(", "cos("],
    ["tan("]
]

button_color = "#3e4451"
hover_color = "#5c6370"
text_color = "white"

def on_enter(e):
    e.widget["background"] = hover_color

def on_leave(e):
    e.widget["background"] = button_color

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        b = tk.Button(root, text=buttons[i][j], font=("Consolas", 18), width=5, height=2,
                      bg=button_color, fg=text_color, activebackground=hover_color, borderwidth=0)
        b.grid(row=i+1, column=j, padx=5, pady=5)
        b.bind("<Button-1>", click)
        b.bind("<Enter>", on_enter)
        b.bind("<Leave>", on_leave)

root.mainloop()